import streamlit as st
import numpy as np

st.set_page_config(page_title="Filter Math", page_icon="📈")

st.markdown("# Filter Math")
st.sidebar.header("Filter Math")
st.write("Put derrivations here")

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
