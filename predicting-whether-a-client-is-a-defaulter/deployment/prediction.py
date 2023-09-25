import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json

# Membuka file proses yang sudah disave sebelumnya:
with open('model_lr.pkl', 'rb') as file_1:
  model_lr = joblib.load(file_1)
with open('model_svc.pkl', 'rb') as file_2:
  model_svc = joblib.load(file_2)
with open('model_knn.pkl', 'rb') as file_3:
  model_knn = joblib.load(file_3)

def run():
    # Daftar bulan dan status yang tersedia
    bulan = ['sept', 'aug', 'jul', 'jun', 'may', 'apr']
    status = [
        'Bayar Lunas',
        'Terlambat 1 Bulan',
        'Terlambat 2 Bulan',
        'Terlambat 3 Bulan',
        'Terlambat 4 Bulan',
        'Terlambat 5 Bulan',
        'Terlambat 6 Bulan',
        'Terlambat 7 Bulan',
        'Terlambat 8 Bulan',
        'Terlambat 9 Bulan',
    ]

    # Membuat dictionary untuk menyimpan input pengguna
    input_user = {}

    # Dictionary untuk mapping status ke nilai numerik
    status_mapping = {
    'Bayar Lunas': 0,
    'Terlambat 1 Bulan': 1,
    'Terlambat 2 Bulan': 2,
    'Terlambat 3 Bulan': 3,
    'Terlambat 4 Bulan': 4,
    'Terlambat 5 Bulan': 5,
    'Terlambat 6 Bulan': 6,
    'Terlambat 7 Bulan': 7,
    'Terlambat 8 Bulan': 8,
    'Terlambat 9 Bulan': 9
    }

    # Gunakan st.markdown untuk menambahkan teks HTML ke tampilan Streamlit
    st.markdown(
        """
        <div style='text-align: center; background-color: #FFFFFF; padding: 40px;'>
        <h3 style='text-align: center; color: #000000;'>APLIKASI UNTUK MEMPREDIKSI APAKAH KAMU AKAN GAGAL BAYAR KARTU KREDITMU BULAN DEPAN</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Membuat form
    with st.form(key='input_form'):
        # Loop melalui setiap bulan
        for b in bulan:
            # st.write(f"### Bulan {b}")
            
            # Dropdown untuk memilih status
            selected_status = st.selectbox(f"Bagaimana Status Pembayaranmu Untuk Bulan {b}:", status)
            
            # Menyimpan input pengguna ke dalam dictionary
            input_user[f'pay_{b.lower()}'] = status_mapping[selected_status]

        # Tombol "Predict"
        predict_button = st.form_submit_button(label='Prediksikan Pembayaran Kartu Kreditmu Bulan depan')

    # Jika tombol "Predict" ditekan
    if predict_button:
        # Membuat DataFrame baru dari input pengguna
        new_data = pd.DataFrame(input_user, index=[0])

        # Menampilkan DataFrame baru
        st.write("Data yang kamu berikan adalah seperti berikut:")
        st.write(new_data)
        st.write('---')

        # Gunakan st.markdown untuk menambahkan teks HTML ke tampilan Streamlit
        st.markdown(
            """
            <div style='text-align: center; background-color: #FFFFFF; padding: 20px;'>
            <h4 style='text-align: center; color: #000000;'>HASIL PREDIKSI MENGGUNAKAN 3 MODEL MACHINE LEARNING:</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Prediksi dengan model Logistic Regression
        prediction_lr = model_lr.predict(new_data)
        st.write("---")
        st.markdown("""<h4 style='text-align: center; color: #FFFFFF;'>LOGISTIC REGRESSION:</h4></div>""",unsafe_allow_html=True)
        if prediction_lr[0] == 0:
            st.markdown("""
            <div style='text-align: center; background-color: #00FF00; padding: 0px;'>
            <h6 style='text-align: center; color: #000000;'>Hasil Prediksi: Kamu akan membayar kartu kreditmu secara normal bulan depan.</h6></div>""",unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style='text-align: center; background-color: #FF0000; padding: 0px;'>
            <h6 style='text-align: center; color: #FFFFFF;'>Hasil Prediksi: Kamu akan gagal membayar kartu kreditmu bulan depan.</h6></div>""",unsafe_allow_html=True)

        # Prediksi dengan model Support Vector Classifier (SVC)
        prediction_svc = model_svc.predict(new_data)
        st.write("---")
        st.markdown("""<h4 style='text-align: center; color: #FFFFFF;'>SUPPORT VECTOR CLASSIFIER:</h4></div>""",unsafe_allow_html=True)
        if prediction_svc[0] == 0:
            st.markdown("""
            <div style='text-align: center; background-color: #00FF00; padding: 0px;'>
            <h6 style='text-align: center; color: #000000;'>Hasil Prediksi: Kamu akan membayar kartu kreditmu secara normal bulan depan.</h6></div>""",unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style='text-align: center; background-color: #FF0000; padding: 0px;'>
            <h6 style='text-align: center; color: #FFFFFF;'>Hasil Prediksi: Kamu akan gagal membayar kartu kreditmu bulan depan.</h6></div>""",unsafe_allow_html=True)

        # Prediksi dengan model K-Nearest Neighbors (KNN)
        prediction_knn = model_knn.predict(new_data)
        st.write("---")
        st.markdown("""<h4 style='text-align: center; color: #FFFFFF;'>K NEAREST NEIGHBORS:</h4></div>""",unsafe_allow_html=True)
        if prediction_knn[0] == 0:
            st.markdown("""
            <div style='text-align: center; background-color: #00FF00; padding: 0px;'>
            <h6 style='text-align: center; color: #000000;'>Hasil Prediksi: Kamu akan membayar kartu kreditmu secara normal bulan depan.</h6></div>""",unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style='text-align: center; background-color: #FF0000; padding: 0px;'>
            <h6 style='text-align: center; color: #FFFFFF;'>Hasil Prediksi: Kamu akan gagal membayar kartu kreditmu bulan depan.</h6></div>""",unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style='text-align: left; background-color: #FF0000; padding: 0px;'>
        <h6 style='text-align: left; color: #FFFFFF;'>Tekan tombol diatas untuk melihat hasil prediksimu.</h6></div>""",unsafe_allow_html=True)

if __name__ == '__main__':
    run()