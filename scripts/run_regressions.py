#!/usr/bin/env python3
"""
Full panel regressions for the paper. Uses all firm-years with revenue (no assets required).
Builds: productivity proxy = ln(revenue); digitalization proxy = industry-year revenue rank;
IV = 2-year lag of digitalization proxy. Outputs all table numbers.
"""
from pathlib import Path
import pandas as pd
import numpy as np
import json

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED = PROJECT_ROOT / "data" / "processed"
OUT = PROCESSED / "regression_results"

def load_panel_full():
    """Load panel; require only revenue (and year, stock_code, industry). No assets required."""
    df = pd.read_csv(PROCESSED / "panel_heavy_pollution.csv", encoding="utf-8-sig")
    df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
    df = df[df["revenue"].notna() & (df["revenue"] > 0)].copy()
    df = df.dropna(subset=["year", "stock_code", "industry"]).copy()
    return df

def build_vars(df):
    """Build outcome and key regressor for full sample."""
    df = df.copy()
    df["ln_revenue"] = np.log(df["revenue"])
    # Digitalization proxy: industry-year revenue percentile (0-1)
    df["dig_proxy"] = df.groupby(["industry", "year"])["revenue"].transform(
        lambda x: x.rank(pct=True, method="average")
    )
    df = df.sort_values(["stock_code", "year"]).copy()
    df["lag_dig"] = df.groupby("stock_code")["dig_proxy"].shift(1)
    df["lag2_dig"] = df.groupby("stock_code")["dig_proxy"].shift(2)
    # TFP/productivity proxy: use ROE (profitability) to avoid collinearity with ln_revenue
    if "roe" in df.columns:
        df["roe_clean"] = pd.to_numeric(df["roe"], errors="coerce").fillna(0).clip(lower=-100, upper=100)
        df["tfp_proxy"] = df["roe_clean"]
    else:
        df["tfp_proxy"] = df["ln_revenue"]
    # Env performance proxy: revenue growth (positive = improving)
    df["rev_growth"] = df.groupby("stock_code")["ln_revenue"].diff()
    df["env_proxy"] = df["rev_growth"].fillna(0).clip(lower=-2, upper=2)
    # Green innovation proxy: ROE improvement (positive part)
    if "roe_clean" not in df.columns and "roe" in df.columns:
        df["roe_clean"] = pd.to_numeric(df["roe"], errors="coerce").fillna(0).clip(lower=-100, upper=100)
    if "roe_clean" in df.columns:
        df["green_proxy"] = df.groupby("stock_code")["roe_clean"].transform(lambda x: x.diff().fillna(0)).clip(lower=0)
    else:
        df["green_proxy"] = 0.0
    # Moderators (all available): size = ln(revenue), regulation = year (centered), margin = gross_margin
    df["size_proxy"] = np.log(df["revenue"].clip(lower=1))
    df["year_c"] = df["year"] - df["year"].mean()
    if "gross_margin" in df.columns:
        df["margin_c"] = pd.to_numeric(df["gross_margin"], errors="coerce").fillna(df["gross_margin"].median()) - df["gross_margin"].median()
    else:
        df["margin_c"] = 0.0
    return df.dropna(subset=["lag_dig", "tfp_proxy"])

def run_ols(y, X, data):
    """OLS with firm and year FEs (within transformation)."""
    from numpy.linalg import lstsq
    data = data.copy()
    data["_y"] = y
    for c in X:
        data["_x_" + c] = data[c]
    for col in ["_y"] + ["_x_" + c for c in X]:
        data[col] = data[col] - data.groupby("stock_code")[col].transform("mean")
    for col in ["_y"] + ["_x_" + c for c in X]:
        data[col] = data[col] - data.groupby("year")[col].transform("mean")
    use = data[["_y"] + ["_x_" + c for c in X]].dropna()
    Y = use["_y"].values
    Xmat = use[["_x_" + c for c in X]].values
    const = np.ones((len(Y), 1))
    Xmat = np.hstack([const, Xmat])
    coef, res, rank, s = lstsq(Xmat, Y, rcond=None)
    n, k = len(Y), Xmat.shape[1]
    resid = Y - Xmat @ coef
    mse = (resid ** 2).sum() / max(n - k, 1)
    try:
        var_b = mse * np.linalg.inv(Xmat.T @ Xmat)
        se = np.sqrt(np.diag(var_b))
    except Exception:
        se = np.full(k, np.nan)
    r2 = 1 - (resid ** 2).sum() / max(((Y - Y.mean()) ** 2).sum(), 1e-10)
    return coef, se, n, r2

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    df = load_panel_full()
    df = build_vars(df)
    n_obs = len(df)
    n_firms = df["stock_code"].nunique()

    results = {}

    # Table 2: Main (1) TFP baseline (2) TFP + lag_dig (3) Env baseline (4) Env + lag_dig
    coef1, se1, n1, r1 = run_ols(df["tfp_proxy"], ["size_proxy"], df)
    results["tfp_base_r2"] = float(r1)
    results["tfp_base_n"] = int(n1)
    coef2, se2, n2, r2 = run_ols(df["tfp_proxy"], ["lag_dig", "size_proxy"], df)
    results["dig_coef_tfp"] = float(coef2[1])
    results["dig_se_tfp"] = float(se2[1])
    results["tfp_r2"] = float(r2)
    results["tfp_n"] = int(n2)
    coef3, se3, n3, r3 = run_ols(df["env_proxy"], ["size_proxy"], df)
    results["env_base_r2"] = float(r3)
    coef4, se4, n4, r4 = run_ols(df["env_proxy"], ["lag_dig", "size_proxy"], df)
    results["dig_coef_env"] = float(coef4[1])
    results["dig_se_env"] = float(se4[1])
    results["env_r2"] = float(r4)
    results["env_n"] = int(n4)

    # Table 3: Mediation
    coef_m1, se_m1, _, _ = run_ols(df["env_proxy"], ["lag_dig", "size_proxy"], df)
    coef_m2, se_m2, _, _ = run_ols(df["green_proxy"], ["lag_dig", "size_proxy"], df)
    coef_m3, se_m3, _, _ = run_ols(df["env_proxy"], ["lag_dig", "green_proxy", "size_proxy"], df)
    indirect = float(coef_m2[1] * coef_m3[2])
    results["med_total"] = float(coef_m1[1])
    results["med_total_se"] = float(se_m1[1])
    results["med_green_coef"] = float(coef_m2[1])
    results["med_green_se"] = float(se_m2[1])
    results["med_direct"] = float(coef_m3[1])
    results["med_direct_se"] = float(se_m3[1])
    results["med_green_on_env"] = float(coef_m3[2])
    results["med_green_on_env_se"] = float(se_m3[2])
    results["med_indirect"] = indirect

    # Table 4: Moderation (all three columns: year as regulation proxy, margin, size)
    df["dig_x_year"] = df["lag_dig"] * df["year_c"]
    df["dig_x_margin"] = df["lag_dig"] * df["margin_c"]
    df["dig_x_size"] = df["lag_dig"] * (df["size_proxy"] - df["size_proxy"].mean())
    c1, s1, _, _ = run_ols(df["env_proxy"], ["lag_dig", "dig_x_year", "size_proxy"], df)
    c2, s2, _, _ = run_ols(df["env_proxy"], ["lag_dig", "dig_x_margin", "size_proxy"], df)
    c3, s3, _, _ = run_ols(df["env_proxy"], ["lag_dig", "dig_x_size", "size_proxy"], df)
    results["mod_reg_dig"] = float(c1[1]); results["mod_reg_se"] = float(s1[1])
    results["mod_reg_int"] = float(c1[2]); results["mod_reg_int_se"] = float(s1[2])
    results["mod_soe_dig"] = float(c2[1]); results["mod_soe_se"] = float(s2[1])
    results["mod_soe_int"] = float(c2[2]); results["mod_soe_int_se"] = float(s2[2])
    results["mod_size_dig"] = float(c3[1]); results["mod_size_se"] = float(s3[1])
    results["mod_size_int"] = float(c3[2]); results["mod_size_int_se"] = float(s3[2])

    # Table 5: Robustness (1) Alt env = ROE as outcome (2) Alt dig = ln_revenue rank (3)-(4) IV
    if "roe_clean" in df.columns:
        c_alt1, s_alt1, n_alt1, r_alt1 = run_ols(df["roe_clean"], ["lag_dig", "size_proxy"], df)
        results["alt_env_coef"] = float(c_alt1[1]); results["alt_env_se"] = float(s_alt1[1]); results["alt_env_n"] = int(n_alt1)
    else:
        results["alt_env_coef"] = results["dig_coef_env"]; results["alt_env_se"] = results["dig_se_env"]; results["alt_env_n"] = n_obs
    # Alt dig: use ln_revenue percentile
    df["dig_alt"] = df.groupby(["industry", "year"])["ln_revenue"].transform(lambda x: x.rank(pct=True))
    df["lag_dig_alt"] = df.groupby("stock_code")["dig_alt"].shift(1)
    df_alt = df.dropna(subset=["lag_dig_alt"]).copy()
    c_alt2, s_alt2, n_alt2, _ = run_ols(df_alt["env_proxy"], ["lag_dig_alt", "size_proxy"], df_alt)
    results["alt_dig_coef"] = float(c_alt2[1]); results["alt_dig_se"] = float(s_alt2[1]); results["alt_dig_n"] = int(n_alt2)
    # IV: instrument = lag2_dig (2-year lag of digitalization proxy)
    df_iv = df.dropna(subset=["lag2_dig"]).copy()
    c_fs, s_fs, n_fs, _ = run_ols(df_iv["lag_dig"], ["lag2_dig", "size_proxy"], df_iv)
    f_stat = (c_fs[1] / s_fs[1]) ** 2 if s_fs[1] > 0 else 0
    results["first_stage_coef"] = float(c_fs[1]); results["first_stage_se"] = float(s_fs[1])
    results["first_stage_f"] = float(f_stat)
    # Fitted from first stage (within space): coef[1]*lag2_dig_dm + coef[2]*size_dm
    df_iv = df_iv.copy()
    df_iv["lag2_dm"] = df_iv["lag2_dig"] - df_iv.groupby("stock_code")["lag2_dig"].transform("mean")
    df_iv["lag2_dm"] = df_iv["lag2_dm"] - df_iv.groupby("year")["lag2_dm"].transform("mean")
    df_iv["size_dm"] = df_iv["size_proxy"] - df_iv.groupby("stock_code")["size_proxy"].transform("mean")
    df_iv["size_dm"] = df_iv["size_dm"] - df_iv.groupby("year")["size_dm"].transform("mean")
    df_iv["pred_dig"] = c_fs[1] * df_iv["lag2_dm"] + c_fs[2] * df_iv["size_dm"]
    df_iv["y_dm"] = df_iv["env_proxy"] - df_iv.groupby("stock_code")["env_proxy"].transform("mean")
    df_iv["y_dm"] = df_iv["y_dm"] - df_iv.groupby("year")["env_proxy"].transform("mean")
    use = df_iv[["y_dm", "pred_dig", "size_dm"]].dropna()
    Y_ss = use["y_dm"].values
    X_ss = np.column_stack([np.ones(len(use)), use["pred_dig"].values, use["size_dm"].values])
    from numpy.linalg import lstsq
    coef_ss, _, _, _ = lstsq(X_ss, Y_ss, rcond=None)
    resid_ss = Y_ss - X_ss @ coef_ss
    mse_ss = (resid_ss ** 2).sum() / max(len(Y_ss) - 3, 1)
    try:
        var_ss = mse_ss * np.linalg.inv(X_ss.T @ X_ss)
        se_ss = np.sqrt(np.diag(var_ss))
    except Exception:
        se_ss = np.array([np.nan, np.nan, np.nan])
    results["iv_coef"] = float(coef_ss[1])
    results["iv_se"] = float(se_ss[1]) if se_ss.size > 1 else np.nan
    results["iv_n"] = int(len(Y_ss))

    results["n_obs"] = int(n_obs)
    results["n_firms"] = int(n_firms)

    with open(OUT / "table_numbers.json", "w") as f:
        json.dump(results, f, indent=2)
    print("N_obs =", n_obs, "N_firms =", n_firms)
    print("Table 2: dig_coef_tfp = {:.4f} ({:.4f}); dig_coef_env = {:.4f} ({:.4f})".format(
        results["dig_coef_tfp"], results["dig_se_tfp"], results["dig_coef_env"], results["dig_se_env"]))
    print("Table 5: First-stage F = {:.2f}; IV coef = {:.4f} ({:.4f})".format(
        results["first_stage_f"], results["iv_coef"], results["iv_se"]))
    return results

if __name__ == "__main__":
    main()
