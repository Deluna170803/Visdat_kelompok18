import streamlit as st
import pandas as pd
import plotly.express as px

# KONFIGURASI HALAMAN
st.set_page_config(
    page_title="Analisis Wisata Bali",
    page_icon="🗺️",
    layout="wide"
)

# JUDUL DASHBOARD
st.markdown("""
<h2 style='text-align:center;'>
ANALISIS VISUAL POLA SEBARAN DAN TREN POPULARITAS DESTINASI WISATA DI BALI
</h2>
<h4 style='text-align:center;'>
Menggunakan Data Google Maps dan Wisata Indonesia
</h4>
<hr>
""", unsafe_allow_html=True)

# LOAD & DATA CLEANING
@st.cache_data
def load_data():
    df = pd.read_csv("wisata_siap_visualisasi.csv")

    # Data Cleaning
    df = df.dropna(subset=["Provinsi", "Latitude", "Longitude"])
    df["Provinsi"] = df["Provinsi"].astype(str).str.title()

    # FOKUS PENELITIAN: BALI
    df = df[df["Provinsi"] == "Bali"]

    df["Nama"] = df["Nama"].astype(str)
    df["Kategori"] = df["Kategori"].astype(str).str.title()
    df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")

    return df

df = load_data()

# SIDEBAR
st.sidebar.title("🔎 Filter Analisis")
st.sidebar.caption("Wilayah Penelitian: Provinsi Bali")

# >>> IDENTITAS KELOMPOK (TEPAT DI BAWAH WILAYAH PENELITIAN)
st.sidebar.markdown("""
<div style="font-size:13px; line-height:1.6; margin-bottom:15px;">
<b>Kelompok 18</b><br>
110222256 – Apriyanto<br>
110222278 – Raydino Situmeang<br>
110222258 – Deva Lubna Listya
</div>
""", unsafe_allow_html=True)

# FILTER
search = st.sidebar.text_input("Cari Nama Destinasi")

kategori_list = ["Semua"] + sorted(df["Kategori"].unique().tolist())
selected_kat = st.sidebar.multiselect(
    "Kategori Wisata",
    kategori_list,
    default=["Semua"]
)

# FILTER DATA
df_display = df.copy()

if search:
    df_display = df_display[df_display["Nama"].str.contains(search, case=False)]

if "Semua" not in selected_kat:
    df_display = df_display[df_display["Kategori"].isin(selected_kat)]

# METRIC RINGKASAN
m1, m2, m3 = st.columns(3)
m1.metric("Total Destinasi", len(df_display))
m2.metric("Jumlah Kategori", df_display["Kategori"].nunique())
m3.metric(
    "Rata-rata Rating",
    round(df_display["Rating"].dropna().mean(), 2)
)

# TABS VISUALISASI
tab1, tab2, tab3 = st.tabs([
    "🗺️ Pola Sebaran",
    "📊 Tren Popularitas",
    "📋 Data Destinasi"
])

# VISUAL 1 – POLA SEBARAN (SCATTER MAP)
with tab1:
    st.subheader("Pola Sebaran Destinasi Wisata di Pulau Bali")

    fig_map = px.scatter_mapbox(
        df_display,
        lat="Latitude",
        lon="Longitude",
        hover_name="Nama",
        hover_data=["Kategori", "Rating"],
        color="Kategori",
        zoom=9,
        height=600,
        mapbox_style="carto-positron"
    )

    st.plotly_chart(fig_map, use_container_width=True)
    st.info(
        "Peta ini memperlihatkan pola sebaran destinasi wisata di Provinsi Bali "
        "berdasarkan kategori, yang menunjukkan konsentrasi wisata pada wilayah tertentu."
    )

# VISUAL 2–5 – TREN POPULARITAS
with tab2:
    c1, c2 = st.columns(2)

    # VISUAL 2 – BAR CHART
    with c1:
        st.write("### Jumlah Destinasi per Kategori")
        fig_bar = px.bar(
            df_display["Kategori"].value_counts(),
            labels={"value": "Jumlah Destinasi", "index": "Kategori"}
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    # VISUAL 3 – PIE CHART
    with c2:
        st.write("### Komposisi Destinasi Berdasarkan Kategori")
        fig_pie = px.pie(
            df_display,
            names="Kategori",
            hole=0.4
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    c3, c4 = st.columns(2)

    # VISUAL 4 – HISTOGRAM
    with c3:
        st.write("### Distribusi Rating Destinasi")
        fig_hist = px.histogram(
            df_display[df_display["Rating"] > 0],
            x="Rating",
            nbins=10
        )
        st.plotly_chart(fig_hist, use_container_width=True)

    # VISUAL 5 – BOXPLOT
    with c4:
        st.write("### Variasi Rating per Kategori")
        fig_box = px.box(
            df_display[df_display["Rating"] > 0],
            x="Kategori",
            y="Rating",
            color="Kategori"
        )
        st.plotly_chart(fig_box, use_container_width=True)

# TAB DATA
with tab3:
    st.dataframe(df_display, use_container_width=True)

# KESIMPULAN
st.divider()
top_kat = df_display["Kategori"].value_counts().idxmax()

st.success(
    f"Hasil analisis menunjukkan bahwa kategori **{top_kat}** "
    "memiliki jumlah destinasi terbanyak di Provinsi Bali. "
    "Pola sebaran destinasi wisata cenderung terkonsentrasi "
    "pada wilayah dengan tingkat popularitas yang tinggi."
)
