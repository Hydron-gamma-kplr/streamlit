import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

st.title("Data Manipulation et Visualisation")

uploaded_file = st.file_uploader("Choisir un fichier")
dataframe = None
if uploaded_file is not None:
    # Lire le fichier
    bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)

    # Convertion en format string basé sur IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #st.write(stringio)

    # Lire le fichier en string:
    string_data = stringio.read()
    #st.write(string_data)

    # transformation fichier csv en dataframe avec lecture
    dataframe = pd.read_csv(uploaded_file)

    if dataframe is not None:
        st.write(dataframe.head())
        st.selectbox()
        st.line_chart(dataframe, x="name", y="age")