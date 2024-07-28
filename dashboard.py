import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi
st.title('Pemetaan Perilaku Pelanggan Rental Sepeda "Manunggal"')

hours_data = pd.read_csv("main_data.csv")

hours_data['dteday'] = pd.to_datetime(hours_data['dteday'])

weather_map = {
    1: 'Cerah', 
    2: 'Berawan', 
    3: 'Hujan Ringan', 
    4: 'Hujan Lebat'
}
holiday_map = {
    0: "Hari Kerja", 
    1: "Hari Libur"
}

hours_data['weathersit'] = hours_data['weathersit'].map(weather_map)
hours_data['holiday'] = hours_data['holiday'].map(holiday_map)

st.subheader('🕗 Jam Berapa Biasanya Orang Menyewa Sepeda?')
hours_mean = hours_data.groupby('hr')['cnt'].mean()
colors = ['tab:blue' if val <= 300 else 'tab:orange' for val in hours_mean.values]
fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(hours_mean.index, hours_mean.values, color=colors, width=0.5)
# ax.set_title('Jam Berapa Biasanya Orang Menyewa Sepeda?')
ax.set_xlabel('Jam')
ax.set_ylabel('Jumlah Penyewaan')
ax.set_xticks(hours_mean.index)
ax.grid(axis='y', alpha=1)
for i, v in enumerate(hours_mean):
    ax.text(i, v, f'{v:.0f}', ha='center', va='bottom')
st.pyplot(fig)
st.markdown(''' ### Behaviour Penyewa: Angka Penyewaan Melonjak Saat Jam Sibuk
**Ini menjawab pertanyaan pertama, yaitu apakah ada pola khusus dalam jumlah penyewaan? Jam berapa biasanya permintaan melonjak?**
- Penyewaan sepeda mencapai puncaknya pada jam sibuk, terutama pukul 8 pagi dan antara pukul 4-7 malam. Dengan ini, menunjukkan banyaknya kebutuhan sepeda untuk transport ke tempat kerja.

- Permintaan terus meningkat hingga mencapai lebih dari 400 sepeda pada pukul 5-6 sore.

- Penurunan permintaan setelah pukul 8 pagi dan peningkatan bertahap mulai pukul 11 siang.

- Angka penyewaan pada tengah malam dan dini hari tetap ada. Menunjukkan penyewaan sepeda tetap diminati hingga malam hari. 

- Semakin malam semakin menurun angkanya, dan mulai naik perlahan pada jam 5 pagi.
''')

st.subheader('⛅ Seberapa berpengaruh cuaca dan hari libur?')
col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    st.bar_chart(hours_data, x="weathersit", y="cnt", color="holiday", stack=False, x_label="Cuaca", y_label="Jumlah Penyewaan")

with col2:
    fig, ax = plt.subplots()
    sns.barplot(data=hours_data, x="holiday", y="cnt", errorbar=None, ax=ax)
    ax.set_title('Pengaruh Hari Libur Terhadap Jumlah Penyewaan')
    ax.set_xlabel('Liburan')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.grid(axis='y', alpha=1)
    st.pyplot(fig)

st.markdown('''### Behaviour Penyewa: Cuaca dan Hari Libur Memiliki Pengaruh dalam Jumlah Penyewaan
**Ini menjawab pertanyaan kedua, yaitu apakah ada pola khusus dalam jumlah penyewaan? Apakah cuaca buruk juga mempengaruhi jumlah permintaan? Apakah hal itu berlaku juga saat hari libur?**
- Permintaan pada hari kerja lebih tinggi daripada hari libur mencapai 20% pada cuaca terang. 

- Bahkan saat hujan deras, permintaan tetap ada pada hari kerja. Dengan ini, membuktikan bahwa penyewaan sepeda sangat dibutuhkan untuk mobilitas ke tempat kerja.
    
- Pada setiap perbedaan cuaca, ketika memburuk, akan terjadi penurunan angka permintaan juga. Sebaliknya jika membaik (cerah), maka permintaan akan meningkat juga. Ini menunjukkan bahwa cuaca adalah faktor yang mempengaruhi angka permintaan. Bahkan, di saat liburan dan hujan deras, hampir tidak ada angka permintaan.''')

with st.sidebar:
    st.image("logo.png")
    st.header("Rental Sepeda Manunggal")
    st.caption("Jalan Jendral Sudirman, No. 31, Kecamatan Ngadipuro, Kabupaten Blitar, Jawa Timur")
    st.link_button("Hubungi via Whatsapp", "https://wa.me/62812345678")
