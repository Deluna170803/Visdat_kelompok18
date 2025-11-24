import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd # Import pandas untuk tabel data

# ==============================================================================
# Informasi Kelompok (Semua Nama Tampil Jelas)
# ==============================================================================
KELOMPOK = {
    "Raydino Situmeang": "0110222278",
    "Apriyanto": "0110222256",
    "Deva Lubna Listya": "0110222258"
}

# ==============================================================================
# Data Sample
# ==============================================================================
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = np.array([10, 20, 15, 25, 30, 45, 40, 50, 60, 55, 65, 70])
product_B_sales = np.array([5, 10, 8, 15, 18, 20, 22, 30, 25, 35, 40, 45])

# Warna Custom
COLOR_A = '#1f77b4' 
COLOR_B = '#ff7f0e'

# ==============================================================================
# FUNGSI PLOT KREATIF (Customized Line Plot)
# ==============================================================================
def create_enhanced_line_plot():
    # Menggunakan Style Modern
    plt.style.use('seaborn-v0_8-darkgrid') 
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Plot Garis
    ax.plot(months, product_A_sales, label='Product A (Unggul)', color=COLOR_A, 
            linewidth=3, marker='o', markersize=6)
    ax.plot(months, product_B_sales, label='Product B (Pesaing)', color=COLOR_B, 
            linewidth=3, marker='s', markersize=6)
    
    # Fitur Kreatif: Area Berarsir untuk Kesenjangan Penjualan (Sales Gap)
    ax.fill_between(months, product_A_sales, product_B_sales, 
                    where=(product_A_sales > product_B_sales), 
                    interpolate=True, 
                    color=COLOR_A, alpha=0.2, 
                    label='Kesenjangan Penjualan A > B')
    
    # Fitur Kreatif: Anotasi Puncak Penjualan
    max_A_sales = product_A_sales.max()
    max_A_index = product_A_sales.argmax()
    max_A_month = months[max_A_index]
    
    ax.annotate(f'PUNCAK A: {max_A_sales}', 
                xy=(max_A_month, max_A_sales), 
                xytext=(max_A_index - 0.5, max_A_sales + 5),
                arrowprops=dict(facecolor='red', shrink=0.05, width=1, headwidth=8),
                fontsize=10, fontweight='bold', color='red')

    ax.set_title('Customized Line Plot: Tren Penjualan Produk Per Bulan', fontsize=14, fontweight='bold')
    ax.set_xlabel('Bulan', fontsize=11)
    ax.set_ylabel('Jumlah Penjualan', fontsize=11)
    ax.legend(loc='upper left', frameon=True, shadow=True, fancybox=True)
    
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    return fig

# ==============================================================================
# FUNGSI PLOT STANDAR (Dari Modul Asli)
# ==============================================================================

def line_plot_basic():
    plt.style.use('default') 
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, color=COLOR_A)
    ax.set_title('Penjualan Produk A Per Bulan (Line Plot Standar)')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    return fig

def subplots_plot():
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    
    axs[0].plot(months, product_A_sales, color=COLOR_A, marker='o')
    axs[1].plot(months, product_B_sales, color=COLOR_B, marker='s')
    
    axs[0].set_title('Penjualan Produk A')
    axs[1].set_title('Penjualan Produk B')
    axs[1].set_xlabel('Bulan')
    
    axs[0].set_ylabel('Jumlah Penjualan')
    axs[1].set_ylabel('Jumlah Penjualan')
    
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    return fig


# ==============================================================================
# STREAMLIT LAYOUT UTAMA
# ==============================================================================

st.set_page_config(layout="wide", page_title="Modul 3: Line Plot Kreatif")
st.title("Visualisasi Data Penjualan Produk")
st.caption("Modul 3: Line Plot | Visualisasi Data | **Kelompok Raydino, Apriyanto, & Deva**")

# --- Sidebar Informasi Kelompok (Semua Nama Tampil) ---
st.sidebar.header("Informasi Kelompok")
st.sidebar.subheader("Anggota:")
for nama, nim in KELOMPOK.items():
    # Menampilkan nama dengan format yang rapi di sidebar
    st.sidebar.markdown(f"**{nama}** (NIM: `{nim}`)")

# --- Dropdown Pilihan Visualisasi ---
st.sidebar.header("Pilihan Visualisasi")
visualization_option = st.sidebar.selectbox(
    "Pilih Tipe Grafik",
    ("Customized Line Plot", 
     "Line Plot Sederhana", 
     "Subplot (Perbandingan A vs B)")
)

# --- Tampilkan Grafik Berdasarkan Pilihan ---
if visualization_option == "Customized Line Plot":
    st.header("1. Customized Line Plot")
    st.success("Analisis Cepat: Produk A mendominasi penjualan sepanjang tahun, dengan puncaknya mencapai 70 unit di bulan Desember. Area berarsir menunjukkan kesenjangan penjualan.")
    st.pyplot(create_enhanced_line_plot())
    
elif visualization_option == "Line Plot Sederhana":
    st.header("2. Line Plot Produk A (Dasar)")
    st.info("Visualisasi dasar untuk melihat tren tunggal Produk A.")
    st.pyplot(line_plot_basic())

elif visualization_option == "Subplot (Perbandingan A vs B)":
    st.header("3. Subplot: Perbandingan Penjualan Produk A dan B")
    st.info("Membandingkan dua tren penjualan secara terpisah dengan skala yang sama.")
    st.pyplot(subplots_plot())

st.markdown("---")

# --- Fitur Kreatif Tambahan: Dataframe/Heatmap Data Mentah ---
st.subheader("Data Mentah Penjualan")
df_sales = pd.DataFrame({
    'Bulan': months,
    'Product A': product_A_sales,
    'Product B': product_B_sales
})

# Menggunakan style.background_gradient untuk membuat mini heatmap pada data
st.dataframe(df_sales.style.background_gradient(cmap='Blues', subset=['Product A'])
                         .background_gradient(cmap='Oranges', subset=['Product B']),
             width=600)