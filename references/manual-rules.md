# Student Manual Decision Rules

Use these rules from `D:/ican商道杯/学生手册.pdf` when calculating decisions. Treat them as higher priority than generic business heuristics.

## Scoring And Objectives

The board evaluates performance with six measures:

- Sales revenue growth.
- EPS growth.
- ROI.
- Market capitalization: stock price times shares outstanding.
- Bond rating.
- Strategic score.

Relative scoring matters. For most score categories, the best company receives 100 and others score by percentage versus the best. EPS or ROI below zero scores 0. Bond rating score is:

- AAA = 100
- AA = 90
- A = 80
- BBB = 60
- BB = 40
- B = 20
- C = 0

Strategic score rewards distinction, not generic balance. It can come from strong market share, sustainable competitive advantages, and high product reputation.

## Demand Forecasts

For early years, use the demand chart and the CEO annual budget meeting. The manual states that year 11 demand uses year 11 as the stock-index baseline; 沪深300 affects demand from year 12 onward, not the current year 11 decision.

Demand forecast adjustments:

- 沪深300 can move demand in the same direction, with maximum impact around plus/minus 10%.
- Industry competitive intensity can create up to about 4% demand deviation.
- Later industry reports include five-year demand expectations; after the first decision year, read them first.
- Actual demand can deviate from forecasts by roughly 10-15% when stock-index movement or industry competition is unusually strong or weak.

## Market Share Factors

Market share is driven by 11 factors:

1. Wholesale price.
2. Consumer rebate.
3. Product variety.
4. Product quality.
5. Advertising.
6. Celebrity endorsement and brand effect.
7. Number of independent retailers.
8. Support services provided to retailers.
9. Number of company-owned specialty stores.
10. Online sales effectiveness.
11. Customer brand loyalty.

Wholesale price is one of the most important variables. A price above regional industry average hurts share; price cuts can raise share but cannot work alone without quality, distribution, and service.

Consumer rebates range from 1 to 10 yuan per unit. Approximate redemption rates:

- 1 yuan: 15%
- 2 yuan: 20%
- 3 yuan: 25%
- Continue by roughly 5 percentage points per yuan.
- 10 yuan: 60%

Use rebate cost as expected redemption, not full face value, unless the simulation page calculates it differently.

Product variety choices are 50, 100, 150, 200, or 250 styles. More variety improves market appeal but increases setup cost and defect risk; fewer styles can support a focused strategy.

Network sales:

- Online sales were about 10% of total sales in year 10.
- Year 11 and 12 are expected around 11% and 12%.
- Online sales share is the same proportion across the four regions.
- Online sales cannot exceed 20% of a region's total sales.

Brand loyalty tends to strengthen for brands with high market share and strong price/quality/service performance.

## Quality And Materials

Raw materials have two levels:

- Ordinary material baseline cost: 9 yuan per unit.
- Premium material baseline cost: 15 yuan per unit.
- Premium material improves quality/function and costs two-thirds more than ordinary material.

Material market price responds to industry capacity utilization:

- If national production is below 90% of total capacity, raw-material price falls 1% for each percentage point below 90%.
- If production exceeds 100% of total capacity, raw-material price rises 1% for each percentage point above 100%.
- If national premium-material usage exceeds 25%, each percentage point above 25% raises premium-material price by 0.5% and lowers ordinary-material price by 0.5%.

Quality is affected by:

- Premium material ratio.
- Style/design R&D investment.
- Quality-control spending.
- Production process and labor execution.

Inventory quality penalty:

- Unsold private-label inventory loses 5 quality points next year.
- Unsold own-brand inventory loses 10 quality points next year.

## Production And Labor

Assembly lines can produce up to 20% overtime above normal capacity.

Regional annual labor cost benchmarks:

- 长三角: about 20,000 yuan per worker or more.
- 环渤海: about 15,000 yuan per worker.
- 珠三角: about 15,000 yuan per worker.
- 中西部: about 10,000 yuan per worker.

Production capacity is constrained by the smaller of factory capacity and workers times productivity. Overtime pay is 1.5 times standard wage, plus piecework bonus on qualified overtime production.

The purpose of pay and bonus decisions is to reduce labor cost per unit, not simply maximize output. Hiring can improve productivity by up to about 2%; layoffs can hurt morale and reduce productivity by up to about 10%.

More styles increase setup cost and defect risk. This can be offset by more style/features R&D or higher premium-material ratio.

## Factory And Capacity

New factories, expansion, and automation projects require one year to implement. Each region can have at most one factory.

Capacity expansion limits:

- If national capacity plus prior-year inventory exceeds national total demand by 25% or more, expansion of any existing factory cannot exceed 1,000 thousand units.
- If national capacity exceeds demand by more than 50%, new factories or capacity expansion are not allowed.

Factory location is strategic:

- 珠三角 factory can lower sales/transport cost for 珠三角.
- 中西部 factory can lower local distribution cost and has cheap labor that may lower total production cost.
- A large factory in one region may outperform small factories in all regions due to scale.

## Logistics And Inventory

Distribution decisions must balance stockout risk against inventory cost and quality decay.

If distribution centers lack enough stock:

- Sales fall.
- Delivery time can worsen.
- Market share and service perception suffer.

If inventory is too high:

- Warehousing cost rises.
- Next-year quality falls because old styles lose appeal.
- Own-brand inventory penalty is worse than private-label inventory penalty.

Ship more than the bare minimum when defect-rate uncertainty could create stockouts, but avoid sending large volumes into weak demand regions.

## Private Label Market

Private-label sales are in the 长三角 channel. Current common bid requirements:

- Quality at least 50.
- Style count at least 50.
- Bid price must be at least 2.5 yuan lower than the company's own-brand average wholesale price.

Winning logic:

- Lowest bid price wins first.
- If the lowest bidder cannot satisfy total demand, remaining demand is awarded by ascending bid price.
- If bid price ties, higher quality wins.
- If bid price and quality tie, higher style count wins.

Private-label bid decisions require:

- Bid quantity, in thousand units.
- Bid price, to the cent.

Unsold private-label products remain in inventory and can be bid next year, but lose 5 quality points.

## Finance Rules

Cash must remain nonnegative at year end. If management cannot keep ending cash at or above 0, the bank automatically issues short-term debt to cover the deficit. This automatic borrowing costs 2 percentage points more than normal short-term borrowing, so avoid it when possible.

Stock issuance limits:

- Total shares outstanding cannot exceed 50,000 thousand shares.
- New shares cannot be issued below 7.5 yuan per share.
- If year-end market price is below 7.5 yuan, new shares cannot be issued the next year.

Stock repurchase limits:

- Total shares cannot fall below 3,000 thousand shares.
- Repurchase price rises as more shares are repurchased.
- Repurchase cannot make equity negative.

Bond redemption:

- Bonds may be redeemed early in whole or part.
- Early redemption carries a 2% penalty, included in interest expense.
- Redeeming high-rate debt can be rational when new rates are low enough to offset the penalty.

Dividends:

- Dividends affect stock price.
- Dividends above current-year profit reduce retained earnings.
- Dividends are prohibited if retained earnings are negative or if paying the dividend would make them negative.

Stock price is influenced by revenue growth, expected EPS trend, ROI, expected ROI trend, EPS growth trend, dividend growth trend, dividend payout above 100%, bond rating, and strategic risk. EPS growth, ROI, and three-year EPS/ROI trends are especially important.

## Strategic Score Rules

Strategic score rewards recognizable advantages. Requirements and scoring logic include:

- Product breadth/focus: weighted average style count must be above or below regional industry average by about 20%; each 10% difference gives points, capped around 10.
- High quality: regional quality must exceed industry average by about 20 points; each 10-point difference gives points, capped around 10.
- Good service: regional service score must exceed industry average by about 20 points; each 10-point difference gives points, capped around 10.
- Brand image: regional brand image must exceed industry average by about 20 points; each 10-point difference gives points, capped around 10.
- Low cost: own-brand regional average operating cost must be at least 10% below average; private label must be at least 2% below average. Each 2% cost advantage gives points.
- Market share leader: own-brand, online, or private-label sales above regional average by 15% qualifies; each 5% above average gives points.
- High-value product: value = (quality + style count) / price. Own-brand or online value at least 10% above average qualifies; each 3% above average gives points. Private label has no value score because price is the only competitive factor.

Strategic score in a region generally requires at least 100 thousand units of sales in that region.
