import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def render_radar_chart(data, metrics_to_show, compare_models):
    fig = plt.figure(figsize=(5, 3))
    ax = fig.add_subplot(111, polar=True)

    labels = metrics_to_show
    main_vals = [data["output_file"].get(m, [0])[0] if isinstance(data["output_file"].get(m), list)
                 else data["output_file"].get(m, 0) for m in labels]
    base_vals = [data["svd"].get(m, [0])[0] if isinstance(data["svd"].get(m), list)
                 else data["svd"].get(m, 0) for m in labels]

    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]
    main_vals += main_vals[:1]
    base_vals += base_vals[:1]

    ax.plot(angles, main_vals, label="Your Result")
    ax.fill(angles, main_vals, alpha=0.1)
    ax.plot(angles, base_vals, label="SVD Baseline")
    ax.fill(angles, base_vals, alpha=0.1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_title("Radar Chart of Metrics")
    ax.legend(loc='upper right')

    st.pyplot(fig, use_container_width=False)
