import streamlit as st
import numpy as np
import time

st.header("Tester les éléments de Streamlit")

if st.button("OK"):
    st.write("Ok cliqué")

slider = st.slider("Slider", 0,100)
st.write(slider)

st.selectbox("Selectbox", ["Cats", "Dogs", "Tigers", "Apple"],1)

st.multiselect("Multiselect", ["France","Espagne","Brésil","Portugal","Angleterre","Allemagne"])

text_input = st.text_input("Text Input")
st.write(text_input)

number_input = st.number_input("Numeric input",0,100)
st.write(number_input)

text_area = st.text_area("Text area")
st.write(text_area)


date_input = st.date_input("Date")
st.write(date_input)

time_input = st.time_input("Time")
st.write(time_input)