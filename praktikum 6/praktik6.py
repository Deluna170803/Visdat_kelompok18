import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
# JUDUL 
st.title("Visualisasi Data Pengunjung Perpustakaan Kampus")
# DATA FAKULTAS
faculties = [
    'Teknik Informatika',
    'Sistem Informasi',
    'Bisnis Digital'
]
x = np.arange(len(faculties))

# GRAFIK 1
# Jumlah Pengunjung Perpustakaan (Gender)
st.subheader("Jumlah Pengunjung Perpustakaan Berdasarkan Fakultas")

male_visitors = [180, 210, 190]
female_visitors = [240, 260, 230]

fig1, ax1 = plt.subplots()

ax1.bar(x, male_visitors, label='Laki-laki', color='#1f77b4')
ax1.bar(
    x,
    female_visitors,
    bottom=male_visitors,
    label='Perempuan',
    color='#ff7f0e'
)

ax1.set_ylabel('Jumlah Pengunjung')
ax1.set_title('Pengunjung Perpustakaan Berdasarkan Gender')
ax1.set_xticks(x)
ax1.set_xticklabels(faculties)
ax1.legend()

st.pyplot(fig1)


# GRAFIK 2
# Peminjaman Koleksi Perpustakaan
st.subheader("Peminjaman Koleksi Perpustakaan")

physical_books = [320, 350, 330]   # Buku Fisik
ebooks = [180, 210, 200]           # E-Book

fig2, ax2 = plt.subplots()

ax2.bar(x, physical_books, label='Buku Fisik', color='#2ca02c')
ax2.bar(
    x,
    ebooks,
    bottom=physical_books,
    label='E-Book',
    color='#9467bd'
)

ax2.set_ylabel('Jumlah Peminjaman')
ax2.set_title('Peminjaman Koleksi Perpustakaan Berdasarkan Fakultas')
ax2.set_xticks(x)
ax2.set_xticklabels(faculties)
ax2.legend()

st.pyplot(fig2)


# GRAFIK 3
# Multiple Stacked Vertical Bar Chart (Periode)
st.subheader("Perbandingan Pengunjung Perpustakaan per Periode")

# Data Periode
period1_male = [90, 110, 100]
period1_female = [120, 140, 130]

period2_male = [100, 120, 110]
period2_female = [130, 150, 140]

bar_width = 0.35

fig3, ax3 = plt.subplots()

ax3.bar(
    x - bar_width / 2,
    period1_male,
    width=bar_width,
    label='Periode 1 Laki-laki',
    color='#aec7e8'
)
ax3.bar(
    x - bar_width / 2,
    period1_female,
    bottom=period1_male,
    width=bar_width,
    label='Periode 1 Perempuan',
    color='#ff9896'
)
ax3.bar(
    x + bar_width / 2,
    period2_male,
    width=bar_width,
    label='Periode 2 Laki-laki',
    color='#98df8a'
)
ax3.bar(
    x + bar_width / 2,
    period2_female,
    bottom=period2_male,
    width=bar_width,
    label='Periode 2 Perempuan',
    color='#f7b6d2'
)
ax3.set_ylabel('Jumlah Pengunjung')
ax3.set_title('Perbandingan Pengunjung Perpustakaan per Fakultas')
ax3.set_xticks(x)
ax3.set_xticklabels(faculties)
ax3.legend()
st.pyplot(fig3)



