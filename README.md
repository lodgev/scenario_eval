# LOLA Scenario Evaluation Viewer

A lightweight Streamlit dashboard for visualizing and comparing evaluation metrics from LOLA (Learning Oriented Lightweight Auditing) AI scenario results.

---

## Features

- Upload LOLA-generated JSON output
- Visualize key metrics with:
  - Bar charts
  - Radar charts
  - Heatmaps
  - Delta plots
  - Box plots (multi-run distributions)
  - KPI metric cards
- Compare "Your Result" with a baseline model (e.g. `svd`)

---

## Project structure

```bash
lola_dashboard/
├── app.py # Main Streamlit entry point
├── charts/ # Modular chart components
│ ├── bar_chart.py
│ ├── radar_chart.py
│ ├── heatmap.py
│ ├── delta_plot.py
│ ├── box_plot.py
│ └── kpi_cards.py
├── utils/
│ ├── flatten.py # JSON flattening helper
└── requirements.txt
```
---

## Requirements

- Python 3.8+
- Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the app
```bash
streamlit run app.py
```
Open the app in your browser: [http://localhost:8501](http://localhost:8501)


## Input format
Supports LOLA output (after execution Stage1) in the following JSON format:

```json
{
  "output_file": [
    {"RMSE": [0.08]},
    {"FCP": [0.26]},
    {"MAE": [0.03]},
    {"MSE": [0.006]}
  ],
  "svd": [
    {"RMSE": [0.07]},
    {"FCP": [0.31]},
    {"MAE": [0.037]},
    {"MSE": [0.0048]}
  ]
}
```


