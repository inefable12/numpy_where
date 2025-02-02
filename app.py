import streamlit as st
import pandas as pd
import numpy as np

st.title("Aplicación de NUMPY - WHERE")
st.info("np.where(condicion, TRUE, FALSE)")

df = pd.read_csv("https://raw.githubusercontent.com/inefable12/numpy_where/refs/heads/main/midataset.csv")

st.write(df)
