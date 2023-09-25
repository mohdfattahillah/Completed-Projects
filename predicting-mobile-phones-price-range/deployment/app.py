import streamlit as st
import eda
import prediction

st.set_page_config(
    page_title = 'PREDICT YOUR MOBILE PHONE PRICE CATEGORY WITH THIS GREAT APP!',
    layout = 'wide',
    initial_sidebar_state = 'expanded'
)

page = st.sidebar.selectbox('Choose Page: ', ('Exploratory Data Analysis', 'Application'))

if page == 'Exploratory Data Analysis':
    eda.run()
else:
    prediction.run()