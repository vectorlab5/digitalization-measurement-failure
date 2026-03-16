#!/usr/bin/env python3
"""
Build firm-year panel from raw data, compute descriptives, and export
summary stats for the paper. Uses only data/raw/ (open data).
"""
import sys
from pathlib import Path

import pandas as pd
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW = PROJECT_ROOT / "data" / "raw"
PROCESSED = PROJECT_ROOT / "data" / "processed"
PROCESSED.mkdir(parents=True, exist_ok=True)

def load_yjbb():
    df = pd.read_csv(RAW / "yjbb_all.csv", encoding="utf-8-sig")
    df["stock_code"] = df["股票代码"].astype(str).str.zfill(6)
    return df

def load_heavy_pollution_codes():
    codes = pd.read_csv(RAW / "heavy_pollution_stock_codes.csv", encoding="utf-8-sig")
    return set(codes["stock_code"].astype(str).str.zfill(6))

def load_balance():
    df = pd.read_csv(RAW / "balance_sheet_sina.csv", encoding="utf-8-sig")
    df = df.copy()
    df["stock_code"] = df["stock_code"].astype(str).str.zfill(6)
    df["报告日"] = pd.to_datetime(df["报告日"].astype(str), format="%Y%m%d", errors="coerce")
    df["year"] = df["报告日"].dt.year
    # Year-end only
    df = df[df["报告日"].dt.month == 12].copy()
    return df

def load_income():
    df = pd.read_csv(RAW / "income_statement_sina.csv", encoding="utf-8-sig")
    df["stock_code"] = df["stock_code"].astype(str).str.zfill(6)
    df["报告日"] = pd.to_datetime(df["报告日"].astype(str), format="%Y%m%d", errors="coerce")
    df["year"] = df["报告日"].dt.year
    df = df[df["报告日"].dt.month == 12].copy()
    return df

def build_panel():
    yjbb = load_yjbb()
    codes = load_heavy_pollution_codes()
    # Restrict to heavy-pollution firms
    yjbb = yjbb[yjbb["stock_code"].isin(codes)].copy()
    # Rename for clarity
    yjbb = yjbb.rename(columns={
        "营业总收入-营业总收入": "revenue",
        "净利润-净利润": "net_income",
        "净资产收益率": "roe",
        "销售毛利率": "gross_margin",
        "所处行业": "industry",
        "股票简称": "name",
    })
    # Select and clean numeric cols
    for c in ["revenue", "net_income", "roe", "gross_margin"]:
        if c in yjbb.columns:
            yjbb[c] = pd.to_numeric(yjbb[c], errors="coerce")
    yjbb = yjbb[["stock_code", "year", "name", "industry", "revenue", "net_income", "roe", "gross_margin"]].drop_duplicates(subset=["stock_code", "year"])
    # Merge balance (asset totals, fixed assets)
    bal = load_balance()
    asset_col = "资产总计" if "资产总计" in bal.columns else None
    fa_col = "固定资产净额" if "固定资产净额" in bal.columns else "固定资产净值"
    if asset_col and asset_col in bal.columns:
        bal[asset_col] = pd.to_numeric(bal[asset_col], errors="coerce")
    if fa_col in bal.columns:
        bal[fa_col] = pd.to_numeric(bal[fa_col], errors="coerce")
    bal = bal[["stock_code", "year", asset_col, fa_col]].rename(columns={asset_col: "total_assets", fa_col: "fixed_assets"}) if asset_col else bal[["stock_code", "year", fa_col]].rename(columns={fa_col: "fixed_assets"})
    if "total_assets" not in bal.columns:
        bal["total_assets"] = np.nan
    panel = yjbb.merge(bal, on=["stock_code", "year"], how="left").copy()
    # Merge income (revenue already in yjbb; optional double-check)
    inc = load_income()
    if "营业总收入" in inc.columns:
        inc["营业总收入"] = pd.to_numeric(inc["营业总收入"], errors="coerce")
    inc = inc[["stock_code", "year", "营业总收入"]].rename(columns={"营业总收入": "revenue_income"})
    panel = panel.merge(inc[["stock_code", "year", "revenue_income"]], on=["stock_code", "year"], how="left")
    # Use revenue from yjbb (already have); fill from income if missing
    panel["revenue"] = panel["revenue"].fillna(panel["revenue_income"])
    panel = panel.drop(columns=["revenue_income"], errors="ignore")
    # Size and leverage proxies (we don't have debt in all; use total_assets for size)
    panel["size_log"] = np.log(panel["total_assets"].clip(lower=1))
    panel["roa"] = panel["net_income"] / panel["total_assets"].replace(0, np.nan)
    return panel

def descriptives(panel):
    """Return dict of summary stats and full table (N, Mean, SD, Min, Max) for paper."""
    panel = panel.dropna(subset=["revenue", "total_assets"], how="all")
    n_obs = len(panel)
    n_firms = panel["stock_code"].nunique()
    years = sorted(panel["year"].unique())
    year_range = f"{min(years)}--{max(years)}" if years else "N/A"
    rev = panel["revenue"] / 1e8  # 100M yuan
    assets = panel["total_assets"] / 1e8
    roe = panel["roe"]
    # Winsorize ROE for display (extreme values)
    roe_d = roe.clip(lower=roe.quantile(0.01), upper=roe.quantile(0.99))
    d = {
        "N": n_obs,
        "K": n_firms,
        "year_range": year_range,
        "revenue_mean": rev.mean(),
        "revenue_sd": rev.std(),
        "revenue_min": rev.min(),
        "revenue_max": rev.max(),
        "assets_mean": assets.mean(),
        "assets_sd": assets.std(),
        "assets_min": assets.min(),
        "assets_max": assets.max(),
        "roe_mean": roe_d.mean(),
        "roe_sd": roe_d.std(),
        "roe_min": roe_d.min(),
        "roe_max": roe_d.max(),
    }
    if "size_log" in panel.columns:
        sl = panel["size_log"].dropna()
        d["size_log_mean"] = sl.mean()
        d["size_log_sd"] = sl.std()
        d["size_log_min"] = sl.min()
        d["size_log_max"] = sl.max()
    if "gross_margin" in panel.columns:
        gm = panel["gross_margin"].dropna()
        gm = gm.clip(lower=gm.quantile(0.01), upper=gm.quantile(0.99))
        d["gross_margin_mean"] = gm.mean()
        d["gross_margin_sd"] = gm.std()
        d["gross_margin_min"] = gm.min()
        d["gross_margin_max"] = gm.max()
    return d

def main():
    panel = build_panel()
    panel.to_csv(PROCESSED / "panel_heavy_pollution.csv", index=False, encoding="utf-8-sig")
    print("Saved", PROCESSED / "panel_heavy_pollution.csv", "with", len(panel), "rows")
    d = descriptives(panel)
    for k, v in d.items():
        if isinstance(v, float):
            print(f"  {k}: {v:.4f}")
        else:
            print(f"  {k}: {v}")
    # Export summary for paper (LaTeX table source)
    summary = pd.DataFrame({
        "Variable": ["Firm-year observations", "Unique firms", "Year range", "Revenue (100M yuan), mean", "Revenue (100M yuan), SD", "Total assets (100M yuan), mean", "ROE (%), mean", "ROE (%), SD"],
        "Value": [d["N"], d["K"], d["year_range"], f"{d['revenue_mean']:.2f}", f"{d['revenue_sd']:.2f}", f"{d['assets_mean']:.2f}", f"{d['roe_mean']:.2f}", f"{d['roe_sd']:.2f}"],
    })
    summary.to_csv(PROCESSED / "descriptives_for_paper.csv", index=False, encoding="utf-8-sig")
    # Full descriptives table: N (non-null), Mean, SD, Min, Max (for Table 1)
    panel_for_n = panel.dropna(subset=["revenue", "total_assets"], how="all")
    n_rev = int(panel_for_n["revenue"].notna().sum())
    n_assets = int(panel_for_n["total_assets"].notna().sum())
    n_roe = int(panel_for_n["roe"].notna().sum())
    rows = [
        ("Revenue (100 million yuan)", n_rev, d["revenue_mean"], d["revenue_sd"], d["revenue_min"], d["revenue_max"]),
        ("Total assets (100 million yuan)", n_assets, d["assets_mean"], d["assets_sd"], d["assets_min"], d["assets_max"]),
        ("ROE (%)", n_roe, d["roe_mean"], d["roe_sd"], d["roe_min"], d["roe_max"]),
    ]
    if "size_log_mean" in d:
        n_sl = int(panel_for_n["size_log"].notna().sum())
        rows.append(("Size (ln assets)", n_sl, d["size_log_mean"], d["size_log_sd"], d["size_log_min"], d["size_log_max"]))
    if "gross_margin_mean" in d:
        n_gm = int(panel_for_n["gross_margin"].notna().sum())
        rows.append(("Gross margin (%)", n_gm, d["gross_margin_mean"], d["gross_margin_sd"], d["gross_margin_min"], d["gross_margin_max"]))
    full_desc = pd.DataFrame(rows, columns=["Variable", "N", "Mean", "SD", "Min", "Max"])
    full_desc.to_csv(PROCESSED / "table1_descriptives_full.csv", index=False, encoding="utf-8-sig")
    # By-year means for Figure 2 (descriptive time trend)
    panel_yr = panel.dropna(subset=["revenue"]).copy()
    panel_yr["revenue_100m"] = panel_yr["revenue"] / 1e8
    by_year = panel_yr.groupby("year").agg(
        revenue_mean=("revenue_100m", "mean"),
        revenue_median=("revenue_100m", "median"),
        roe_mean=("roe", "mean"),
        roe_median=("roe", "median"),
        N=("stock_code", "count"),
    ).reset_index()
    by_year.to_csv(PROCESSED / "figure2_by_year.csv", index=False, encoding="utf-8-sig")
    print("Saved", PROCESSED / "figure2_by_year.csv")
    return d

if __name__ == "__main__":
    main()
