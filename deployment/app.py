import os
import streamlit as st
from src.infer import load_model, predict_with_gradcam

st.set_page_config(page_title="Chest X-Ray Diagnostic Assistant", layout="wide")

st.title("🩺 Chest X-Ray Diagnostic Assistant (Testing Build)")
st.caption("Testing & educational only. Not a medical device.")

LIVE_URL = "https://chest-xray-app-mfawfpdbjakjdr7bsotynh.streamlit.app/"
st.markdown(f"[Live App Link]({LIVE_URL})")

# Model loading (weights from local file or MODEL_URL secret)
with st.spinner("Loading model..."):
    model, device, class_names = load_model()

left, right = st.columns(2)
with left:
    up = st.file_uploader("Upload Chest X-Ray (.png/.jpg)", type=["png", "jpg", "jpeg"])

if up is not None:
    with st.spinner("Inferring + generating Grad-CAM..."):
        result = predict_with_gradcam(up, model, device, class_names)

    with left:
        st.image(result['input_image'], caption="Input X-Ray", use_column_width=True)

    with right:
        st.image(result['overlay'], caption="Grad-CAM Overlay", use_column_width=True)
        st.subheader("Probabilities")
        for cls, p in zip(class_names, result['probs']):
            st.write(f"{cls}: {p:.3f}")
else:
    st.info("Upload a chest X-ray image to see predictions and Grad-CAM.")
