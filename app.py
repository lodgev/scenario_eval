import streamlit as st
import pandas as pd
import json
from utils.flatten import flatten_metrics
from charts.bar_chart import render_bar_chart
from charts.radar_chart import render_radar_chart
from charts.heatmap import render_heatmap
from charts.delta_plot import render_delta_plot
from charts.kpi_cards import render_kpi_cards

st.set_page_config(page_title="LOLA Scenario Evaluation Viewer", layout="wide")


if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False
if "uploaded_filename" not in st.session_state:
    st.session_state.uploaded_filename = ""

st.sidebar.header("Upload JSON")
uploaded_file = st.sidebar.file_uploader("Choose a JSON file", type="json")
if uploaded_file and uploaded_file.name != st.session_state.uploaded_filename:
    st.session_state.uploaded_filename = uploaded_file.name
    st.session_state.analysis_done = False

chart_types = st.sidebar.multiselect(
    "Choose chart types",
    ["Bar chart", "Radar chart", "Heatmap", "Delta plot", "KPI cards"],
    default=["Bar chart"]
)

metrics_to_show = st.sidebar.multiselect(
    "Choose metrics",
    ["RMSE", "FCP", "MAE", "MSE"],
    default=["RMSE", "MAE", "MSE", "FCP"]
)

compare_models = st.sidebar.checkbox("Compare with SVD (baseline)", value=True)

st.title("LOLA Scenario Evaluation Viewer")

if uploaded_file:
    raw_data = json.load(uploaded_file)
    data = {
        "output_file": flatten_metrics(raw_data.get("output_file", [])),
        "svd": flatten_metrics(raw_data.get("svd", []))
    }

    st.subheader("General Info")
    st.success(f"File name: `{uploaded_file.name}`")

    st.markdown("---")
    st.subheader("Raw metrics table")
    df_display = pd.DataFrame({
        m: data["output_file"].get(m, [None])[0] if isinstance(data["output_file"].get(m), list)
        else data["output_file"].get(m)
        for m in metrics_to_show
    }, index=["Your Result"])

    if compare_models:
        df_display.loc["SVD Baseline"] = [
            data["svd"].get(m, [None])[0] if isinstance(data["svd"].get(m), list)
            else data["svd"].get(m)
            for m in metrics_to_show
        ]

    st.dataframe(df_display)

    st.markdown("---")
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Start analysis"):
            st.session_state.analysis_done = True

            if "Bar chart" in chart_types:
                render_bar_chart(data, metrics_to_show, compare_models)

            if "Radar chart" in chart_types and compare_models:
                render_radar_chart(data, metrics_to_show, compare_models)

            if "Heatmap" in chart_types:
                render_heatmap(df_display)

            if "Delta plot" in chart_types and compare_models:
                render_delta_plot(data, metrics_to_show)

            if "KPI cards" in chart_types:
                render_kpi_cards(data, metrics_to_show, compare_models)