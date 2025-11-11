import streamlit as st
import pandas as pd
from identitas import show_identity

# Sidebar identitas
show_identity()

st.title("📈 Visualisasi - Area Chart (Data Penduduk Miskin Indonesia)")

try:
    # Baca data dari file Excel
    df = pd.read_excel("Jumlah Penduduk Miskin Provinsi 2020-2025.xlsx", header=1)
    df.rename(columns={df.columns[0]: "Provinsi"}, inplace=True)
    df = df.replace("-", pd.NA)
    df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors="coerce")

    st.success("✅ Data berhasil dimuat!")
    st.dataframe(df)

    st.subheader("📊 Area Chart per Tahun")
    st.area_chart(df.set_index("Provinsi"))

except Exception as e:
    st.error(f"Gagal memuat data: {e}")




