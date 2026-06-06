---
name: shangdao-decision-advisor
description: Analyze and recommend annual decisions for the 商道管理系统 / 商道杯 business simulation. Use when the user asks Codex to help decide a year's strategy, inspect a demand chart, compare prior years' decisions and scores, calculate the best current-year decision, optimize production/marketing/finance/stock/celebrity choices, or produce a decision plan before uploading a strategy. The workflow must use demand-chart analysis first, then previous years' scores and previous decisions when available; for the first playable year, use the demand chart as the only historical reference.
---

# Shangdao Decision Advisor

## Core Rule

Treat every recommendation as an evidence-backed business decision, not a guess. Before proposing current-year decisions:

1. Read `references/manual-rules.md`; treat it as the authoritative decision rulebook.
2. Read the demand chart in detail.
3. Identify the current year, industry number, company number, and available competitors.
4. If this is the first decision year, use only the demand chart, manual rules, and current starting conditions.
5. If prior years exist, read prior-year decisions and prior-year scores/results before calculating the current plan.
6. Never click destructive or finalizing controls such as delete, logout, save, upload strategy, export, or submit unless the user explicitly asks.

## Data Collection Workflow

Use the browser page as the source of truth when it is available.

1. Open `查看比赛`.
2. Record the race name, industry number, company number, current year, company count, and demand-chart image.
3. Open or enlarge the demand chart and extract:
   - Year range on the x-axis.
   - Region demand curves: 长三角, 环渤海, 珠三角, 中西部.
   - 贴牌 curve.
   - 全国 total demand curve.
   - Inflection points, peak years, decline years, and which regions accelerate fastest.
4. Open `比赛决策`.
5. Record the current filters and all decision tabs:
   - 年度预算
   - 生产运营
   - 厂区建设
   - 产品配送
   - 自由市场
   - 网络市场
   - 贴牌市场
   - 名人签约
   - 财务管理
   - 股票投资
6. Open `比赛成绩`.
7. If result filters work, collect historical data for each available prior year:
   - 总成绩 and ranking.
   - 详细得分.
   - 行业分析.
   - 生产分析.
   - 销售分析.
   - 名人分析.
   - 效率参考.
   - 战略.
   - 财务.
   - 股票.
8. If results are unavailable or require unavailable dropdown selection, state that clearly and continue with the available decision pages.

For detailed extraction guidance, read `references/data-collection.md`.

## Analysis Workflow

Read `references/manual-rules.md` and `references/decision-heuristics.md`, then build a year-by-year evidence table before calculating the recommendation.

Required columns:

- `year`
- `demand_stage`: early growth, fast growth, peak, plateau, decline
- `regional_priority`: ranked regions by expected demand and growth
- `own_brand_sales`
- `private_label_sales`
- `revenue`
- `net_profit`
- `cash`
- `eps`
- `roi`
- `capacity_by_factory`
- `inventory_by_region`
- `quality`
- `style_count`
- `marketing_spend`
- `price`
- `service_score`
- `celebrity_contracts`
- `debt_and_financing`
- `stock_investment`

Then compare:

1. Demand trend versus last-year capacity and inventory.
2. Sales results versus price, advertising, retail network, service, and delivery time.
3. Production volume versus demand, waste rate, quality, and labor efficiency.
4. Cash flow versus expansion, marketing, debt service, dividends, and inventory burden.
5. Score components versus the decisions that drove them.
6. Manual-rule constraints versus proposed values.

Use `references/decision-heuristics.md` for decision logic and risk checks.
Use `references/manual-rules.md` for constraints, formulas, scoring rules, and simulation-specific tradeoffs.

## Recommendation Workflow

Produce a decision plan in this order:

1. `Executive Summary`: 3-6 bullets explaining the strategy.
2. `Demand Reading`: what the demand chart implies for this year and next year.
3. `Historical Diagnosis`: what past decisions/results show; omit only for the first year.
4. `Decision Table`: proposed values for each tab and field.
5. `Manual Rule Checks`: price/rebate, quality, capacity, inventory, private-label, finance, and scoring constraints from the student manual.
6. `Expected Effects`: demand captured, production sufficiency, inventory, profit, cash, score impact.
7. `Risks And Watch Items`: cash shortage, overcapacity, unsold inventory, debt rating, weak regions, low quality, low service, celebrity overbid, stock concentration.
8. `Before Upload Checklist`: a concise list of values the user should verify on the website before uploading.

When a field cannot be calculated precisely from visible data, provide a bounded recommendation such as `500-700` and explain the dependency.

Use `references/output-format.md` for the final response structure.

## First-Year Exception

If no prior decisions or scores exist:

- Do not invent history.
- Base the plan on the demand chart, student-manual rules, current starting assets, initial cash, factory capacity, market attractiveness, and first-year scoring priorities.
- Prefer robust first-year positioning over aggressive optimization:
  - Avoid severe cash stress.
  - Avoid capacity that cannot be sold into visible demand.
  - Enter the strongest near-term regions first.
  - Keep quality, style count, service, and delivery credible enough to avoid weak early brand formation.
  - Treat celebrity, debt, and stock decisions conservatively unless the simulation's scoring data shows they are high-impact.

For year 11 specifically, remember the manual rule that 沪深300 affects demand from year 12 onward; do not use it to modify year 11 demand.

## Browser Safety

It is acceptable to click tabs, menus, image previews, pagination, and search/filter controls for read-only analysis. It is acceptable to type into local filter boxes to retrieve data.

Ask for explicit permission before:

- Changing current-year decision input values for what-if testing.
- Clicking `上传策略`, `保存`, `删除`, `退出登录`, `导出`, or any finalizing action.
- Making irreversible account, password, profile, or competition changes.

If the user asks for the final strategy, present the plan and ask for confirmation before uploading it.

## Optional Script

Use `scripts/analyze_snapshot.py` when the collected data has been saved as JSON. The script provides deterministic checks for demand-stage classification, regional priorities, profitability warnings, cash warnings, and capacity-demand balance. It does not replace judgment; use it as a consistency check.
