import streamlit as st
import pandas as pd
from identitas import show_identity

# Sidebar identitas
show_identity()

st.title("📊 Visualisasi - Bar Chart (Data Penduduk Miskin Indonesia)")

st.subheader("📥 Memuat Data dari File Lokal")

try:
    # Baca file Excel dengan header di baris pertama yang benar
    file_path = "Jumlah Penduduk Miskin Provinsi 2020-2025.xlsx"
    df = pd.read_excel(file_path, header=1)  # header=1 agar baris ke-2 jadi judul kolom

    # Ganti nama kolom agar lebih mudah dipakai
    df.rename(columns={df.columns[0]: "Provinsi"}, inplace=True)

    # Ganti tanda '-' dengan NaN, lalu ubah kolom angka menjadi numerik
    df = df.replace("-", pd.NA)
    df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

    st.success("✅ Data berhasil dimuat!")
    st.dataframe(df)

    # Pilih tahun (kolom angka)
    tahun = st.selectbox("📅 Pilih Tahun:", df.columns[1:])

    st.subheader("📈 Visualisasi Bar Chart")
    st.bar_chart(df.set_index("Provinsi")[tahun])

except Exception as e:
    st.error(f"Gagal memuat data: {e}")



