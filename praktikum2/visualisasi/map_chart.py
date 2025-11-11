import streamlit as st
import pandas as pd
import numpy as np
from identitas import show_identity

# Sidebar identitas kelompok
show_identity()

st.title("🗺️ Visualisasi - Map Chart (Peta Persebaran)")

st.write("Menampilkan peta persebaran provinsi di Indonesia (simulasi lokasi acak).")

# Muat data lokal
try:
    df = pd.read_excel("Jumlah Penduduk Miskin Provinsi 2020-2025.xlsx")
    df.columns = df.iloc[0]
    df = df.drop(0).reset_index(drop=True)
    df = df.rename(columns={df.columns[0]: "Provinsi"})

    # Tambahkan koordinat acak (simulasi)
    np.random.seed(42)
    df["lat"] = np.random.uniform(-10, 5, len(df))
    df["lon"] = np.random.uniform(95, 141, len(df))

    st.success("✅ Data berhasil dimuat!")

    # Tampilkan data di peta
    st.map(df[["lat", "lon"]])

except Exception as e:
    st.error(f"Gagal memuat data: {e}")
