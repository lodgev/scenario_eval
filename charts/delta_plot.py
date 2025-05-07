import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


def render_delta_plot(data, metrics_to_show):
    diffs = []
    for metric in metrics_to_show:
        your_val = data["output_file"].get(metric, [0])[0] if isinstance(data["output_file"].get(metric), list) else data["output_file"].get(metric, 0)
        base_val = data["svd"].get(metric, [0])[0] if isinstance(data["svd"].get(metric), list) else data["svd"].get(metric, 0)
        diffs.append(your_val - base_val)

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.bar(metrics_to_show, diffs, color=["green" if d > 0 else "red" for d in diffs])
    ax.set_title("Delta (Your Result - Baseline)")
    ax.axhline(0, color='black', linewidth=0.8)
    st.pyplot(fig)
