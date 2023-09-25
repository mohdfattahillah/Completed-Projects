import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

def run():
    # Membuat Tittle:
    st.markdown(
        """
        <div style='text-align: center; background-color: #FFFFFF; padding: 40px;'>
        <h2 style='text-align: center; color: #000000;'>EXPLORATORY DATA ANALYSIS OF CREDIT CARD DEFAULT PREDICTION</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write('---')

    # Buka gambar
    image = Image.open('cc.png')
    # Mendapatkan ukuran gambar
    width, height = image.size
    # Menampilkan gambar dengan tata letak tengah
    st.image(image, caption='Credit Card Defaulter', use_column_width=True)
    st.write('---')

    # Membuat Sub Header Center dengan Background:
    st.markdown("<h3 style='text-align: center; background-color: #FFFFFF; padding: 10px; color: #000000;'>DATASET:</h3>", unsafe_allow_html=True)

    # Show Dataframe:
    data = pd.read_csv('https://raw.githubusercontent.com/mohdfattahillah/Learning-Journal/master/P1G5_Set_1_muhammad-fattahillah.csv')
    st.dataframe(data)
    st.write('---')

    # LIMIT BALANCE X DEFAULT PAYMENT:
    st.markdown("<h3 style='text-align: center; background-color: #FFFFFF; padding: 10px; color: #000000;'>DEAULTER BY LIMIT BALANCE:</h3>", unsafe_allow_html=True)
    st.write('---')    
    i = list(data[data['default_payment_next_month'] == 1]['limit_balance'])
    j = list(data[data['default_payment_next_month'] == 0]['limit_balance'])
    fig = plt.figure(figsize=(10,4))
    plt.hist([i, j], bins = 40, color=['purple', 'plum'])
    plt.xlim([0,600000])
    plt.legend(['Yes', 'No'], title = 'default_payment_next_month', loc='upper right', facecolor='white', shadow=True)
    plt.xlabel('Limit Balance (in Dollars)')
    plt.ylabel('Frequency')
    plt.title('Limit Balance Histogram by "default_payment_next_month"')
    st.pyplot(fig)
    st.markdown("<h5 style='text-align: center; background-color: #FFFFFF; padding: 10px; color: #663399;'><em>Dari histogram di atas bisa dilihat bahwa defaulters cenderung lebih banyak di klien dengan limit balance $200000 kebawah.</em></h3>", unsafe_allow_html=True)
    st.write('---')

    # AGE X DEFAULT PAYMENT:
    st.markdown("<h3 style='text-align: center; background-color: #FFFFFF; padding: 10px; color: #000000;'>DEAULTER BY AGE:</h3>", unsafe_allow_html=True)
    st.write('---')   
    u = list(data[data['default_payment_next_month'] == 1]['age'])
    v = list(data[data['default_payment_next_month'] == 0]['age'])
    fig = plt.figure(figsize=(10,4))
    plt.hist([u, v], bins = 20, color=['purple', 'plum'])
    plt.legend(['Yes', 'No'], title = 'default_payment_next_month', loc='upper right', facecolor='white', shadow=True)
    plt.xlabel('age')
    plt.ylabel('Frequency')
    plt.title('Age Histogram by "default_payment_next_month"')
    st.pyplot(fig)
    st.markdown("<h5 style='text-align: center; background-color: #FFFFFF; padding: 10px; color: #663399;'><em>Dari histogram di atas bisa dilihat bahwa defaulters cenderung lebih banyak di klien dengan umur antara 25-50 tahun.</em></h3>", unsafe_allow_html=True)
    st.write('---')

    # SEX X DEFAULT PAYMENT:
    st.markdown("<h3 style='text-align: center; background-color: #FFFFFF; padding: 10px; color: #000000;'>DEAULTER BY SEX/GENDER:</h3>", unsafe_allow_html=True)
    st.write('---')   
    fig = plt.figure(figsize=(8,4))
    ax=sns.countplot(data=data, x="sex", hue="default_payment_next_month", palette="magma")
    for label in ax.containers:
        ax.bar_label(label)
    plt.xticks([0,1], labels=["Male", "Female"])
    plt.title("Sex variable distribution by default_payment_next_month")
    plt.legend(['No', 'Yes'], title = 'default_payment_next_month', loc='upper left', facecolor='white', shadow=True)
    st.pyplot(fig)
    st.markdown("<h5 style='text-align: center; background-color: #FFFFFF; padding: 10px; color: #663399;'><em>Dari histogram di atas bisa dilihat bahwa jumlah klien lebih banyak wanita dan defaulters cenderung lebih banyak di klien wanita juga dibandingkan laki-laki.</em></h3>", unsafe_allow_html=True)
    st.write('---')

    # EDUCATION LEVEL X DEFAULT PAYMENT:
    st.markdown("<h3 style='text-align: center; background-color: #FFFFFF; padding: 10px; color: #000000;'>DEAULTER BY EDUCATION LEVEL:</h3>", unsafe_allow_html=True)
    st.write('---')   
    fig = plt.figure(figsize=(10,6))
    ax=sns.countplot(data=data, x="education_level", hue="default_payment_next_month", palette="magma")
    for label in ax.containers:
        ax.bar_label(label)
    plt.xticks([0,1,2,3,4,5,6], labels=["Unknown", "Graduate School", "University", "High School", "Unknown", "Unknown", "Unknown"])
    plt.title("Education variable distribution by default_payment_next_month")
    plt.legend(['No', 'Yes'], title = 'default_payment_next_month', loc='upper right', facecolor='white', shadow=True)
    st.pyplot(fig)
    st.markdown("<h5 style='text-align: center; background-color: #FFFFFF; padding: 10px; color: #663399;'><em>Dari histogram di atas bisa dilihat bahwa jumlah klien lebih banyak yang berasal dari lulusan University dan yang paling sedikit adalah klien yang tidak berpendidikan atau sekolah/unknown. Dan untuk defaulters sebagian besar juga terjadi di kalangan lulusan Universitas.</em></h3>", unsafe_allow_html=True)
    st.write('---')

    # MARITAL STATUS X DEFAULT PAYMENT:
    st.markdown("<h3 style='text-align: center; background-color: #FFFFFF; padding: 10px; color: #000000;'>DEAULTER BY MARITAL STATUS:</h3>", unsafe_allow_html=True)
    st.write('---')   
    fig = plt.figure(figsize=(10,5))
    ax=sns.countplot(data=data, x="marital_status", hue="default_payment_next_month", palette="magma")
    for label in ax.containers:
        ax.bar_label(label)
    plt.xticks([0,1,2,3], labels=["Unknown", "Married", "Single", "Others"])
    plt.title("Marriage variable distribution by default_payment_next_month")
    plt.legend(['No', 'Yes'], title = 'default_payment_next_month', loc='upper right', facecolor='white', shadow=True)
    st.pyplot(fig)
    st.markdown("<h5 style='text-align: center; background-color: #FFFFFF; padding: 10px; color: #663399;'><em>Dari histogram di atas bisa dilihat bahwa jumlah klien lebih banyak yang berstatus Married dan Single. Dan defaulters juga cenderung lebih banyak pada klien yang berstatus Married dan Single tersebut.</em></h3>", unsafe_allow_html=True)
    st.write('---')

    # Plot untuk melihat persentase defaulter:
    st.markdown("<h3 style='text-align: center; background-color: #FFFFFF; padding: 10px; color: #000000;'>DEAULTER YES/NO PERCENTAGE:</h3>", unsafe_allow_html=True)
    st.write('---')
    fig = plt.figure(figsize=(10,10))
    perc_default = data.default_payment_next_month.sum() / len(data.default_payment_next_month)
    data['default_payment_next_month'].value_counts().plot(kind='pie', explode=[0.1,0],autopct="%1.1f%%")
    st.pyplot(fig)
    st.markdown("<h5 style='text-align: center; background-color: #FFFFFF; padding: 10px; color: #663399;'><em>0: Status Pembayaran Normal | 1: Status Pembayaran Gagal:</em></h3>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; background-color: #FFFFFF; padding: 10px; color: #663399;'><em>Dari pie chart di atas menunjukkan bahwa persentase klien yang gagal bayar dalam data adalah 21,4%.</em></h3>", unsafe_allow_html=True)
    st.write('---')

if __name__ == '__main__':
    run()