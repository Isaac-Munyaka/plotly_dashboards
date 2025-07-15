# Plotly Dashboards

This project generates interactive dashboards using Python's Plotly library and exports them as static HTML files.

The data used is also generated from scratch using Pandas and numpy ONLY, and stored in '.csv' and json files.

## Structure

```
README.md
requirements.txt
data/
    kpi_summary.json
    sales_data.csv
outputs/
    dashboard.html
scripts/
    data_gen.py
    viz.py
```

## How It Works

- **Data Generation:**  
  Run [`scripts/data_gen.py`](scripts/data_gen.py) to generate sample sales data and KPIs. Output files are saved in the `data/` folder.

- **Dashboard Visualization:**  
  Run [`scripts/viz.py`](scripts/viz.py) to create a dashboard with sales trends, product breakdowns, regional maps, and scatter plots. The dashboard is saved as `outputs/dashboard.html`.

## Usage

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Generate data:
    ```sh
    python scripts/data_gen.py
    ```

3. Create dashboard:
    ```sh
    python scripts/viz.py
    ```

4. Open `outputs/dashboard.html` in your browser to view the dashboard.

## Files

- [`scripts/data_gen.py`](scripts/data_gen.py): Generates `data/sales_data.csv` and `data/kpi_summary.json`.
- [`scripts/viz.py`](scripts/viz.py): Builds the dashboard from generated data.
- [`outputs/dashboard.html`](outputs/dashboard.html): The final dashboard output.

## Requirements

- Python 3.7+
- pandas
- numpy
- plotly

## License
