# Data Collection Guide

Before collecting browser data, load `manual-rules.md` for simulation-specific constraints. The PDF source is `D:/ican商道杯/学生手册.pdf`; do not reread the PDF unless a rule needs verification or the user provides a different manual.

## Demand Chart

Extract the chart before reading decisions. Record:

- Image URL and visible race row.
- X-axis year range.
- Left y-axis region-demand scale.
- Right y-axis total-demand scale.
- Legend names and line colors.
- Approximate values by year for each line.
- Inflection points where growth accelerates or slows.
- Peak year and post-peak decline, if any.

Approximate values are acceptable when the source is an image. Use ranges when exact reading is not possible.

## Race Metadata

From `查看比赛`, record:

- 比赛名
- 行业号
- 比赛状态
- 公司号
- 公司数(组数)
- 当前年份
- 创建时期
- 公司名称
- 股票代码

Do not click `删除`. Treat `修改` as read-only only if the user asks to inspect it.

## Decision Page

From `比赛决策`, record the filter state:

- 行业号
- 公司号
- 比赛年份

Then collect every tab. For each visible table, capture both labels and values. For editable fields, record the input value and whether the field is readonly or disabled.

Priority fields by tab:

- 年度预算: price, quality, service, brand image, style count, advertising, store count, retailers, rebates, demand forecast, expected share, inventory, required production, utilization.
- 生产运营: production quantity, style count, R&D, premium material rate, quality control budget, process improvement, wages, bonus, expected efficiency, labor need, quality, waste, net production, unit costs.
- 厂区建设: new factory, capacity expansion, permanent closure, upgrade options, next-year capex, risk index, bond rating.
- 产品配送: factory-to-market shipments, beginning inventory, available-for-sale quantity, weighted quality, weighted style count, warehousing and transport cost.
- 自由市场: wholesale price, advertising, rebate, retailers, self-owned stores, retailer support, delivery time, expected wholesale sales, clearance choice, profit analysis.
- 网络市场: online price, style count, delivery mode, available stock, expected online sales, remaining stock, profit analysis.
- 贴牌市场: beginning stock, current production, available quantity, bid quantity, bid price, clearance, expected sales, ending stock, cost-profit analysis.
- 名人签约: candidate list, attractiveness, contract length, current contract status, eligible bid year, bid amount, prior bid statistics, cost impact.
- 财务管理: bonds, short-term loan, new bonds, stock issue, bond redemption, stock buyback, dividends, leverage, interest coverage, risk index, bond rating, cash flow.
- 股票投资: stock code, price, change, dividend, held shares, buy shares, sell shares, asset value, investment limit.

## Historical Results

From `比赛成绩`, collect all available prior years. If dropdowns must be selected, select only filter values and click search. Do not export unless requested.

For each tab, collect:

- 总成绩: rank, score, company comparison.
- 详细得分: category scores and penalties.
- 行业分析: market demand, market share, regional performance.
- 生产分析: production volume, capacity utilization, quality, waste, cost.
- 销售分析: price, marketing, delivery, sales volume, inventory.
- 名人分析: contracts, cost, effect.
- 效率参考: productivity, labor, factory utilization, cost benchmark.
- 战略: major strategic indicators and risk.
- 财务: cash, debt, profit, EPS, ROI, bond rating.
- 股票: stock investment return and portfolio risk.

If the page shows `暂无数据`, report that exact state and continue with available evidence.
