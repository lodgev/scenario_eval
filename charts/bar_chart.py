import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import streamlit as st

def render_bar_chart(data, metrics, compare_models):
    labels = metrics
    your_vals = [data["output_file"].get(m, [None])[0] if isinstance(data["output_file"].get(m), list) else data["output_file"].get(m) for m in labels]
    baseline_vals = [data["svd"].get(m, [None])[0] if isinstance(data["svd"].get(m), list) else data["svd"].get(m) for m in labels] if compare_models else [None] * len(labels)

    x = np.arange(len(labels))
    width = 0.35
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.bar(x - width/2, your_vals, width, label='Your Result')
    if compare_models:
        ax.bar(x + width/2, baseline_vals, width, label='SVD Baseline')
    ax.set_ylabel("Metric Value")
    ax.set_title("Grouped Bar Chart of Selected Metrics")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    # col = st.columns([1, 4, 1])[1]
    # with col:
    #     st.pyplot(fig, use_container_width=False)
    st.pyplot(fig, use_container_width=False)
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
 
