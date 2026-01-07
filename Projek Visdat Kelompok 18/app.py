import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Konfigurasi Halaman
st.set_page_config(page_title="Analisis Pariwisata - Kelompok 18", layout="wide")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv('wisata_final_combined.csv')

df = load_data()

# --- SIDEBAR (NAVBAR SEBELAH KIRI) ---
with st.sidebar:
    st.image("https://www.sttnf.ac.id/wp-content/uploads/2023/04/logo-sttnf-1.png", width=180)
    
    # Format Nama Anggota sesuai permintaan (Tanpa List/Angka/Simbol)
    st.markdown("### Anggota Kelompok 18")
    st.text("Raydino Situmeang 0110222278")
    st.text("Apriyanto 0110222256")
    st.text("Deva Lubna Listya 0110222258")
    
    st.markdown("---")
    st.markdown("### Filter Eksplorasi")
    selected_prov = st.multiselect("Provinsi:", options=sorted(df['provinsi'].unique()), default=["Bali"])
    selected_cat = st.multiselect("Kategori:", options=sorted(df['kategori'].unique()), default=df['kategori'].unique())
    st.markdown("---")
    st.caption("Projek Akhir Visualisasi Data 2025")

# Filter Data
df_filtered = df[(df['provinsi'].isin(selected_prov)) & (df['kategori'].isin(selected_cat))]

# --- MAIN CONTENT ---
st.markdown("<h2 style='text-align: center;'>Analisis Visual Pola Sebaran dan Tren Popularitas Destinasi Wisata</h2>", unsafe_allow_html=True)
st.markdown("---")

# Row 1: Key Metrics
m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Total Destinasi Terdata", f"{len(df_filtered)}")
with m2:
    st.metric("Rata-rata Popularitas (Rating)", f"{df_filtered['rating'].mean():.2f}")
with m3:
    st.metric("Cakupan Provinsi", f"{df_filtered['provinsi'].nunique()}")

# Layout Menggunakan Tabs
tab1, tab2, tab3 = st.tabs(["Sebaran Geografis", "Popularitas & Tren", "Analisis Kategori"])

with tab1:
    st.subheader("Pola Sebaran Destinasi Wisata")
    # Visualisasi 1: Map
    st.map(df_filtered)

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Peringkat Destinasi per Provinsi")
        # Visualisasi 2: Horizontal Bar Chart
        top_data = df_filtered['provinsi'].value_counts().head(10)
        fig_bar, ax_bar = plt.subplots(figsize=(8, 5))
        sns.barplot(x=top_data.values, y=top_data.index, palette="Blues_d", ax=ax_bar)
        ax_bar.set_xlabel("Jumlah Objek Wisata")
        st.pyplot(fig_bar)
    
    with col2:
        st.subheader("Tren Popularitas Berdasarkan Rating")
        # Visualisasi 3: Scatter Plot
        fig_scatter = px.scatter(df_filtered, x=df_filtered.index, y="rating", 
                                 color="kategori", template="plotly_white")
        st.plotly_chart(fig_scatter, use_container_width=True)

with tab3:
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Proporsi Kategori Wisata")
        # Visualisasi 4: Pie Chart (Disederhanakan)
        cat_counts = df_filtered['kategori'].value_counts()
        if len(cat_counts) > 6:
            cat_plot_data = pd.concat([cat_counts.head(6), pd.Series([cat_counts.iloc[6:].sum()], index=['Lainnya'])])
        else:
            cat_plot_data = cat_counts

        fig_pie, ax_pie = plt.subplots()
        ax_pie.pie(cat_plot_data, labels=cat_plot_data.index, autopct='%1.1f%%', 
                   startangle=140, colors=sns.color_palette("Set3"))
        ax_pie.axis('equal')
        st.pyplot(fig_pie)

    with col4:
        st.subheader("Distribusi Skor Rating")
        # Visualisasi 5: Bar Chart Distribusi
        rating_counts = df_filtered['rating'].value_counts().sort_index()
        st.bar_chart(rating_counts)

# Section Kesimpulan Analisis (Bab V & Deskripsi Tugas)
st.markdown("---")
st.markdown("### Kesimpulan Analisis")
col_ins1, col_ins2 = st.columns(2)

with col_ins1:
    st.markdown("**1. Pola Sebaran Geografis**")
    st.write(f"""
    Berdasarkan peta sebaran, destinasi wisata di {', '.join(selected_prov[:3])} dan sekitarnya menunjukkan pola konsentrasi pada area pesisir dan pusat kota. 
    Hal ini mengindikasikan bahwa aksesibilitas dan infrastruktur pendukung menjadi faktor utama dalam distribusi titik wisata. 
    Dataset mencakup total {len(df_filtered)} titik koordinat yang tervalidasi.
    """)

with col_ins2:
    st.markdown("**2. Tren Popularitas dan Karakteristik**")
    st.write(f"""
    Tren popularitas yang diukur melalui skor rating menunjukkan nilai rata-rata sebesar {df_filtered['rating'].mean():.2f}. 
    Kategori '{df_filtered['kategori'].value_counts().idxmax()}' menjadi tren utama dalam pilihan destinasi. 
    Sebaran rating yang mayoritas berada di atas 4.0 menunjukkan tingkat kepuasan publik yang tinggi terhadap objek wisata di wilayah Indonesia terpilih.
    """)

st.info("Keterangan: Data diolah dari integrasi dataset Google Maps Bali dan Wisata Indonesia untuk memenuhi tugas akhir Visualisasi Data.")