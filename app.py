import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.graph_objects as go

# Konfigurasi halaman
st.set_page_config(
    page_title="Smart Hydroponic",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Custom
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2E8B57;
        text-align: center;
        margin-bottom: 1rem;
    }
    .card {
        padding: 1.5rem;
        border-radius: 10px;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .sensor-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
    .product-card {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 1rem;
        transition: transform 0.3s;
    }
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.image("assets/images/logo.png", width=150)  # Ganti dengan logo Anda
    st.title("🌱 Smart Hydroponic")
    
    menu = st.radio(
        "Navigasi Utama",
        ["🏠 Home", "📊 Monitoring", "🛒 Beli Produk", "👥 Team", "📞 Kontak"]
    )
    
    st.divider()
    
    # Quick stats di sidebar
    st.subheader("📈 Status Sistem")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("pH", "6.5", "0.2")
    with col2:
        st.metric("TDS", "800 ppm", "-50")
    
    # Toggle untuk dark/light mode
    dark_mode = st.toggle("🌙 Dark Mode", value=False)
    
    st.divider()
    st.caption("© 2024 Smart Hydroponic. All rights reserved.")

# Main content berdasarkan menu
if menu == "🏠 Home":
    # Homepage akan di-handle oleh pages/1_🏠_Home.py
    # Tapi kita bisa buat preview di sini
    st.title("🌿 Selamat Datang di Smart Hydroponic")
    st.write("""
    Platform lengkap untuk monitoring dan manajemen sistem hidroponik pintar.
    Navigasi ke halaman spesifik melalui menu di sidebar.
    """)
    
elif menu == "📊 Monitoring":
    import pages.monitoring  # Akan dibuat terpisah
    
elif menu == "🛒 Beli Produk":
    import pages.beli_product  # Akan dibuat terpisah
    
elif menu == "👥 Team":
    import pages.team  # Akan dibuat terpisah
    
elif menu == "📞 Kontak":
    st.title("📞 Hubungi Kami")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📧 Form Kontak")
        with st.form("contact_form"):
            name = st.text_input("Nama Lengkap")
            email = st.text_input("Email")
            message = st.text_area("Pesan")
            submitted = st.form_submit_button("Kirim Pesan")
            if submitted:
                st.success("Pesan berhasil dikirim! Kami akan menghubungi Anda dalam 1x24 jam.")
    
    with col2:
        st.subheader("📍 Info Kontak")
        st.write("""
        **Alamat Kantor:**  
        Jl. Teknologi No. 123, Bandung, Jawa Barat
        
        **Telepon:**  
        (022) 1234-5678
        
        **Email:**  
        info@smarthydroponic.id
        
        **Jam Operasional:**  
        Senin - Jumat: 08.00 - 17.00  
        Sabtu: 08.00 - 12.00
        """)
        
        st.subheader("🌐 Sosial Media")
        social_cols = st.columns(4)
        with social_cols[0]:
            st.button("📘 Facebook")
        with social_cols[1]:
            st.button("📷 Instagram")
        with social_cols[2]:
            st.button("🐦 Twitter")
        with social_cols[3]:
            st.button("📺 YouTube")
