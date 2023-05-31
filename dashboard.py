#Import Library yang digunakan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
from PIL import Image
from babel.numbers import format_currency
sns.set(style='dark')

st.title("Dashboard Visualisasi Data sederhana E-Commerce Brazil")


st.header("Presentase customer, seller, product, dan order")
with st.container():
   
    labels = 'Produk', 'Penjual', 'Pelanggan', 'Pesanan'
    sizes = [14.1, 1.3, 42.3, 42.3]
    explode = (0, 0.1, 0, 0)  

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  

st.pyplot(fig1)

with st.expander("See explanation"):
    st.write( """Dari pie chart di atas, menunjukan bahwa produk memiliki presentase 14.1%, pesanan 42.3%, pelanggan 42.3% dan penjual 1.3%
        """)    
    
st.header("Histogram customer pada setiap state")
image_path = "histogram.png"
st.image(image_path, use_column_width=True)

st.caption('Submission Dicoding - Data Analys tahap 1')