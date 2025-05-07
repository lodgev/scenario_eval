from PIL import Image
import streamlit as st

def save_fig_to_buffer(fig, label):
    from io import BytesIO
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    st.session_state.image_buffers.append((label, buf))
