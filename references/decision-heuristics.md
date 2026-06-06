# Decision Heuristics

Use these heuristics only after applying `manual-rules.md`. If a heuristic conflicts with a student-manual rule, follow the manual rule.

## Demand-First Market Choice

Rank regions by a blended score:

`regional_score = current_year_demand * 0.45 + next_year_growth * 0.35 + recent_company_strength * 0.20`

If historical company strength is unavailable, use:

`regional_score = current_year_demand * 0.60 + next_year_growth * 0.40`

Prefer the top 2-3 regions when cash, production, or inventory is constrained. Avoid spreading marketing and retail investment evenly across weak regions.

Adjust demand using the manual's rules before ranking regions:

- Year 11 uses demand chart/CEO forecast directly; 沪深300 starts affecting demand from year 12.
- From year 12 onward, apply 沪深300 direction with a maximum impact around plus/minus 10% when data is available.
- Use competitive intensity as a smaller adjustment, up to about 4%.

## Production And Inventory

Target production should cover expected sales plus required delivery buffer, minus beginning inventory, then adjust for waste:

`gross_production_needed = max(0, expected_sales + delivery_buffer - usable_beginning_inventory) / (1 - waste_rate)`

Avoid:

- Producing far above demand when cash is negative or inventory is already high.
- Leaving high-demand regions understocked while low-demand regions hold idle inventory.
- Increasing style count or quality without enough marketing and distribution to sell the higher-cost product.

Apply manual inventory penalties when planning:

- Unsold private-label inventory loses 5 quality points next year.
- Unsold own-brand inventory loses 10 quality points next year.

## Pricing

Use price as a margin and demand lever:

- If prior-year market share was weak and inventory is high, reduce price or increase sales support before increasing production.
- If demand is strong and inventory sold through, keep price near or above prior-year level while raising marketing/service enough to protect share.
- If quality and brand are below competitors, avoid premium pricing.
- For private label, bid price must cover manufacturing, storage, management, and financing cost. Do not chase volume with negative margin unless scoring clearly rewards volume and cash can absorb it.

## Marketing, Retail, And Service

Advertising, retailer count, retailer support, rebates, delivery time, style count, quality, and brand image work together. Do not optimize one in isolation.

Common patterns:

- High demand + low share: increase advertising and retailer coverage before large factory expansion.
- High inventory + low sales: improve price, rebate, delivery, retailer support, or clearance before increasing production.
- Strong quality + weak sales: distribution/price/marketing is likely the bottleneck.
- Strong sales + weak profit: price, cost, debt, or marketing efficiency is likely the bottleneck.

Use the manual's 11 market-share factors as the checklist for every regional sales plan: price, rebate, variety, quality, advertising, celebrity/brand effect, retailers, retailer support, specialty stores, online sales, and brand loyalty.

Estimate rebate cost with redemption rates from `manual-rules.md`; do not treat the full rebate face value as expected paid cost unless the site's own calculated output says so.

## Factory And Capacity

Expansion and upgrades should be justified by demand that persists into next year.

Prefer capacity expansion or new factories when:

- Demand chart shows multi-year growth.
- Prior-year sales were supply-constrained.
- Cash flow and bond rating can tolerate capex.
- Existing factory utilization is high.

Prefer process, quality, cost, or efficiency upgrades when:

- Capacity exists but margins are weak.
- Waste, quality, labor cost, or management cost is hurting score.
- Cash cannot support large new capacity.

Avoid new capacity near or after total-demand peak unless it replaces expensive or poorly located capacity.

Before recommending new capacity, check the manual capacity restrictions:

- If national capacity plus prior-year inventory exceeds national total demand by 25% or more, existing-factory expansion cannot exceed 1,000 thousand units.
- If national capacity exceeds demand by more than 50%, new factory construction or expansion is disallowed.
- New factories and expansion take one year to implement.

## Finance

Cash stress changes every recommendation.

Warning signs:

- Negative cash.
- Negative profit with large inventory.
- Low interest coverage.
- Poor bond rating.
- High debt service next year.

If cash is stressed:

- Cut low-ROI advertising in weak regions.
- Avoid nonessential factory expansion.
- Avoid dividends and stock buybacks.
- Use financing only to fund profitable demand capture or prevent liquidity failure.
- Reduce production that is not backed by demand.

Avoid automatic short-term borrowing when possible; the manual states that bank-created overdraft borrowing costs 2 percentage points more than normal short-term debt.

Check financing hard limits before recommending equity or buybacks:

- Total shares cannot exceed 50,000 thousand after issuance.
- Shares cannot be issued below 7.5 yuan.
- If year-end stock price is below 7.5 yuan, shares cannot be issued the next year.
- Buybacks cannot reduce shares below 3,000 thousand and cannot make equity negative.
- Dividends cannot be paid if retained earnings are negative or if the dividend would make retained earnings negative.

## Celebrity Bidding

Bid only when the celebrity effect can be monetized through own-brand sales. Avoid celebrity spending when:

- Current year own-brand sales are tiny.
- Cash is negative.
- Product quality, distribution, or delivery is too weak to convert awareness into sales.
- The minimum bid plus bid cost would materially worsen financing risk.

When bidding, prioritize high attractiveness per contract-year cost, not fame alone.

## Stock Investment

Treat stock investment as separate from operating strategy, but still risk-controlled.

- Respect the three-company limit.
- Prefer diversified choices when forecast data is weak.
- Do not use stock choices to compensate for an operating cash crisis unless the simulation explicitly permits and rewards it.
- If no price/change/dividend data is visible, recommend holding rather than guessing.

Do not confuse the site's `股票投资` decision tab with operating-company stock issuance, repurchase, and dividend decisions under `财务管理`; analyze both separately.

## Scoring Feedback Loop

When historical scores are available, diagnose the score before changing numbers:

- Low production score: inspect capacity, waste, cost, labor efficiency, quality.
- Low sales score: inspect regional demand capture, pricing, advertising, retailers, delivery, inventory.
- Low finance score: inspect cash, debt, interest coverage, profit, dividends, capex.
- Low strategy score: inspect overexpansion, underinvestment in growth regions, risk index, bond rating.
- Low celebrity score: inspect contract ROI and bid waste.
- Low stock score: inspect concentration and poor buy/sell timing.

Use the diagnosis to change the next-year plan, and explicitly explain which past weakness each change addresses.

## Manual Rule Gate

Before finalizing a recommendation, run this gate:

- Does private-label bidding meet quality at least 50, style count at least 50, and price at least 2.5 yuan below own-brand average wholesale price?
- Does any online sales assumption stay at or below 20% of regional total sales?
- Does production account for overtime maximum of 20% above normal line capacity?
- Does inventory planning avoid large own-brand carryover because it loses 10 quality points next year?
- Does capacity expansion obey the national capacity versus demand restrictions?
- Does ending cash avoid automatic overdraft borrowing?
- Does the plan support at least one strategic-score advantage rather than being average everywhere?
