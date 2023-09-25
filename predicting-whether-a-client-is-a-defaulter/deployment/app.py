import streamlit as st
import eda
import prediction

st.set_page_config(
    page_title = 'APLIKASI UNTUK MEMPREDIKSI APAKAH KAMU AKAN GAGAL BAYAR KARTU KREDITMU BULAN DEPAN',
    layout = 'wide',
    initial_sidebar_state = 'expanded'
)

page = st.sidebar.selectbox('Pilih Halaman: ', ('Exploratory Data Analysis', 'Prediksi Pembayaran Kartu Kredit'))

if page == 'Exploratory Data Analysis':
    eda.run()
else:
    prediction.run()