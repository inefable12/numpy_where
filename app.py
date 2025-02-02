import streamlit as st
import pandas as pd
import numpy as np

st.title("Aplicación de NUMPY - WHERE")
st.info("np.where(condicion, TRUE, FALSE)")

tabla = st.input_text("Ingresa tu csv:", "https://raw.githubusercontent.com/inefable12/numpy_where/refs/heads/main/midataset.csv")

df = pd.read_csv(tabla)
st.show(df)
