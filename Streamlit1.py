import streamlit as st
import numpy as np
import time

st.title("Mon application Streamlit avec Markdown")
st.subheader("Exemple d'utilisation du Markdown")
st.markdown("Voici un **texte en gras** et un *Test*.")
st.markdown("""
Voici une liste à puces :
- élément 1
- élément 2
- élément 3
""")

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random(1,1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)