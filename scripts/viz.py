import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import random
import os

# --- Constants ---
FONT = "Arial, sans-serif"
MONTHS = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar']

# --- KPI Values ---
kpi_actuals = 7165
kpi_variance = 99.4
kpi_period = 9.4
kpi_processing = 30.2

# --- Colors ---
DARK_GREEN = "#685b28"   # darker green (or whatever) for bars and scatter
DARK_PINK = "#c94a65"    # slightly darker pink or whatever :)

prod_colors = [DARK_GREEN, DARK_PINK]

# --- Sales Trend Values ---
trend_values = [8000000, 7200000, 7400000, 8000000, 7900000, 7600000, 7500000, 7400000, 7300000, 7200000, 7100000, 7000000]

# --- Sales Trend Data ---
time_fig = go.Figure(
    data=[go.Bar(
        x=MONTHS,
        y=trend_values,
        marker_color=[DARK_GREEN if i%2==0 else DARK_PINK for i in range(len(MONTHS))],
        width=0.6
    )]
)
time_fig.update_layout(
    title=dict(
        text="<b>Sales Trend</b>",
        font=dict(family=FONT, color='#000', size=18),
        x=0.01,
        xanchor='left'
    ),
    xaxis=dict(tickangle=-30),
    yaxis=dict(
        tickvals=[0,4_000_000,8_000_000],
        ticktext=['0','4M','8M'],
        range=[0,8_500_000]
    ),
    plot_bgcolor='white', paper_bgcolor='white',
    margin=dict(t=40,b=40,l=40,r=20),
    font=dict(family=FONT, color='#000'),
    height=400
)

# --- Sales by Product Data ---
product_order = ['Pasta & Pizza', 'Canned Goods', 'Soup', 'Condiments', 'Coffee & Snacks']
product_values = [25000000, 18000000, 12000000, 10000000, 9000000]

product_colors = [DARK_GREEN, DARK_PINK, DARK_PINK, DARK_GREEN, DARK_GREEN]

bar_prod = go.Figure(
    data=[go.Bar(
        x=product_values,
        y=product_order,
        orientation='h',
        marker_color=product_colors
    )],
    layout=go.Layout(
        title=dict(
            text="<b>Sales by Product</b>",
            font=dict(family=FONT, color='#000', size=18),
            x=0.01,
            xanchor='left'
        ),
        xaxis=dict(
            tickvals=[0, 5_000_000, 10_000_000, 15_000_000, 20_000_000, 25_000_000, 30_000_000],
            ticktext=['0','5M','10M','15M','20M','25M','30M'],
            range=[0, 30_000_000],
            showgrid=False
        ),
        yaxis=dict(autorange='reversed'),
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(t=40, b=40, l=40, r=20),
        font=dict(family=FONT, color='#000'),
        showlegend=False,
        height=400
    )
)

# --- Sales by Region Data ---
region_points = []
# West America (California/Seattle area)
for _ in range(120):
    region_points.append({
        'Region': 'North America',
        'Latitude': 37.5 + random.uniform(-2, 2),
        'Longitude': -122.0 + random.uniform(-2, 2),
        'Sales': random.randint(100000, 500000)
    })
# Central America (Texas, Mexico, etc.)
for _ in range(100):
    region_points.append({
        'Region': 'North America',
        'Latitude': 29.0 + random.uniform(-3, 3),
        'Longitude': -98.0 + random.uniform(-5, 5),
        'Sales': random.randint(100000, 500000)
    })
# East America (New York, Florida, etc.)
for _ in range(80):
    region_points.append({
        'Region': 'North America',
        'Latitude': 40.0 + random.uniform(-5, 5),
        'Longitude': -75.0 + random.uniform(-5, 5),
        'Sales': random.randint(100000, 500000)
    })
# Northern Europe (UK, Scandinavia)
for _ in range(80):
    region_points.append({
        'Region': 'Europe',
        'Latitude': 55.0 + random.uniform(-2, 2),
        'Longitude': 10.0 + random.uniform(-10, 10),
        'Sales': random.randint(100000, 500000)
    })
#  bubbles in other regions
region_config = [
    {'region': 'North America', 'lat': 40.7128, 'lon': -74.0060, 'count': 40, 'spread': 1.2},
    {'region': 'Europe', 'lat': 48.8566, 'lon': 2.3522, 'count': 40, 'spread': 1.2},
    {'region': 'South America', 'lat': -23.5505, 'lon': -46.6333, 'count': 20, 'spread': 1.5},
    {'region': 'Asia', 'lat': 35.6895, 'lon': 139.6917, 'count': 20, 'spread': 1.5},
    {'region': 'Africa', 'lat': -1.2921, 'lon': 36.8219, 'count': 20, 'spread': 1.5},
    {'region': 'Australia', 'lat': -33.8688, 'lon': 151.2093, 'count': 20, 'spread': 1.5}
]
for reg in region_config:
    for _ in range(reg['count']):
        region_points.append({
            'Region': reg['region'],
            'Latitude': reg['lat'] + random.uniform(-reg['spread'], reg['spread']),
            'Longitude': reg['lon'] + random.uniform(-reg['spread'], reg['spread']),
            'Sales': random.randint(100000, 500000)
        })
region_df = pd.DataFrame(region_points)

map_fig = px.scatter_geo(
    region_df,
    lat='Latitude', lon='Longitude', size='Sales', hover_name='Region',
    projection='natural earth', color_discrete_sequence=['#1f77b4'], size_max=10, opacity=0.7
)
map_fig.update_layout(
    title=dict(
        text="<b>Sales by Region</b>",
        font=dict(family=FONT, color='#000', size=18),
        x=0.01,
        xanchor='left'
    ),
    geo=dict(showland=True, landcolor='lightgray'),
    margin=dict(t=40,b=20,l=20,r=20),
    font=dict(family=FONT, color='#000'),
    height=400
)

# --- Scatter Data ---
scatter_points = []
for prod, color in zip(product_order, product_colors):
    for _ in range(20):
        sales = np.random.uniform(0, 500)
        variance = np.random.normal(loc=100, scale=8)
        scatter_points.append({'Product': prod, 'Sales': sales, 'VariancePct': variance, 'Color': color})
sc_df = pd.DataFrame(scatter_points)

scatter_fig = go.Figure()
for prod, color in zip(product_order, product_colors):
    df_prod = sc_df[sc_df['Product'] == prod]
    scatter_fig.add_trace(go.Scatter(
        x=df_prod['Sales'],
        y=df_prod['VariancePct'],
        mode='markers',
        marker=dict(size=12, color=color),
        name=prod
    ))
scatter_fig.add_shape(
    type='line',
    x0=-100, x1=500, y0=100, y1=100,
    line=dict(color='gray', width=2)
)
scatter_fig.add_shape(
    type='line',
    x0=100, x1=100, y0=80, y1=120,
    line=dict(color='gray', width=2)
)
scatter_fig.add_annotation(
    x=100,
    y=125,
    text="$K(95.44)",
    showarrow=False,
    font=dict(color='gray', size=13),
    xanchor='center',
    yanchor='bottom'
)
scatter_fig.update_layout(
    title=dict(
        text="<b>Sales / Variance Scatter by Product</b>",
        font=dict(family=FONT, color='#000', size=18),
        x=0.01,
        xanchor='left'
    ),
    xaxis=dict(
        tickvals=[-100, 0, 100, 200, 300, 400, 500],
        ticktext=['-100','0','100','200','300','400','500'],
        range=[-100, 500],
        showgrid=False
    ),
    yaxis=dict(
        tickvals=[80,100,120],
        ticktext=['80%','100%','120%'],
        range=[80,125],
        zeroline=True,
        zerolinecolor='black',
        showgrid=False
    ),
    plot_bgcolor='white', paper_bgcolor='white',
    margin=dict(t=40,b=40,l=40,r=20),
    font=dict(family=FONT, color='#000'),
    legend=dict(bordercolor='black', borderwidth=1),
    height=400
)

# --- KPI Card HTML Helper ---
def kpi_card_html(title, value):
    value_color = "#26c6da" if "%" in str(value) or "PERIOD" in title or "TIME" in title else "#26c6da"
    return f"""
    <div style='background:#f9f9f9; padding:20px; border-radius:8px; box-shadow:0 2px 4px rgba(0,0,0,0.1); text-align:center; flex:1; margin:5px; display:inline-block;'>
        <h4 style='font-weight:bold; color:#000; margin-bottom:5px;'><b>{title}</b></h4>
        <h2 style='margin-top:0; color:{value_color}; font-size:32px; font-weight:bold;'>{value}</h2>
    </div>
    """

# --- Static HTML Export ---
if __name__ == '__main__':
    html = []
    html.append("<html><head><title>Dashboard</title></head><body style='background-color:#f8f9fa; font-family:Arial;'>")
    html.append("<h1 style='color:#000; font-weight:bold; padding-left:30px;'>Dashboard</h1>")

    # KPI row
    kpis = [
        ("ACTUALS: THIS PERIOD (in $K)", f"${int(kpi_actuals):,}"),
        ("VARIANCE (TO FORECAST)",        f"{kpi_variance:.1f}%"),
        ("PERIOD OVER PERIOD",            f"{kpi_period:.1f}%"),
        ("ORDER PROCESSING TIME",         f"{kpi_processing:.1f}")
    ]
    html.append("<div style='display:flex; justify-content:space-between; flex-wrap:wrap; padding:0 30px 30px;'>")
    for title, val in kpis:
        html.append(kpi_card_html(title, val))
    html.append("</div>")

    # Charts container with responsive flex 
    html.append("<div style='display:flex; flex-wrap:wrap; justify-content:space-between; gap:40px; padding:0 30px;'>")
    # Sales Trend and Product
    for t, fig in [("Sales Trend", time_fig), ("Sales by Product", bar_prod)]:
        fig_html = pio.to_html(fig, full_html=False, include_plotlyjs='cdn')
        html.append(f"<div style='flex:1; min-width:600px; min-height:440px; background:white; border-radius:8px; padding:20px; margin-bottom:30px; box-shadow:0 2px 4px rgba(0,0,0,0.05);'>" +
                    fig_html + "</div>")
    html.append("</div>")

    html.append("<div style='display:flex; flex-wrap:wrap; justify-content:space-between; gap:40px; padding:0 30px 30px;'>")
    # Region and Scatter
    for t, fig in [("Sales by Region", map_fig), ("Sales / Variance Scatter by Product", scatter_fig)]:
        fig_html = pio.to_html(fig, full_html=False, include_plotlyjs='cdn')
        html.append(f"<div style='flex:1; min-width:600px; min-height:440px; background:white; border-radius:8px; padding:20px; margin-bottom:30px; box-shadow:0 2px 4px rgba(0,0,0,0.05);'>" +
                    fig_html + "</div>")
    html.append("</div>")

    html.append("</body></html>")

    # Ensuring outputs directory exists
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'outputs'))
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, 'dashboard.html'), 'w', encoding='utf-8') as f:
        f.write(''.join(html))
    print(f"dashboard.html saved to {output_dir}/")