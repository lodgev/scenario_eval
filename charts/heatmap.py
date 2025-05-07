import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def render_heatmap(df_display):
    df_heat = df_display.copy().astype(float)
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.heatmap(df_heat, annot=True, fmt=".4f", cmap="coolwarm", ax=ax)
    ax.set_title("Metric Heatmap")

    st.pyplot(fig)
