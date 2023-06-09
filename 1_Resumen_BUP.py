import streamlit as st
import pandas as pd
import numpy  as np

st.header('Resumen BraveUp!')

col1, col2, col3 = st.columns(3)
col1.metric("N° encuestas"  , "70 °F", "1.2 2022")
col2.metric("N° colegios"   , "9 mph", "-8%")
col3.metric("N° estudiantes", "86%", "4%")

st.divider()

col1,col2 = st.columns(2)
chart_data1 = pd.DataFrame( np.random.randn(12, 2), columns=['2022', '2023'])
col1.subheader('Acumu encuestas')
col1.line_chart(chart_data1)

chart_data2 = pd.DataFrame( np.random.randn(12, 2), columns=['2022', '2023'])
col2.subheader('Acumulado respuestas')
col2.line_chart(chart_data2)

st.divider()

col1,col2,col3,col4,col5 = st.columns(5)
col1.metric("Aceptados", '50%', '40% 2022')
col2.metric("Aceptados", '50%', '40% 2022')
col3.metric("Aceptados", '50%', '40% 2022')
col4.metric("Aceptados", '50%', '40% 2022')
col5.metric("Aceptados", '50%', '40% 2022')
import time
with st.sidebar:
  st.write("This code wilebar.")

  with st.spinner("Loading..."):
    time.sleep(1)
  st.success("Done!")