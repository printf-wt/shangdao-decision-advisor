#!/usr/bin/env python3
"""Analyze a Shangdao yearly decision snapshot.

Input JSON shape is intentionally simple and flexible:
{
  "current_year": 11,
  "demand": {
    "years": [10, 11, 12],
    "regions": {
      "长三角": [1200, 1000, 1650],
      "环渤海": [700, 800, 950],
      "珠三角": [900, 1000, 1100],
      "中西部": [0, 0, 300],
      "贴牌": [500, 600, 700],
      "全国": [3300, 3200, 4500]
    }
  },
  "metrics": {"cash": -55493, "net_profit": -18841, "roi": -20.63},
  "capacity": {"total": 4000},
  "expected_sales": {"total": 500},
  "online": {"regional_total_sales": {"长三角": 1000}, "online_sales": {"长三角": 150}},
  "private_label": {"quality": 78, "style_count": 100, "bid_price": 34, "own_brand_avg_wholesale_price": 42},
  "finance": {"ending_cash": 100}
}
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def nearest_index(years: list[int], year: int) -> int:
    if year in years:
        return years.index(year)
    return min(range(len(years)), key=lambda i: abs(years[i] - year))


def growth(values: list[float], idx: int) -> float:
    if idx <= 0 or idx >= len(values):
        return 0.0
    return values[idx] - values[idx - 1]


def demand_stage(total: list[float], idx: int) -> str:
    prev_g = growth(total, idx)
    next_g = total[idx + 1] - total[idx] if idx + 1 < len(total) else 0.0
    peak = max(total) if total else 0.0
    current = total[idx] if total else 0.0
    if current >= peak * 0.97 and next_g <= 0:
        return "peak_or_early_decline"
    if prev_g > 0 and next_g > prev_g * 0.8:
        return "fast_growth"
    if prev_g > 0 and next_g >= 0:
        return "growth"
    if abs(next_g) <= max(50.0, current * 0.03):
        return "plateau"
    if next_g < 0:
        return "decline"
    return "unknown"


def analyze(data: dict[str, Any]) -> dict[str, Any]:
    current_year = int(data.get("current_year", 0))
    demand = data.get("demand", {})
    years = [int(y) for y in demand.get("years", [])]
    regions = demand.get("regions", {})
    idx = nearest_index(years, current_year) if years else 0

    total = [float(v) for v in regions.get("全国", [])]
    stage = demand_stage(total, idx) if total else "unknown"

    regional_scores = []
    for name, raw_values in regions.items():
        if name in {"全国"}:
            continue
        values = [float(v) for v in raw_values]
        if not values or idx >= len(values):
            continue
        next_growth = values[idx + 1] - values[idx] if idx + 1 < len(values) else 0.0
        score = values[idx] * 0.6 + next_growth * 0.4
        regional_scores.append({
            "region": name,
            "current_demand": values[idx],
            "next_growth": next_growth,
            "score": round(score, 2),
        })
    regional_scores.sort(key=lambda item: item["score"], reverse=True)

    metrics = data.get("metrics", {})
    cash = float(metrics.get("cash", 0) or 0)
    net_profit = float(metrics.get("net_profit", 0) or 0)
    roi = float(metrics.get("roi", 0) or 0)

    capacity_total = float(data.get("capacity", {}).get("total", 0) or 0)
    expected_sales_total = float(data.get("expected_sales", {}).get("total", 0) or 0)

    warnings = []
    if cash < 0:
        warnings.append("negative_cash")
    if net_profit < 0:
        warnings.append("negative_net_profit")
    if roi < 0:
        warnings.append("negative_roi")
    if capacity_total and expected_sales_total and capacity_total > expected_sales_total * 2.5:
        warnings.append("capacity_may_exceed_visible_expected_sales")
    if capacity_total and expected_sales_total and expected_sales_total > capacity_total * 0.9:
        warnings.append("capacity_may_be_tight")

    manual_checks = []

    online = data.get("online", {})
    regional_total_sales = online.get("regional_total_sales", {})
    online_sales = online.get("online_sales", {})
    for region, online_value in online_sales.items():
        total_value = float(regional_total_sales.get(region, 0) or 0)
        online_value = float(online_value or 0)
        if total_value and online_value > total_value * 0.20:
            warnings.append(f"online_sales_exceeds_20_percent_limit:{region}")
            manual_checks.append({
                "rule": "online_share_limit",
                "region": region,
                "ok": False,
                "detail": f"{online_value} > 20% of {total_value}",
            })

    private_label = data.get("private_label", {})
    if private_label:
        quality = float(private_label.get("quality", 0) or 0)
        style_count = float(private_label.get("style_count", 0) or 0)
        bid_price = float(private_label.get("bid_price", 0) or 0)
        own_brand_avg = float(private_label.get("own_brand_avg_wholesale_price", 0) or 0)
        ok = quality >= 50 and style_count >= 50 and (not own_brand_avg or bid_price <= own_brand_avg - 2.5)
        if not ok:
            warnings.append("private_label_bid_may_violate_manual_rules")
        manual_checks.append({
            "rule": "private_label_bid",
            "ok": ok,
            "detail": {
                "quality": quality,
                "style_count": style_count,
                "bid_price": bid_price,
                "own_brand_avg_wholesale_price": own_brand_avg,
            },
        })

    finance = data.get("finance", {})
    if finance:
        ending_cash = float(finance.get("ending_cash", finance.get("cash", 0)) or 0)
        if ending_cash < 0:
            warnings.append("ending_cash_negative_triggers_expensive_auto_short_term_debt")
        manual_checks.append({
            "rule": "ending_cash_nonnegative",
            "ok": ending_cash >= 0,
            "detail": {"ending_cash": ending_cash},
        })

    return {
        "current_year": current_year,
        "demand_stage": stage,
        "regional_priority": regional_scores,
        "warnings": warnings,
        "manual_checks": manual_checks,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze a Shangdao decision snapshot JSON file.")
    parser.add_argument("snapshot", type=Path, help="Path to snapshot JSON.")
    args = parser.parse_args()

    data = json.loads(args.snapshot.read_text(encoding="utf-8"))
    print(json.dumps(analyze(data), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
