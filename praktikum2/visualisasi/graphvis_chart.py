import streamlit as st
from graphviz import Digraph
from identitas import show_identity

# Sidebar identitas kelompok
show_identity()

st.title("🕸️ Visualisasi - Graphviz Chart")

st.write("Contoh representasi hubungan antar wilayah berdasarkan regional Indonesia:")

# Buat grafik relasi antar wilayah
dot = Digraph()

# Tambahkan node (wilayah besar)
dot.node("Sumatera", "Pulau Sumatera")
dot.node("Jawa", "Pulau Jawa")
dot.node("Kalimantan", "Pulau Kalimantan")
dot.node("Sulawesi", "Pulau Sulawesi")
dot.node("Papua", "Pulau Papua")

# Tambahkan hubungan antar wilayah
dot.edge("Sumatera", "Jawa")
dot.edge("Jawa", "Kalimantan")
dot.edge("Kalimantan", "Sulawesi")
dot.edge("Sulawesi", "Papua")
dot.edge("Sumatera", "Papua")

# Tampilkan diagram di Streamlit
st.graphviz_chart(dot)

