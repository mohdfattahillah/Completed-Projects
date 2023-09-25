import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

def run():
    # Membuat title
    st.markdown(
        """
        <div style='text-align: center; background-color: #FFFFFF; padding: 40px;'>
        <h2 style='text-align: center; color: #000000;'>EXPLORATORY DATA ANALYSYS OF MOBILE PHONES PRICE RANGE</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write('---')

    # Membuka gambar
    image = Image.open('header.jpg')
    # Mendapatkan ukuran gambar
    width, height = image.size
    # Menampilkan gambar dengan tata letak tengah
    st.image(image, caption='Mobile Phones', use_column_width=True)
    st.write('---')

    # Membuka dataset
    df = pd.read_csv('https://raw.githubusercontent.com/mohdfattahillah/Learning-Journal/master/mobile_prices.csv')

    # PIE CHART OF NUMERIC CATEGORICAL COLUMNS:
    st.markdown("<h3 style='text-align: center; background-color: #FFFFFF; padding: 10px; color: #000000;'>PIE CHART OF PHONES SPECIFICATIONS</h3>", unsafe_allow_html=True)
    st.write('---')    
    # Kolom-kolom yang akan diplot
    pie_cols = ['blue', 'dual_sim', 'four_g', 'n_cores', 'three_g', 'touch_screen', 'wifi', 'price_range']
    # Warna yang akan digunakan
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0','#ffb3e6', '#c2f0c2', '#ffb3e6']
    # Ukuran gambar subplot
    fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(16, 8))
    # Membuat pie chart terpisah untuk setiap kolom
    for i, column in enumerate(pie_cols):
        sizes = df[column].value_counts().values
        labels = df[column].value_counts().index
        explode = [0.1] * len(sizes)
        ax = axes[i // 4, i % 4]
        ax.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90, colors=colors, explode=explode)
        ax.axis('equal')
        ax.set_title(f'{column}')
    st.pyplot(fig)
    st.markdown("<h5 style='text-align: center; background-color: #FFFFFF; padding: 10px; color: #663399;'><em>Dari visualisasi diatas dapat dilihat bahwa distribusi data untuk ponsel yang memiliki bluetooth, dual sim, 4g, touch screen, dan wifi cenderung terbagi secara merata. Untuk konektivitas 3g terdapat 23.8% ponsel tidak memiliki fitur tersebut. Untuk jumlah cores dari masing-masing ponsel terbagi secara merata mulai dari 1 core sampai dengan 8 core. Dan untuk klasifikasi rentang harga juga terbagi secara merata 25% masing-masing kepada 0 (low cost), 1 (medium cost), 2 (high cost), dan 3 (very high cost).</em></h3>", unsafe_allow_html=True)
    st.write('---')

    # SPECIFICATIONS VS PRICE RANGE:
    st.markdown("<h3 style='text-align: center; background-color: #FFFFFF; padding: 10px; color: #000000;'>SPECIFICATIONS VS PRICE RANGE</h3>", unsafe_allow_html=True)
    st.write('---')   
    # Menentukan fitur-fitur yang akan diplot
    kolom = ['int_memory', 'clock_speed', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height', 'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time']
    # Menentukan jumlah baris dan kolom subplot
    rows = 4
    cols = 3
    # Membuat subplot
    fig, axes = plt.subplots(rows, cols, figsize=(15, 18))
    fig.subplots_adjust(hspace=0.5)
    # Meloop melalui setiap fitur dan membuat plot
    for i, feature in enumerate(kolom):
        row = i // cols
        col = i % cols
        sns.boxplot(x='price_range', y=feature, data=df, palette='Set3', ax=axes[row, col])
        axes[row, col].set_title(f'{feature} vs. price_range')
        axes[row, col].set_xlabel('price_range')
        axes[row, col].set_ylabel(feature)
    st.pyplot(fig)
    st.markdown("<h5 style='text-align: center; background-color: #FFFFFF; padding: 10px; color: #663399;'><em>Terlihat adanya pengaruh signifikan dari besarnya RAM, Resolusi Layar, Jumlah Inti Prosesor, dan Kamera Utama terhadap harga sebuah ponsel.</em></h3>", unsafe_allow_html=True)
    st.write('---')

    # BEST MODEL EVALUATION:
    st.markdown("<h3 style='text-align: center; background-color: #FFFFFF; padding: 10px; color: #000000;'>MACHINE LEARNING MODEL PERFORMANCES</h3>", unsafe_allow_html=True)
    st.write('---')   
    # Membuka gambar
    image = Image.open('modelevalfinal1.png')
    image2 = Image.open('modelevalfinal2.png')
    # Mendapatkan ukuran gambar
    width, height = image.size, image2.size
    # Menampilkan gambar dengan tata letak tengah
    st.image(image, use_column_width=True)
    st.image(image2, use_column_width=True)
    st.markdown("<h5 style='text-align: center; background-color: #FFFFFF; padding: 10px; color: #663399;'><em>Visualisasi diatas menunjukkan bahwa model machine learning yang diterapkan dalam aplikasi ini sangat efektif dalam mengklasifikasikan harga ponsel ke dalam berbagai kelas harga. Terbukti dengan hasil evaluasi yang sangat baik dan akurat.</em></h3>", unsafe_allow_html=True)
    st.write('---')

if __name__ == '__main__':
    run()