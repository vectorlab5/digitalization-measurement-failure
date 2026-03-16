"""
Data loading and panel construction.

This module centralizes all logic for:

- reading raw open-data CSVs downloaded via ``scripts/download_data.py``,
- constructing the firm–year panel used in the empirical illustration, and
-,computing descriptive statistics that feed the paper's tables and figures.

The functions here are imported by the thin CLI wrapper in
``scripts/analyze_data.py`` so that analysis can be reused from notebooks
or other modules.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

import numpy as np
import pandas as pd

from .paths import raw_data_dir, processed_data_dir


RAW = raw_data_dir()
PROCESSED = processed_data_dir()


def load_yjbb() -> pd.DataFrame:
    """Load annual performance report (业绩报表) for all firms and years."""
    df = pd.read_csv(RAW / "yjbb_all.csv", encoding="utf-8-sig")
    df["stock_code"] = df["股票代码"].astype(str).str.zfill(6)
    return df


def load_heavy_pollution_codes() -> set[str]:
    """Load the list of heavy-pollution firm codes."""
    codes = pd.read_csv(RAW / "heavy_pollution_stock_codes.csv", encoding="utf-8-sig")
    return set(codes["stock_code"].astype(str).str.zfill(6))


def load_balance() -> pd.DataFrame:
    """Load and pre-process balance sheet data from Sina."""
    df = pd.read_csv(RAW / "balance_sheet_sina.csv", encoding="utf-8-sig")
    df = df.copy()
    df["stock_code"] = df["stock_code"].astype(str).str.zfill(6)
    df["报告日"] = pd.to_datetime(df["报告日"].astype(str), format="%Y%m%d", errors="coerce")
    df["year"] = df["报告日"].dt.year
    # Only keep year-end observations
    df = df[df["报告日"].dt.month == 12].copy()
    return df


def load_income() -> pd.DataFrame:
    """Load and pre-process income statement data from Sina."""
    df = pd.read_csv(RAW / "income_statement_sina.csv", encoding="utf-8-sig")
    df["stock_code"] = df["stock_code"].astype(str).str.zfill(6)
    df["报告日"] = pd.to_datetime(df["报告日"].astype(str), format="%Y%m%d", errors="coerce")
    df["year"] = df["报告日"].dt.year
    df = df[df["报告日"].dt.month == 12].copy()
    return df


def build_panel() -> pd.DataFrame:
    """
    Construct the main firm–year panel used in the empirical illustration.

    The panel includes revenue, profitability, industry, assets and simple
    size/ROA proxies for heavily polluting firms.
    """
    yjbb = load_yjbb()
    codes = load_heavy_pollution_codes()
    # Restrict to heavy-pollution firms
    yjbb = yjbb[yjbb["stock_code"].isin(codes)].copy()
    # Rename for clarity
    yjbb = yjbb.rename(
        columns={
            "营业总收入-营业总收入": "revenue",
            "净利润-净利润": "net_income",
            "净资产收益率": "roe",
            "销售毛利率": "gross_margin",
            "所处行业": "industry",
            "股票简称": "name",
        }
    )
    # Select and clean numeric columns
    for c in ["revenue", "net_income", "roe", "gross_margin"]:
        if c in yjbb.columns:
            yjbb[c] = pd.to_numeric(yjbb[c], errors="coerce")
    yjbb = yjbb[
        [
            "stock_code",
            "year",
            "name",
            "industry",
            "revenue",
            "net_income",
            "roe",
            "gross_margin",
        ]
    ].drop_duplicates(subset=["stock_code", "year"])

    # Merge balance sheet (asset totals, fixed assets)
    bal = load_balance()
    asset_col = "资产总计" if "资产总计" in bal.columns else None
    fa_col = "固定资产净额" if "固定资产净额" in bal.columns else "固定资产净值"
    if asset_col and asset_col in bal.columns:
        bal[asset_col] = pd.to_numeric(bal[asset_col], errors="coerce")
    if fa_col in bal.columns:
        bal[fa_col] = pd.to_numeric(bal[fa_col], errors="coerce")
    if asset_col:
        bal = bal[["stock_code", "year", asset_col, fa_col]].rename(
            columns={asset_col: "total_assets", fa_col: "fixed_assets"}
        )
    else:
        bal = bal[["stock_code", "year", fa_col]].rename(columns={fa_col: "fixed_assets"})
    if "total_assets" not in bal.columns:
        bal["total_assets"] = np.nan
    panel = yjbb.merge(bal, on=["stock_code", "year"], how="left").copy()

    # Merge income (alternative revenue measure, for diagnostics)
    inc = load_income()
    if "营业总收入" in inc.columns:
        inc["营业总收入"] = pd.to_numeric(inc["营业总收入"], errors="coerce")
    inc = inc[["stock_code", "year", "营业总收入"]].rename(columns={"营业总收入": "revenue_income"})
    panel = panel.merge(inc[["stock_code", "year", "revenue_income"]], on=["stock_code", "year"], how="left")
    # Fill missing revenue from income statement where needed
    panel["revenue"] = panel["revenue"].fillna(panel["revenue_income"])
    panel = panel.drop(columns=["revenue_income"], errors="ignore")

    # Simple size and profitability proxies
    panel["size_log"] = np.log(panel["total_assets"].clip(lower=1))
    panel["roa"] = panel["net_income"] / panel["total_assets"].replace(0, np.nan)
    return panel


@dataclass
class Descriptives:
    """Container for key descriptive statistics used in the paper."""

    N: int
    K: int
    year_range: str
    revenue_stats: Tuple[float, float, float, float]
    assets_stats: Tuple[float, float, float, float]
    roe_stats: Tuple[float, float, float, float]
    size_log_stats: Tuple[float, float, float, float] | None = None
    gross_margin_stats: Tuple[float, float, float, float] | None = None


def compute_descriptives(panel: pd.DataFrame) -> Descriptives:
    """Compute high-level descriptives for the panel."""
    panel = panel.dropna(subset=["revenue", "total_assets"], how="all")
    n_obs = len(panel)
    n_firms = panel["stock_code"].nunique()
    years = sorted(panel["year"].unique())
    year_range = f"{min(years)}--{max(years)}" if years else "N/A"

    rev = panel["revenue"] / 1e8  # 100M yuan
    assets = panel["total_assets"] / 1e8
    roe = panel["roe"]
    roe_d = roe.clip(lower=roe.quantile(0.01), upper=roe.quantile(0.99))

    size_stats = None
    if "size_log" in panel.columns:
        sl = panel["size_log"].dropna()
        size_stats = (sl.mean(), sl.std(), sl.min(), sl.max())

    gm_stats = None
    if "gross_margin" in panel.columns:
        gm = panel["gross_margin"].dropna()
        gm = gm.clip(lower=gm.quantile(0.01), upper=gm.quantile(0.99))
        gm_stats = (gm.mean(), gm.std(), gm.min(), gm.max())

    return Descriptives(
        N=n_obs,
        K=n_firms,
        year_range=year_range,
        revenue_stats=(rev.mean(), rev.std(), rev.min(), rev.max()),
        assets_stats=(assets.mean(), assets.std(), assets.min(), assets.max()),
        roe_stats=(roe_d.mean(), roe_d.std(), roe_d.min(), roe_d.max()),
        size_log_stats=size_stats,
        gross_margin_stats=gm_stats,
    )


def export_descriptives_outputs(panel: pd.DataFrame, stats: Descriptives) -> None:
    """
    Write CSV artefacts that the paper uses for tables and figures.

    - ``panel_heavy_pollution.csv``: main panel.
    - ``descriptives_for_paper.csv``: short summary table.
    - ``table1_descriptives_full.csv``: N, Mean, SD, Min, Max for key variables.
    - ``figure2_by_year.csv``: by-year descriptive trends.
    """
    PROCESSED.mkdir(parents=True, exist_ok=True)
    panel.to_csv(PROCESSED / "panel_heavy_pollution.csv", index=False, encoding="utf-8-sig")

    # Short summary for the text
    d: Dict[str, float | int | str] = {
        "N": stats.N,
        "K": stats.K,
        "year_range": stats.year_range,
        "revenue_mean": stats.revenue_stats[0],
        "revenue_sd": stats.revenue_stats[1],
        "assets_mean": stats.assets_stats[0],
        "roe_mean": stats.roe_stats[0],
        "roe_sd": stats.roe_stats[1],
    }
    summary = pd.DataFrame(
        {
            "Variable": [
                "Firm-year observations",
                "Unique firms",
                "Year range",
                "Revenue (100M yuan), mean",
                "Revenue (100M yuan), SD",
                "Total assets (100M yuan), mean",
                "ROE (%), mean",
                "ROE (%), SD",
            ],
            "Value": [
                d["N"],
                d["K"],
                d["year_range"],
                f"{d['revenue_mean']:.2f}",
                f"{d['revenue_sd']:.2f}",
                f"{d['assets_mean']:.2f}",
                f"{d['roe_mean']:.2f}",
                f"{d['roe_sd']:.2f}",
            ],
        }
    )
    summary.to_csv(PROCESSED / "descriptives_for_paper.csv", index=False, encoding="utf-8-sig")

    # Full descriptives table
    panel_for_n = panel.dropna(subset=["revenue", "total_assets"], how="all")
    n_rev = int(panel_for_n["revenue"].notna().sum())
    n_assets = int(panel_for_n["total_assets"].notna().sum())
    n_roe = int(panel_for_n["roe"].notna().sum())

    rows = [
        ("Revenue (100 million yuan)", n_rev, *stats.revenue_stats),
        ("Total assets (100 million yuan)", n_assets, *stats.assets_stats),
        ("ROE (%)", n_roe, *stats.roe_stats),
    ]
    if stats.size_log_stats is not None:
        n_sl = int(panel_for_n["size_log"].notna().sum())
        rows.append(("Size (ln assets)", n_sl, *stats.size_log_stats))
    if stats.gross_margin_stats is not None:
        n_gm = int(panel_for_n["gross_margin"].notna().sum())
        rows.append(("Gross margin (%)", n_gm, *stats.gross_margin_stats))

    full_desc = pd.DataFrame(rows, columns=["Variable", "N", "Mean", "SD", "Min", "Max"])
    full_desc.to_csv(PROCESSED / "table1_descriptives_full.csv", index=False, encoding="utf-8-sig")

    # By-year means for descriptive time-trend figure
    panel_yr = panel.dropna(subset=["revenue"]).copy()
    panel_yr["revenue_100m"] = panel_yr["revenue"] / 1e8
    by_year = (
        panel_yr.groupby("year")
        .agg(
            revenue_mean=("revenue_100m", "mean"),
            revenue_median=("revenue_100m", "median"),
            roe_mean=("roe", "mean"),
            roe_median=("roe", "median"),
            N=("stock_code", "count"),
        )
        .reset_index()
    )
    by_year.to_csv(PROCESSED / "figure2_by_year.csv", index=False, encoding="utf-8-sig")

