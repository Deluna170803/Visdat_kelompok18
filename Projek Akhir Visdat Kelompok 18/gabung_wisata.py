import pandas as pd

file_bali = 'dataset_tempat_wisata_bali_cleaned.csv'
file_indo = 'wisata_indonesia_final.csv'

try:
    # 1. Load Data
    df_bali = pd.read_csv(file_bali)
    df_indo = pd.read_csv(file_indo)

    # 2. Seleksi & Transformasi Kolom Bali
    # Kita tambahkan kolom 'provinsi' secara manual untuk data Bali
    df_bali_sel = df_bali[['nama', 'kategori', 'kabupaten_kota', 'rating', 'latitude', 'longitude']].copy()
    df_bali_sel.columns = ['Nama', 'Kategori', 'Kota_Kabupaten', 'Rating', 'Latitude', 'Longitude']
    df_bali_sel['Provinsi'] = 'Bali' 

    # 3. Seleksi & Transformasi Kolom Indonesia
    # Karena tidak ada 'rating', kita buat kolom Rating dengan nilai 0.0
    df_indo_sel = df_indo[['nama_wisata', 'kategori', 'kota_kabupaten', 'provinsi', 'latitude', 'longitude']].copy()
    df_indo_sel.columns = ['Nama', 'Kategori', 'Kota_Kabupaten', 'Provinsi', 'Latitude', 'Longitude']
    df_indo_sel['Rating'] = 0.0 

    # 4. Gabungkan Data (Concatenate)
    # Langkah ini untuk memastikan jumlah data minimal 1.000 baris 
    df_final = pd.concat([df_bali_sel, df_indo_sel], ignore_index=True)

    # 5. Data Cleaning [cite: 15]
    df_final = df_final.drop_duplicates()
    df_final = df_final.dropna(subset=['Nama', 'Kategori']) # Pastikan nama & kategori tidak kosong

    # 6. Simpan Hasil Akhir
    df_final.to_csv('wisata_siap_visualisasi.csv', index=False)
    
    print("-" * 30)
    print(f"BERHASIL DISATUKAN!")
    print(f"Jumlah baris data: {len(df_final)}")
    print("File 'wisata_siap_visualisasi.csv' telah dibuat.")
    print("-" * 30)

except Exception as e:
    print(f"Terjadi kesalahan saat penggabungan: {e}")