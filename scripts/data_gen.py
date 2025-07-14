#The Overall goal of this project is to create a dashboard to provide a complete overview of global sales performance, for company x. 
# I need to track the top-level KPIs such as actual sales, variance to forecast, period-over-period change, and order processing time. 
# The dashboard should visualize sales trends over time, compare sales volume by product category, 
# and show the geographic distribution of sales across regions. 
# Additionally, I want to analyze sales variance by product to help diagnose performance drivers and identify areas for improvement.
# Therefore, in this script, I will generate synthetic sales data for the dashboard, using pandas and numpy ONLY.


import pandas as pd
import numpy as np
import os
import json

# --- Ensuring data folder exists 
if not os.path.exists('../data'):
    os.makedirs('../data')

np.random.seed(42)

# --- KPI summary for the top cards ---
kpi_summary = {
    "actuals_this_period(in_$k)": "7165",
    "variance_(to_forecast)": "99.4%",
    "period_over_period": "9.4%",
    "order_processing_time": 30.2
}
with open('../data/kpi_summary.json', 'w') as f:
    json.dump(kpi_summary, f)

# --- Base dimensions & categories ---
months = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar']
product_categories = ['Pasta & Pizza', 'Canned Goods', 'Soup', 'Condiments', 'Coffee & Snacks']
regions = [
    {'region': 'North America', 'lat': 40.7128, 'lon': -74.0060},
    {'region': 'Europe',        'lat': 48.8566, 'lon':   2.3522},
    {'region': 'South America', 'lat':-23.5505, 'lon': -46.6333},
    {'region': 'Asia',          'lat': 35.6895, 'lon': 139.6917},
    {'region': 'Africa',        'lat': -1.2921, 'lon':  36.8219},
    {'region': 'Australia',     'lat':-33.8688, 'lon': 151.2093},
]

# --- Generating a rich transaction-level dataset ---
rows = []
for month in months:
    for prod in product_categories:
        for reg in regions:
            for _ in range(30):  # 30 transactions each
                sales = np.random.randint(10_000, 500_000)
                forecast = int(sales * np.random.uniform(0.97, 1.03))
                variance = (sales - forecast) / forecast * 100
                processing_time = np.random.normal(30, 2)
                rows.append({
                    'Month': month,
                    'Product': prod,
                    'Region': reg['region'],
                    'Latitude': reg['lat'],
                    'Longitude': reg['lon'],
                    'Sales': sales,
                    'Forecast': forecast,
                    'VariancePct': variance,
                    'OrderProcessingTime': processing_time
                })

df_sales = pd.DataFrame(rows)
df_sales.to_csv('../data/sales_data.csv', index=False)

print(" Data generation complete. Files in '../data/':")
print("   - kpi_summary.json")
print("   - sales_data.csv")
