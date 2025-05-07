import streamlit as st

def render_kpi_cards(data, metrics_to_show, compare_models):
    st.subheader("🔎 Key Metric Values")
    cols = st.columns(len(metrics_to_show))
    for i, metric in enumerate(metrics_to_show):
        val = data["output_file"].get(metric, [None])[0] if isinstance(data["output_file"].get(metric), list) else data["output_file"].get(metric, None)
        base = data["svd"].get(metric, [None])[0] if compare_models else None
        delta = f"(∆ {val - base:+.4f})" if base is not None else ""
        with cols[i]:
            st.metric(label=metric, value=f"{val:.4f}", delta=delta if base is not None else None)
