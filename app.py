import streamlit as st
import pandas as pd
import numpy as np

st.title("Aplicación de NUMPY - WHERE")
st.info("np.where(condicion, TRUE, FALSE)")

st.write("Original")
df = pd.read_csv("https://raw.githubusercontent.com/inefable12/numpy_where/refs/heads/main/midataset.csv")

st.write(df)

st.write("Convirtiendo SI en 1 y NO en 0")
df["Caract2"] = np.where(df["Caract2"] == "SI", 1, 0)

st.write(df)
