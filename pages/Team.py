import streamlit as st

st.title("👥 Team Development")

st.write("""
Tim kami terdiri dari ahli di bidang pertanian modern, teknologi IoT, dan software development
yang berdedikasi menciptakan solusi hidroponik pintar untuk Indonesia.
""")

# Team members
team_members = [
    {
        "name": "Dr. Ahmad Fauzi",
        "role": "Agricultural Expert",
        "education": "PhD in Plant Biotechnology, IPB University",
        "expertise": ["Hidroponik", "Nutrisi Tanaman", "Plant Pathology"],
        "image": "assets/images/team1.jpg",
        "linkedin": "https://linkedin.com"
    },
    {
        "name": "Sarah Wijaya, S.T.",
        "role": "IoT Engineer",
        "education": "Electrical Engineering, ITB",
        "expertise": ["Sensor System", "Microcontroller", "PCB Design"],
        "image": "assets/images/team2.jpg",
        "linkedin": "https://linkedin.com"
    },
    {
        "name": "Rizky Pratama",
        "role": "Software Developer",
        "education": "Computer Science, Universitas Indonesia",
        "expertise": ["Web Development", "Mobile App", "Cloud Computing"],
        "image": "assets/images/team3.jpg",
        "linkedin": "https://linkedin.com"
    },
    {
        "name": "Diana Sari, M.Si.",
        "role": "Business Development",
        "education": "Master of Management, Universitas Gadjah Mada",
        "expertise": ["Marketing", "Business Strategy", "Customer Relations"],
        "image": "assets/images/team4.jpg",
        "linkedin": "https://linkedin.com"
    }
]

# Display team in columns
cols = st.columns(2)
for idx, member in enumerate(team_members):
    with cols[idx % 2]:
        with st.container():
            # Placeholder image
            st.image("https://via.placeholder.com/200x200", width=150)
            
            st.subheader(member["name"])
            st.write(f"**{member['role']}**")
            st.write(member["education"])
            
            st.write("**Keahlian:**")
            for skill in member["expertise"]:
                st.caption(f"• {skill}")
            
            st.button(f"📧 Kontak {member['name'].split()[0]}", key=f"contact_{idx}")

# Company timeline
st.divider()
st.subheader("📅 Perjalanan Kami")

timeline_data = [
    {"year": "2022", "event": "Research & Development awal, prototype pertama"},
    {"year": "2023 Q1", "event": "Launch Smart Hydroponic Kit versi 1.0"},
    {"year": "2023 Q3", "event": "Penghargaan Inovasi Pertanian Kementan"},
    {"year": "2024", "event": "Ekspansi ke 5 kota besar di Indonesia"},
    {"year": "2025", "event": "Target: Go international ke ASEAN countries"}
]

for item in timeline_data:
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f"**{item['year']}**")
    with col2:
        st.write(item["event"])

# Career opportunities
st.divider()
st.subheader("💼 Bergabung dengan Kami")

with st.expander("Lihat Lowongan Pekerjaan"):
    jobs = [
        {"title": "IoT Engineer", "location": "Bandung", "type": "Full-time"},
        {"title": "Agricultural Researcher", "location": "Bogor", "type": "Contract"},
        {"title": "Sales Marketing", "location": "Jakarta", "type": "Full-time"},
        {"title": "Mobile App Developer", "location": "Remote", "type": "Full-time"}
    ]
    
    for job in jobs:
        st.write(f"**{job['title']}**")
        st.write(f"📍 {job['location']} | 📝 {job['type']}")
        if st.button("Apply", key=f"apply_{job['title']}"):
            st.info("Silakan kirim CV ke: careers@smarthydroponic.id")
        st.divider()

# Partners section
st.divider()
st.subheader("🤝 Mitra Kami")

partners = [
    {"name": "Kementerian Pertanian", "logo": "assets/images/kementan.png"},
    {"name": "IPB University", "logo": "assets/images/ipb.png"},
    {"name": "IoT Indonesia", "logo": "assets/images/iot.png"},
    {"name": "AgriTech Startup", "logo": "assets/images/agritech.png"}
]

partner_cols = st.columns(4)
for idx, partner in enumerate(partners):
    with partner_cols[idx]:
        st.image("https://via.placeholder.com/100x50", caption=partner["name"])

# Contact team
st.divider()
st.subheader("📞 Hubungi Tim Development")

col1, col2 = st.columns(2)

with col1:
    st.write("**Untuk Technical Support:**")
    st.write("📧 tech@smarthydroponic.id")
    st.write("📱 +62 812-3456-7891")
    
with col2:
    st.write("**Untuk Partnership:**")
    st.write("📧 partnership@smarthydroponic.id")
    st.write("📱 +62 812-3456-7892")

st.info("""
**Jam Operasional Support:**
Senin - Jumat: 09.00 - 17.00 WIB
Sabtu: 09.00 - 12.00 WIB
""")
