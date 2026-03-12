# StyleSense Retail Analytics

End-to-end retail analytics project analyzing 18 months of sales, customer, inventory, and expense data for StyleSense, a clothing retailer selling across physical stores and online.

<img width="1746" height="1083" alt="p l" src="https://github.com/user-attachments/assets/394bfc52-88a9-474c-8426-af3f50bcd872" />


---

## Business Problem

StyleSense faced four unresolved questions:
- Profit margins were unclear after factoring in all operating costs
- Seasonal products were going out of stock during peak demand
- Discounts were being applied freely with no measure of their impact
- Customer segments existed in the CRM but were not being acted on

---

## Project Structure

The analysis follows a four-stage pipeline, with each notebook building on the last.

```
stylesense-retail-analytics/
│
├── data/
│   ├── raw/                        # Original five CSV files
│   └── processed/                  # Cleaned and feature-engineered CSVs
│
├── stylesense_data_cleaning.ipynb
├── stylesense_feature_engineering.ipynb
├── stylesense_exploratory_data_analysis.ipynb
└── stylesense_analytics.ipynb
```

| Stage | Notebook | What it does |
|---|---|---|
| 1 | Data Cleaning | Null handling, type fixes, referential integrity checks, derived columns (`net_profit`, `derived_segment`) |
| 2 | Feature Engineering | Time features, RFM scoring, margin erosion, stock health ratio, fixed vs variable cost classification |
| 3 | EDA | Distributions, trends, cross-dataset relationships across all five datasets |
| 4 | Business Analytics | 8 business questions answered across all four analysis types |

---

## Data

Five datasets covering January 2024 to June 2025.

| Dataset | Rows | Description |
|---|---|---|
| `clothing_sales.csv` | 10,039 | Every transaction: product, channel, price, discount, profit |
| `clothing_customers.csv` | 200 | Customer profiles, CRM segments, purchase history |
| `clothing_expenses.csv` | 1,322 | Operating costs by category |
| `clothing_inventory.csv` | 13,675 | Daily stock levels per product |
| `clothing_products.csv` | 25 | Product catalogue with base price and cost |

---

## Analysis Types Covered

- **Descriptive** — What happened? Revenue, profit, and segment summaries
- **Diagnostic** — Why did it happen? Discount impact, channel gaps, cost structure
- **Predictive** — What will happen next? Seasonal stock depletion forecasting
- **Prescriptive** — What should we do? Targeted recommendations per finding

---

## Key Findings

<img width="1748" height="1083" alt="discount_analysis" src="https://github.com/user-attachments/assets/04578b6a-62b5-4638-990d-26bcbcbeda6c" />

<img width="1746" height="1299" alt="monthly_rev-profit_trend" src="https://github.com/user-attachments/assets/67f17e22-a212-44ff-96ed-6e5ec1b82b54" />
<img width="1619" height="868" alt="near_stockout_days_by_product_month" src="https://github.com/user-attachments/assets/5fe4693d-046c-4270-be18-63d257db5727" />

| Area | Finding |
|---|---|
| Products | Men's and Women's Puffer Jackets generated over $62,000 combined net profit, the top two products by a clear margin |
| Profitability | StyleSense operated at a loss every single month across 18 months |
| Costs | COGS (45.7%) and Payroll (34.2%) account for nearly 80% of all operating costs |
| Discounts | The 0% discount tier generated 4,450 transactions vs 350 at 20%. Higher discounts reduce volume and margin with no benefit |
| Channels | Physical stores outperformed online every single month ($360k vs $310k total revenue) |
| Customers | Champion customers average $5,027 spend. Loyal and Bargain Hunter CRM segments are nearly tied at ~$4,650 |
| Marketing | Average Revenue ROMS = 50.6x. September 2024 was the peak at ~87x |
| Inventory | Men's Swim Shorts spent 15 days near or below the reorder threshold in November, the only critical stockout risk |

---

## Top Recommendations

1. **Cap discounts at 10%** and remove the 20% tier. It generates the fewest transactions at the lowest margin with no measurable benefit.
2. **Protect the Puffer Jacket range.** These two products are the profit engine. Keep them in stock and never deep-discount them.
3. **Win back At Risk customers** with personalised outreach based on their favourite category.
4. **Invest more in the physical channel**, which has outperformed online consistently for 18 months.
5. **Address COGS and Payroll** — these two costs must be reduced or outgrown through revenue growth to reach profitability.

---

## Tools

`Python` `Pandas` `NumPy` `Matplotlib` `Seaborn` `Scikit-learn`

---


---

*Project by [Priscilla Nzula](https://github.com/priscillanzula)*
