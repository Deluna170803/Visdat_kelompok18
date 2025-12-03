import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------------------------
#      IDENTITAS KELOMPOK 18
# --------------------------------------------------------------------

st.title("Streamlit — Bar Chart dan Trend Analisis")

st.markdown("""
### **Kelompok 18**
- Raydino Situmeang (0110222278)  
- Deva Lubna Listya (0110222258)  
- Apriyanto (0110222256)
""")

# --------------------------------------------------------------------
#                           BAGIAN A — BAR CHART
# --------------------------------------------------------------------

st.header("a. Bar Chart")

# =============================
# DATA DASAR (SUDAH DIUBAH)
# =============================
data = {
    'Jurusan': ['Sistem Informasi', 'Teknik Informatika', 'Bisnis Digital'],
    'Jumlah Mahasiswa': [150, 120, 90]
}
df = pd.DataFrame(data)

# =============================
# 1. Basic Bar Chart Streamlit
# =============================
st.subheader("1) Basic Bar Chart (Streamlit Built-in)")

st.bar_chart(df.set_index('Jurusan'))


# =============================
# 2. Bar Chart Matplotlib
# =============================
st.subheader("2) Basic Bar Chart Menggunakan Matplotlib")

fig, ax = plt.subplots()
ax.bar(data['Jurusan'], data['Jumlah Mahasiswa'], color='skyblue')
ax.set_title('Jumlah Mahasiswa per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')
st.pyplot(fig)

# =============================
# 3. Kustomisasi Bar Chart
# =============================
st.subheader("3) Kustomisasi Bar Chart")

fig, ax = plt.subplots()
colors = ['blue', 'green', 'orange']
bars = ax.bar(data['Jurusan'], data['Jumlah Mahasiswa'], color=colors)
ax.set_title('Jumlah Mahasiswa per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3,
            str(bar.get_height()), ha='center')

st.pyplot(fig)


# =============================
# 4. Multiple Bar Chart (2023 vs 2024)
# =============================
st.subheader("4) Multiple Basic Bar Chart")

data_2023 = [150, 120, 90]
data_2024 = [160, 130, 100]

x = range(len(data['Jurusan']))
width = 0.35

fig, ax = plt.subplots()
ax.bar(x, data_2023, width=width, label='2023', color='skyblue')
ax.bar([p + width for p in x], data_2024, width=width, label='2024', color='orange')

ax.set_title('Jumlah Mahasiswa per Jurusan (2023 vs 2024)')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')
ax.set_xticks([p + width / 2 for p in x])
ax.set_xticklabels(data['Jurusan'])
ax.legend()

st.pyplot(fig)

# --------------------------------------------------------------------
#             BAGIAN B — POLA & TREND DENGAN BAR CHART
# --------------------------------------------------------------------
st.header("b. Pola dan Trend dengan Bar Chart")
# DATA TREND 5 TAHUN (DIUBAH)
data_tren = {
    'Tahun': ['2019', '2020', '2021', '2022', '2023'],
    'Sistem Informasi': [120, 130, 145, 150, 160],
    'Teknik Informatika': [100, 110, 115, 120, 130],
    'Bisnis Digital': [60, 70, 80, 85, 95]
}

df2 = pd.DataFrame(data_tren)

st.subheader("Visualisasi Tren Jumlah Mahasiswa 3 Jurusan (5 Tahun Terakhir)")
# FILTER TAHUN
filter_tahun = st.multiselect("Pilih Tahun:", df2['Tahun'], default=df2['Tahun'])
# FILTER JURUSAN
jurusan_list = ['Sistem Informasi', 'Teknik Informatika', 'Bisnis Digital']
filter_jurusan = st.multiselect("Pilih Jurusan:", jurusan_list, default=jurusan_list)
# FILTER DATA
filtered_data = df2[df2['Tahun'].isin(filter_tahun)][['Tahun'] + filter_jurusan]
# TAMPILKAN DATA
st.subheader("Data Jumlah Mahasiswa")
st.dataframe(filtered_data)

# =============================
# BAR CHART BERDASARKAN FILTER
# =============================
st.subheader("Bar Chart dengan Filter")

fig, ax = plt.subplots(figsize=(10, 6))

x = range(len(filtered_data['Tahun']))
width = 0.2

for i, jur in enumerate(filter_jurusan):
    ax.bar([p + i * width for p in x], filtered_data[jur], width=width, label=jur)

ax.set_title("Jumlah Mahasiswa per Jurusan (Berdasarkan Filter)")
ax.set_xlabel("Tahun")
ax.set_ylabel("Jumlah Mahasiswa")
ax.set_xticks([p + width * len(filter_jurusan) / 2 - width / 2 for p in x])
ax.set_xticklabels(filtered_data['Tahun'])
ax.legend()

st.pyplot(fig)
