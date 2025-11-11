import streamlit as st
import pandas as pd
import altair as alt
from identitas import show_identity

# Sidebar identitas kelompok
show_identity()

st.title("📈 Visualisasi Interaktif - Line Chart (Tren Penduduk Miskin Indonesia)")

st.write("Grafik ini menampilkan perubahan jumlah penduduk miskin per provinsi dari tahun 2020 hingga 2025.")

# Load data
try:
    df = pd.read_excel("Jumlah Penduduk Miskin Provinsi 2020-2025.xlsx")
    df.columns = df.iloc[0]  # gunakan baris pertama sebagai header
    df = df.drop(0).reset_index(drop=True)
    df = df.rename(columns={df.columns[0]: "Provinsi"})

    # ubah format data menjadi long (tahun, nilai)
    df_long = df.melt(id_vars=["Provinsi"], var_name="Tahun", value_name="Jumlah (Ribu Jiwa)")
    df_long["Jumlah (Ribu Jiwa)"] = pd.to_numeric(df_long["Jumlah (Ribu Jiwa)"], errors="coerce")

    # pilih beberapa provinsi untuk interaksi
    provinsi_pilihan = st.multiselect("Pilih Provinsi:", df["Provinsi"].tolist(), ["Aceh", "Jawa Barat", "Papua"])

    if provinsi_pilihan:
        df_filtered = df_long[df_long["Provinsi"].isin(provinsi_pilihan)]

        chart = (
            alt.Chart(df_filtered)
            .mark_line(point=True)
            .encode(
                x=alt.X("Tahun:N", title="Tahun"),
                y=alt.Y("Jumlah (Ribu Jiwa):Q", title="Jumlah Penduduk Miskin (Ribu Jiwa)"),
                color="Provinsi:N",
                tooltip=["Provinsi", "Tahun", "Jumlah (Ribu Jiwa)"]
            )
            .interactive()
            .properties(height=500, width=800, title="Tren Penduduk Miskin per Provinsi")
        )

        st.altair_chart(chart, use_container_width=True)
    else:
        st.info("Silakan pilih minimal satu provinsi untuk melihat grafik.")

except Exception as e:
    st.error(f"Gagal memuat data: {e}")



