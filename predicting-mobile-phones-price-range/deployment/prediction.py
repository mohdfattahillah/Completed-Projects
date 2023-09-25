import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json

# Membuka file proses yang sudah disave sebelumnya:
with open('best_svm_model.pkl', 'rb') as file_1:
  model = joblib.load(file_1)
with open('preprocessing_pipeline.pkl', 'rb') as file_2:
  preprocessing = joblib.load(file_2)

def run():

    st.markdown("""
        <div style='text-align: center; background-color: #FFFFFF; padding: 40px;'>
        <h2 style='text-align: center; color: #000000;'>PREDICT YOUR MOBILE PHONE PRICE CATEGORY WITH THIS GREAT APP!</h3></div>""",unsafe_allow_html=True)

    # Membuat form
    with st.form("mobile_phone_form"):
        name = st.text_input("Mobile Phone Name")
        battery_power = st.slider("Battery Capacity (mAh)", min_value=0, max_value=6000, step=1000)
        ram = st.slider("RAM (MB)", min_value=0, max_value=16000, step=1000)
        int_memory = st.number_input("Internal Memory (GB)", min_value=0, max_value=512)
        pc = st.number_input("Main Camera Pixel Size", min_value=0, max_value=100)
        px_width = st.number_input("Pixel Resolution Width", min_value=0, max_value=4000)
        px_height = st.number_input("Pixel Resolution Height", min_value=0, max_value=4000)
        submitted = st.form_submit_button("Submit")

    # Membuat dataframe dari input user diatas
    if submitted:
        data = {
            "Mobile Phone": [name],
            "ram": [ram],
            "battery_power": [battery_power],
            "px_width": [px_width],
            "px_height": [px_height],
            "int_memory": [int_memory],
            "pc": [pc]
        }
        df = pd.DataFrame(data)

        # Melakukan preprocessing pada data (selain kolom name)
        df_preprocessed = preprocessing.transform(df.drop(columns=['Mobile Phone']))

        # Membuat prediksi menggunakan model
        predicted_price = model.predict(df_preprocessed)

        # Memperlihatkan input user
        st.write("Your Inputs:")
        st.write(df)

        if predicted_price[0] == 0:
            st.markdown("""
            <div style='text-align: center; background-color: #FFFFFF; padding: 20px;'>
            <h2 style='text-align: center; color: #000000;'>Your Predicted Phone Price Category:</h4>
            <h1 style='text-align: center; color: #FF0000;'>Low Price</h3>
            <h7 style='text-align: center; color: #000000;'>Note: (0 = Low Cost | 1 = Medium Cost | 2 = High Cost | 3 = Very High Cost)</h4>""",unsafe_allow_html=True)
        elif predicted_price[0] == 1:
            st.markdown("""
            <div style='text-align: center; background-color: #FFFFFF; padding: 20px;'>
            <h2 style='text-align: center; color: #000000;'>Your Predicted Phone Price Category:</h4>
            <h1 style='text-align: center; color: #FF0000;'>Medium Price</h3>
            <h7 style='text-align: center; color: #000000;'>Note: (0 = Low Cost | 1 = Medium Cost | 2 = High Cost | 3 = Very High Cost)</h4>""",unsafe_allow_html=True)        
        elif predicted_price[0] == 2:
            st.markdown("""
            <div style='text-align: center; background-color: #FFFFFF; padding: 20px;'>
            <h2 style='text-align: center; color: #000000;'>Your Predicted Phone Price Category:</h4>
            <h1 style='text-align: center; color: #FF0000;'>High Price</h3>
            <h7 style='text-align: center; color: #000000;'>Note: (0 = Low Cost | 1 = Medium Cost | 2 = High Cost | 3 = Very High Cost)</h4>""",unsafe_allow_html=True)             
        elif predicted_price[0] == 3:
            st.markdown("""
            <div style='text-align: center; background-color: #FFFFFF; padding: 20px;'>
            <h2 style='text-align: center; color: #000000;'>Your Predicted Phone Price Category:</h4>
            <h1 style='text-align: center; color: #FF0000;'>Very High Price</h3>
            <h7 style='text-align: center; color: #000000;'>Note: (0 = Low Cost | 1 = Medium Cost | 2 = High Cost | 3 = Very High Cost)</h4>""",unsafe_allow_html=True)             
        else:
            st.markdown("""
            <div style='text-align: center; background-color: #FF0000; padding: 0px;'>
            <h6 style='text-align: center; color: #FFFFFF;'>Please check your input values and try again.</h6></div>""",unsafe_allow_html=True)

if __name__ == '__main__':
    run()