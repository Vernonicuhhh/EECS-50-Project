import streamlit as st
import numpy as np
from PIL import Image
from skimage import data, img_as_float, transform
from skimage.transform import resize
from skimage.metrics import (
    mean_squared_error,
    peak_signal_noise_ratio,
    structural_similarity,
    normalized_root_mse
)

def calc_metrics(orig, new) -> dict:
    return {
        'mse': mean_squared_error(orig, new),
        'nrmse': normalized_root_mse(orig,new),
        'psnr': peak_signal_noise_ratio(orig, new, data_range=1.0),
        'ssim': structural_similarity(orig, new, data_range=1.0, channel_axis=-1)
    }

st.set_page_config(page_title="Filter Demo", page_icon="🌍")

st.markdown("# Filter Demo")
st.sidebar.header("Filter Demo")

uploaded_img = st.file_uploader("Please Upload an Image")

if uploaded_img is not None:
    img = Image.open(uploaded_img)
    st.image(img, caption="Image")

    signal = img_as_float(np.array(img))


    target_shape = (128, 128)
    signal_aa = resize(
        signal, target_shape, anti_aliasing=True, preserve_range=True
    )
    signal_no_aa = resize(
        signal, target_shape, anti_aliasing=False, preserve_range=True
    )

    img_aa = transform.resize(
        signal_aa, signal.shape, anti_aliasing=False
    )
    img_no_aa = transform.resize(
        signal_no_aa, signal.shape, anti_aliasing=False
    )

    metrics = calc_metrics(signal, img_aa)
    st.json(metrics)
    bad_metrics = calc_metrics(signal, img_no_aa)
    st.json(bad_metrics)

    st.image(signal_aa)
    st.image(signal_no_aa)





