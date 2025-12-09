import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# HEADER SCATTER PLOT

st.title("Analisis dan Visualisasi Penjualan Es Krim Berdasarkan Suhu")

st.markdown("""
### Kelompok 18
- **Raydino Situmeang** (0110222278)  
- **Deva Lubna Listya** (0110222258)  
- **Apriyanto** (0110222256)
---
""")


# DATA SCATTER DASAR

suhu = np.array([20, 22, 24, 26, 28, 30, 32, 34, 36])
penjualan = np.array([50, 60, 70, 90, 100, 110, 130, 150, 180])


# SCATTER PLOT  + TREND LINE

st.subheader("1. Hubungan Suhu dan Penjualan")

fig, ax = plt.subplots()
ax.scatter(
    suhu,
    penjualan,
    c=penjualan,
    cmap='viridis',
    s=120,
    marker='o',
    edgecolor='black',
    alpha=0.85,
    label='Data Penjualan'
)

# Garis tren (regresi linear)
z = np.polyfit(suhu, penjualan, 1)
p = np.poly1d(z)
ax.plot(suhu, p(suhu), linestyle='--', linewidth=2, color='red', label='Garis Tren')

ax.set_title("Pengaruh Suhu terhadap Penjualan Es Krim")
ax.set_xlabel("Suhu (°C)")
ax.set_ylabel("Penjualan Es Krim")
ax.legend()
ax.grid(True, linestyle='--', alpha=0.5)

st.pyplot(fig)


# MULTIPLE SCATTER 

st.subheader("2. Perbandingan Penjualan Hari Kerja dan Akhir Pekan")

penjualan_kerja = [50, 60, 70, 80, 90, 100, 110, 120, 130]
penjualan_akhir_pekan = [60, 70, 80, 100, 110, 120, 140, 160, 200]

fig, ax = plt.subplots()
ax.scatter(
    suhu, penjualan_kerja,
    color='#1f77b4',
    s=100,
    marker='s',
    label='Hari Kerja'
)
ax.scatter(
    suhu, penjualan_akhir_pekan,
    color='#ff7f0e',
    s=120,
    marker='^',
    label='Akhir Pekan'
)

ax.set_title("Perbandingan Penjualan Es Krim")
ax.set_xlabel("Suhu (°C)")
ax.set_ylabel("Penjualan")
ax.legend()
ax.grid(True, alpha=0.4)

st.pyplot(fig)


# DATA ANALISIS 

st.subheader("3. Analisis Berdasarkan Jenis Es Krim")

data = {
    'Suhu': [20, 22, 24, 26, 28, 30, 32, 34, 36],
    'Penjualan_Cokelat': [50, 60, 70, 80, 90, 100, 110, 120, 130],
    'Penjualan_Vanila': [60, 70, 80, 90, 100, 110, 120, 130, 140],
    'Penjualan_Stroberi': [40, 50, 60, 70, 80, 90, 100, 110, 120],
    'Kelembapan': [60, 65, 70, 75, 80, 85, 90, 95, 100]
}

df = pd.DataFrame(data)

jenis_eskrim = st.selectbox(
    "Pilih Jenis Es Krim:",
    ["Cokelat", "Vanila", "Stroberi"]
)

if jenis_eskrim == "Cokelat":
    penjualan_pilih = df["Penjualan_Cokelat"]
elif jenis_eskrim == "Vanila":
    penjualan_pilih = df["Penjualan_Vanila"]
else:
    penjualan_pilih = df["Penjualan_Stroberi"]

st.subheader("Tabel Data")
st.dataframe(df)


# SCATTER COLOR GRADIENT

fig, ax = plt.subplots()
scatter = ax.scatter(
    df["Suhu"],
    penjualan_pilih,
    c=df["Kelembapan"],
    s=130,
    cmap="plasma",
    marker='o',
    edgecolor='black',
    alpha=0.85
)

ax.set_title(f"Penjualan {jenis_eskrim} terhadap Suhu & Kelembapan")
ax.set_xlabel("Suhu (°C)")
ax.set_ylabel(f"Penjualan Es Krim {jenis_eskrim}")

cbar = fig.colorbar(scatter)
cbar.set_label("Kelembapan (%)")

ax.grid(True, linestyle=':')

st.pyplot(fig)


# KESIMPULAN

st.subheader("4. Kesimpulan")
st.write(
    f"Hasil visualisasi menunjukkan bahwa peningkatan suhu "
    f"cenderung meningkatkan penjualan es krim. "
    f"Selain itu, faktor kelembapan juga memiliki kontribusi "
    f"terhadap penjualan es krim jenis **{jenis_eskrim}**."
)
