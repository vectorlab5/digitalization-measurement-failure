#!/usr/bin/env python3
"""
Monte Carlo study of same-source proxy bias.

Reproduces and generalizes the single-seed controlled experiment. For each
data-generating process (DGP) we draw R independent balanced panels in which
latent "true digitalization" D* is, by construction, independent of revenue,
and we run the same proxy regression used in the empirical illustration:

    Y_it (revenue growth)  ~  X_{i,t-1} (industry-year revenue rank)
                              + firm FE + year FE

Because D* is orthogonal to revenue, any nonzero coefficient is produced by the
shared revenue source (same-source structure), not by a digitalization effect.

Per DGP we report: mean beta_hat, bias, RMSE, mean cluster-robust SE, empirical
rejection rate at 5% (size under the true null), and coverage of the nominal
95% CI for the true parameter.

DGP variants:
  A  baseline null            : random-walk log revenue, single industry, beta*=0
  B  + industry heterogeneity : K industries, heterogeneous drift/volatility
  C  + time trends            : common year effects + firm-specific linear trends
  D  + AR(1) revenue          : persistent (rho=0.8) rather than unit-root revenue
  E  true effect (proxy/direct): D* has a REAL effect beta*=0.5 on a DIRECT
                                 outcome Y*; proxy regression vs direct regression
  F  sample-size sweep        : rejection rate and mean |t| vs N (baseline null)

Storage layout: every long array is ordered as year-blocks of N firms, i.e.
shape (Tobs, N) row-major with Tobs = T-1. This makes the two-way within
transform and firm clustering fully vectorized. Only numpy is used; two-sided
p-values use the normal approximation (|t| > 1.96 at 5%). Deterministic: a
master seed spawns one child seed per replication.
"""
import numpy as np
import math
import json
import csv
import os

Z975 = 1.959963984540054


def rank_within_year(Rprev, industry, K):
    """Percentile rank in [0,1] of revenue at t-1 within each (industry) group,
    for one year. Rprev, industry are length-N arrays. Returns length-N."""
    N = Rprev.size
    if K == 1:
        order = Rprev.argsort(kind="mergesort")
        r = np.empty(N, dtype=float)
        r[order] = np.arange(N, dtype=float)
        return r / (N - 1)
    out = np.empty(N, dtype=float)
    for k in range(K):
        m = industry == k
        v = Rprev[m]
        n = v.size
        order = v.argsort(kind="mergesort")
        r = np.empty(n, dtype=float)
        r[order] = np.arange(n, dtype=float)
        out[m] = r / (n - 1) if n > 1 else 0.5
    return out


def fe_slope_cluster(Y, X, N, Tobs):
    """Two-way FE slope of Y on scalar X with firm-clustered robust SE (CR1).
    Y, X are (Tobs, N) arrays: rows = years, cols = firms."""
    def within(A):
        col = A.mean(axis=0, keepdims=True)   # firm mean (over years)
        row = A.mean(axis=1, keepdims=True)   # year mean (over firms)
        return A - col - row + A.mean()
    Yt = within(Y); Xt = within(X)
    sxx = float((Xt * Xt).sum())
    beta = float((Xt * Yt).sum()) / sxx
    e = Yt - beta * Xt
    # firm clusters = columns
    g = (Xt * e).sum(axis=0)                  # length-N score sums per firm
    meat = float((g * g).sum())
    G = N
    n = N * Tobs
    k = 1 + G + (Tobs)                        # slope + firm FE + year FE(=Tobs here)
    dof = (G / (G - 1.0)) * ((n - 1.0) / max(n - k, 1.0))
    var = dof * meat / (sxx * sxx)
    se = math.sqrt(var)
    return beta, se, beta / se


def make_panel(rng, N, T, K=1, dgp="A", beta_star=0.0):
    """Return X, Y (and optionally Ystar, D) as (Tobs, N) arrays plus r, industry."""
    industry = np.arange(N) % K
    sigma = 0.06      # level-shock SD of the log-revenue random walk
    sigma0 = 0.13     # cross-sectional dispersion of initial log revenue
    tau = 0.08        # idiosyncratic growth noise (keeps growth SD ~ 0.10)
    r = np.empty((N, T))
    r[:, 0] = rng.normal(3.0, sigma0, size=N)
    if dgp == "B":
        ind_drift = rng.normal(0.0, 0.02, size=K)[industry]
        ind_vol = (0.04 + 0.05 * (np.arange(K) / max(K - 1, 1)))[industry]
        for t in range(1, T):
            r[:, t] = r[:, t-1] + ind_drift + rng.normal(0.0, 1.0, size=N) * ind_vol
    elif dgp == "C":
        year_fx = np.cumsum(rng.normal(0.0, 0.03, size=T))
        firm_trend = rng.normal(0.0, 0.015, size=N)
        for t in range(1, T):
            r[:, t] = r[:, t-1] + firm_trend + (year_fx[t]-year_fx[t-1]) \
                      + rng.normal(0.0, sigma, size=N)
    elif dgp == "D":
        rho = 0.8
        mu = r[:, 0].copy()
        for t in range(1, T):
            r[:, t] = mu + rho * (r[:, t-1] - mu) + rng.normal(0.0, sigma, size=N)
    else:
        for t in range(1, T):
            r[:, t] = r[:, t-1] + rng.normal(0.0, sigma, size=N)

    R = np.exp(r)
    Dstar = rng.normal(0.0, 1.0, size=(N, T))
    Tobs = T - 1
    X = np.empty((Tobs, N)); Y = np.empty((Tobs, N)); D = np.empty((Tobs, N))
    for j, t in enumerate(range(1, T)):
        X[j] = rank_within_year(R[:, t-1], industry, K)
        Y[j] = np.clip(r[:, t] - r[:, t-1] + rng.normal(0.0, tau, size=N), -2.0, 2.0)
        D[j] = Dstar[:, t]
    out = dict(X=X, Y=Y, D=D, r=r, industry=industry, N=N, Tobs=Tobs)
    if dgp == "E":
        Ys = np.empty((Tobs, N))
        for j, t in enumerate(range(1, T)):
            Ys[j] = beta_star * Dstar[:, t] + rng.normal(0.0, 1.0, size=N)
        out["Ystar"] = Ys
    return out


def summarize(betas, ses, ts, true_val):
    betas = np.asarray(betas); ses = np.asarray(ses); ts = np.asarray(ts)
    return dict(
        mean_beta=float(betas.mean()),
        bias=float(betas.mean() - true_val),
        rmse=float(np.sqrt(np.mean((betas - true_val) ** 2))),
        mean_se=float(ses.mean()),
        sd_beta=float(betas.std(ddof=1)),
        reject_rate=float(np.mean(np.abs(ts) > Z975)),
        coverage=float(np.mean((betas - Z975 * ses <= true_val) &
                               (true_val <= betas + Z975 * ses))),
        mean_abs_t=float(np.abs(ts).mean()),
    )


def run_variant(name, dgp, N, T, K, R, master_seed, beta_star=0.0):
    child = np.random.SeedSequence(master_seed).spawn(R)
    betas = np.empty(R); ses = np.empty(R); ts = np.empty(R)
    have_direct = (dgp == "E")
    db = np.empty(R); dse = np.empty(R); dt = np.empty(R)
    for i in range(R):
        rng = np.random.default_rng(child[i])
        p = make_panel(rng, N, T, K=K, dgp=dgp, beta_star=beta_star)
        b, se, t = fe_slope_cluster(p["Y"], p["X"], p["N"], p["Tobs"])
        betas[i] = b; ses[i] = se; ts[i] = t
        if have_direct:
            b2, se2, t2 = fe_slope_cluster(p["Ystar"], p["D"], p["N"], p["Tobs"])
            db[i] = b2; dse[i] = se2; dt[i] = t2
    res = {"name": name, "dgp": dgp, "N": N, "T": T, "K": K, "reps": R,
           "proxy": summarize(betas, ses, ts, 0.0)}
    if have_direct:
        res["direct"] = summarize(db, dse, dt, beta_star)
        res["beta_star"] = beta_star
    return res


def corr_D_revenue(master_seed, N=500, T=4):
    rng = np.random.default_rng(master_seed)
    p = make_panel(rng, N, T, K=1, dgp="A")
    rev = p["r"][:, 1:T].T.reshape(-1)          # (Tobs, N) matching D
    D = p["D"].reshape(-1)
    return (float(np.corrcoef(D, rev)[0, 1]),
            float(np.corrcoef(D, np.exp(rev))[0, 1]))


def main():
    os.makedirs("mc_out", exist_ok=True)
    MASTER = 20240517
    REPS = 2000
    results = [
        run_variant("A. Baseline (random walk)", "A", 500, 4, 1, REPS, MASTER+1),
        run_variant("B. + Industry heterogeneity", "B", 500, 4, 10, REPS, MASTER+2),
        run_variant("C. + Time trends", "C", 500, 4, 1, REPS, MASTER+3),
        run_variant("D. + AR(1) revenue", "D", 500, 4, 1, REPS, MASTER+4),
        run_variant("E. True effect (beta*=0.5)", "E", 500, 4, 1, REPS, MASTER+5, beta_star=0.5),
    ]
    sweep = []
    for N in [100, 500, 2000, 8000]:
        r = run_variant(f"F.N={N}", "A", N, 4, 1, 1000, MASTER+100+N)
        sweep.append({"N": N, **r["proxy"]})
    corr1, corr2 = corr_D_revenue(MASTER+777)

    rng = np.random.default_rng(42)
    p = make_panel(rng, 500, 4, K=1, dgp="A")
    b0, se0, t0 = fe_slope_cluster(p["Y"], p["X"], p["N"], p["Tobs"])
    single = {"seed": 42, "beta": b0, "se": se0, "t": t0, "N": int(p["Y"].size),
              "y_mean": float(p["Y"].mean()), "y_sd": float(p["Y"].std()),
              "x_mean": float(p["X"].mean()), "x_sd": float(p["X"].std())}

    out = {"reps": REPS, "master_seed": MASTER, "variants": results,
           "size_sweep": sweep, "corr_D_logrev": corr1, "corr_D_rev": corr2,
           "single_seed42": single}
    with open("mc_out/results.json", "w") as f:
        json.dump(out, f, indent=2)

    print("=== Single-seed reference (seed 42, N=500,T=4) ===")
    print(f"  beta={single['beta']:.3f}  SE={single['se']:.3f}  t={single['t']:.2f}  N={single['N']}")
    print(f"  y(growth) mean={single['y_mean']:.3f} sd={single['y_sd']:.3f} | "
          f"x(rank) mean={single['x_mean']:.3f} sd={single['x_sd']:.3f}")
    print(f"  corr(D*, log revenue)={corr1:+.3f}   corr(D*, revenue)={corr2:+.3f}\n")
    print(f"=== Monte Carlo (REPS={REPS}) : proxy regression, true effect = 0 ===")
    print(f"{'Variant':32s} {'meanb':>7s} {'bias':>7s} {'RMSE':>6s} {'meanSE':>7s} "
          f"{'reject%':>8s} {'cover%':>7s} {'mean|t|':>7s}")
    for r in results:
        s = r["proxy"]
        print(f"{r['name']:32s} {s['mean_beta']:7.3f} {s['bias']:7.3f} {s['rmse']:6.3f} "
              f"{s['mean_se']:7.3f} {100*s['reject_rate']:8.1f} {100*s['coverage']:7.1f} {s['mean_abs_t']:7.2f}")
    e = [r for r in results if r['dgp'] == 'E'][0]
    s = e["direct"]; sp = e["proxy"]
    print("\n=== Variant E: direct-measure estimator (true beta*=0.5) ===")
    print(f"  direct Y* on D*:  mean_beta={s['mean_beta']:.3f}  bias={s['bias']:+.3f}  "
          f"RMSE={s['rmse']:.3f}  reject%={100*s['reject_rate']:.1f}  cover%={100*s['coverage']:.1f}")
    print(f"  proxy  Y  on X :  mean_beta={sp['mean_beta']:.3f}  (target 0.5 -> "
          f"bias={sp['mean_beta']-0.5:+.3f})  reject%={100*sp['reject_rate']:.1f}")
    print("\n=== F. Size sweep (baseline null, T=4) ===")
    print(f"{'N':>6s} {'reject%':>8s} {'mean|t|':>8s} {'meanb':>7s} {'RMSE':>6s} {'cover%':>7s}")
    for row in sweep:
        print(f"{row['N']:6d} {100*row['reject_rate']:8.1f} {row['mean_abs_t']:8.2f} "
              f"{row['mean_beta']:7.3f} {row['rmse']:6.3f} {100*row['coverage']:7.1f}")

    with open("mc_out/variants.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["variant", "mean_beta", "bias", "rmse", "mean_se",
                    "reject_rate", "coverage", "mean_abs_t"])
        for r in results:
            s = r["proxy"]
            w.writerow([r["name"], f"{s['mean_beta']:.4f}", f"{s['bias']:.4f}",
                        f"{s['rmse']:.4f}", f"{s['mean_se']:.4f}", f"{s['reject_rate']:.4f}",
                        f"{s['coverage']:.4f}", f"{s['mean_abs_t']:.4f}"])
    with open("mc_out/sizesweep.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["N", "reject_rate", "mean_abs_t", "mean_beta", "rmse", "coverage"])
        for row in sweep:
            w.writerow([row["N"], f"{row['reject_rate']:.4f}", f"{row['mean_abs_t']:.4f}",
                        f"{row['mean_beta']:.4f}", f"{row['rmse']:.4f}", f"{row['coverage']:.4f}"])


if __name__ == "__main__":
    main()
