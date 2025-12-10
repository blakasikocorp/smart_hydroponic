import streamlit as st

st.title("🏠 Homepage Smart Hydroponic")

# Tab untuk 3 bagian utama
tab1, tab2, tab3 = st.tabs(["🌱 Edukasi Hidroponik", "🔧 Tata Cara Merakit", "⚙️ Maintenance"])

with tab1:
    st.header("📚 Edukasi Tata Cara Menanam Hidroponik")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Persiapan Benih")
        st.write("""
        - Pilih benih berkualitas
        - Rendam benih 4-6 jam
        - Letakkan di media semai (rockwool)
        - Simpan di tempat gelap sampai berkecambah
        """)
        
        st.subheader("2. Sistem NFT (Nutrient Film Technique)")
        st.write("""
        - Sistem paling populer untuk sayuran daun
        - Larutan nutrisi dialirkan tipis
        - Akar mendapat oksigen cukup
        - Cocok untuk: selada, kangkung, pakcoy
        """)
    
    with col2:
        st.subheader("3. Nutrisi AB Mix")
        st.write("""
        - Gunakan nutrisi khusus hidroponik
        - Perbandingan A dan B sesuai fase
        - Vegetatif: N tinggi
        - Generatif: P dan K tinggi
        """)
        
        st.subheader("4. Pengaturan pH")
        st.write("""
        - pH ideal: 5.5 - 6.5
        - Cek setiap hari
        - Gunakan pH meter digital
        - Adjust dengan pH up/down
        """)
    
    # Video tutorial
    st.subheader("🎥 Video Tutorial")
    video_url = st.text_input("Masukkan URL video YouTube:", "https://www.youtube.com/watch?v=example")
    if video_url:
        st.video(video_url)

with tab2:
    st.header("🔧 Panduan Merakit Smart Hydroponic Kit")
    
    steps = [
        {
            "title": "Step 1: Persiapan Material",
            "items": ["Pipa PVC 3 inch", "Netpot", "Pompa air", "Timer", "Nutrisi AB Mix", "pH meter"]
        },
        {
            "title": "Step 2: Potong dan Rakit Pipa",
            "items": ["Potong pipa 1 meter", "Buat lubang untuk netpot", "Pasang end cap", "Buat kemiringan 3%"]
        },
        {
            "title": "Step 3: Instalasi Sistem Air",
            "items": ["Pasang pompa di reservoir", "Hubungkan selang", "Atur debit air 2L/menit", "Test kebocoran"]
        },
        {
            "title": "Step 4: Instalasi Sensor",
            "items": ["Pasang sensor pH", "Pasang sensor TDS", "Pasang sensor water level", "Hubungkan ke microcontroller"]
        },
        {
            "title": "Step 5: Programming",
            "items": ["Install Arduino IDE", "Upload kode monitoring", "Setup database", "Test semua sensor"]
        }
    ]
    
    for i, step in enumerate(steps, 1):
        with st.expander(f"Step {i}: {step['title']}"):
            for item in step['items']:
                st.write(f"✓ {item}")
            
            if i == 2:
                st.image("assets/images/rakit-pipa.jpg", caption="Contoh rakitan pipa")
            elif i == 4:
                st.image("assets/images/sensor-install.jpg", caption="Instalasi sensor")

with tab3:
    st.header("⚙️ Panduan Maintenance")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔄 Rutin Harian")
        daily_tasks = {
            "Cek pH larutan": "6.0 - 6.5",
            "Cek TDS/EC": "800-1200 ppm",
            "Cek volume air": "Minimal 70%",
            "Cek kebersihan": "Bersihkan kotoran",
            "Cek pertumbuhan": "Foto dokumentasi"
        }
        
        for task, target in daily_tasks.items():
            st.checkbox(f"{task}: **{target}**")
        
        st.subheader("🧼 Cleaning Schedule")
        cleaning = {
            "Setiap 2 minggu": "Bersihkan reservoir",
            "Setiap bulan": "Flushing sistem",
            "Setiap 3 bulan": "Ganti media tanam",
            "Setiap 6 bulan": "Kalibrasi sensor"
        }
        
        for when, what in cleaning.items():
            st.info(f"**{when}**: {what}")
    
    with col2:
        st.subheader("⚠️ Troubleshooting")
        
        problems = [
            ("Daun menguning", "Kekurangan nitrogen", "Tambah nutrisi A"),
            ("Pertumbuhan lambat", "Cahaya kurang", "Tambahkan lampu LED"),
            ("pH tidak stabil", "Buffer habis", "Ganti larutan nutrisi"),
            ("Pompa tidak bekerja", "Kabel longgar", "Cek koneksi power"),
            ("Sensor error", "Kotor/kering", "Bersihkan probe")
        ]
        
        for problem, cause, solution in problems:
            with st.expander(f"❌ {problem}"):
                st.write(f"**Penyebab**: {cause}")
                st.write(f"**Solusi**: {solution}")
        
        st.subheader("📊 Log Maintenance")
        log_date = st.date_input("Tanggal maintenance")
        log_activity = st.text_area("Aktivitas yang dilakukan")
        if st.button("Simpan Log"):
            st.success(f"Log {log_date} berhasil disimpan!")
