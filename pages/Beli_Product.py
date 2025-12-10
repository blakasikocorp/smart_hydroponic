import streamlit as st

st.title("🛒 Beli Produk Smart Hydroponic")

# Product database
products = [
    {
        "id": 1,
        "name": "Smart Hydroponic Kit Basic",
        "price": 1500000,
        "description": "Paket lengkap untuk pemula, termasuk 12 lubang tanam, sensor pH, TDS, dan aplikasi monitoring",
        "features": ["Sensor pH & TDS", "App Monitoring", "Pompa otomatis", "Lampu LED 18W"],
        "image": "assets/images/kit-basic.jpg",
        "category": "starter-kit",
        "stock": 15
    },
    {
        "id": 2,
        "name": "Sensor pH Digital",
        "price": 350000,
        "description": "Sensor pH digital dengan akurasi ±0.01, tahan air, kalibrasi mudah",
        "features": ["Akurasi tinggi", "Tahan air IP67", "Auto temperature compensation"],
        "image": "assets/images/sensor-ph.jpg",
        "category": "sensor",
        "stock": 42
    },
    {
        "id": 3,
        "name": "Nutrisi AB Mix Premium",
        "price": 120000,
        "description": "Nutrisi lengkap untuk semua fase tumbuh, 1kg A + 1kg B",
        "features": ["Untuk semua tanaman", "Mudah larut", "pH stabil"],
        "image": "assets/images/nutrisi.jpg",
        "category": "consumable",
        "stock": 87
    },
    {
        "id": 4,
        "name": "Smart Hydroponic Pro",
        "price": 3500000,
        "description": "Sistem hidroponik otomatis lengkap dengan IoT, bisa tanam 36 tanaman",
        "features": ["IoT Controller", "Auto dosing", "Cloud monitoring", "Backup power"],
        "image": "assets/images/kit-pro.jpg",
        "category": "starter-kit",
        "stock": 8
    }
]

# Filter by category
st.sidebar.subheader("🔍 Filter Produk")
categories = ["Semua", "starter-kit", "sensor", "consumable", "accessories"]
selected_category = st.sidebar.selectbox("Kategori", categories)

price_range = st.sidebar.slider("Rentang Harga (Rp)", 0, 5000000, (0, 5000000))

# Shopping cart in session state
if 'cart' not in st.session_state:
    st.session_state.cart = []

# Display products
st.subheader("🛍️ Katalog Produk")

# Filter products
filtered_products = products
if selected_category != "Semua":
    filtered_products = [p for p in products if p["category"] == selected_category]
filtered_products = [p for p in filtered_products if price_range[0] <= p["price"] <= price_range[1]]

# Product grid
cols = st.columns(2)
for idx, product in enumerate(filtered_products):
    with cols[idx % 2]:
        with st.container():
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            
            # Product image (placeholder)
            st.image("https://via.placeholder.com/300x200", caption=product["name"])
            
            st.subheader(product["name"])
            st.write(f"**Rp {product['price']:,}**")
            st.write(product["description"])
            
            # Features as badges
            for feature in product["features"][:2]:
                st.caption(f"✓ {feature}")
            
            # Add to cart
            col1, col2 = st.columns([3, 1])
            with col1:
                quantity = st.number_input(
                    "Jumlah",
                    min_value=1,
                    max_value=product["stock"],
                    value=1,
                    key=f"qty_{product['id']}",
                    label_visibility="collapsed"
                )
            with col2:
                if st.button("🛒", key=f"cart_{product['id']}"):
                    # Add to cart
                    cart_item = {
                        "id": product["id"],
                        "name": product["name"],
                        "price": product["price"],
                        "quantity": quantity
                    }
                    st.session_state.cart.append(cart_item)
                    st.success(f"{quantity} {product['name']} ditambahkan ke keranjang!")
            
            st.caption(f"Stok: {product['stock']} unit")
            st.markdown('</div>', unsafe_allow_html=True)

# Shopping Cart Sidebar
with st.sidebar:
    st.divider()
    st.subheader("🛒 Keranjang Belanja")
    
    if st.session_state.cart:
        total = 0
        for item in st.session_state.cart:
            st.write(f"• {item['name']}")
            st.write(f"  {item['quantity']} x Rp {item['price']:,}")
            total += item['quantity'] * item['price']
        
        st.divider()
        st.write(f"**Total: Rp {total:,}**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💳 Checkout"):
                st.info("Fitur checkout dalam pengembangan")
        with col2:
            if st.button("🗑️ Kosongkan"):
                st.session_state.cart = []
                st.rerun()
    else:
        st.write("Keranjang kosong")

# Checkout page
st.divider()
st.subheader("💳 Proses Checkout")

with st.form("checkout_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Data Pengiriman**")
        name = st.text_input("Nama Lengkap")
        address = st.text_area("Alamat Lengkap")
        phone = st.text_input("Nomor Telepon")
        
    with col2:
        st.write("**Metode Pengiriman**")
        shipping = st.selectbox(
            "Kurir",
            ["JNE", "J&T", "SiCepat", "GoSend", "Ambil di tempat"]
        )
        
        st.write("**Metode Pembayaran**")
        payment = st.selectbox(
            "Pembayaran",
            ["Transfer Bank", "QRIS", "COD", "Kredit"]
        )
    
    # Order summary
    st.write("**Ringkasan Pesanan**")
    if st.session_state.cart:
        summary_df = pd.DataFrame(st.session_state.cart)
        st.dataframe(summary_df)
        total = sum(item['quantity'] * item['price'] for item in st.session_state.cart)
        st.write(f"**Total Pembayaran: Rp {total:,}**")
    else:
        st.warning("Keranjang belanja kosong")
    
    agree = st.checkbox("Saya menyetujui syarat dan ketentuan")
    
    if st.form_submit_button("Buat Pesanan", type="primary"):
        if agree and st.session_state.cart:
            st.success("🎉 Pesanan berhasil dibuat!")
            st.balloons()
            st.info("Silakan lakukan pembayaran dan konfirmasi melalui WhatsApp: 0812-3456-7890")
            # Clear cart after order
            st.session_state.cart = []
        else:
            st.error("Silakan isi semua data dan setujui syarat & ketentuan")

# Customer reviews
st.divider()
st.subheader("⭐ Ulasan Pelanggan")

reviews = [
    {"name": "Budi Santoso", "rating": 5, "comment": "Sistemnya sangat mudah dirakit, tanaman tumbuh subur!", "date": "2024-01-15"},
    {"name": "Sari Dewi", "rating": 4, "comment": "Sensor pH akurat, app monitoring sangat membantu", "date": "2024-01-10"},
    {"name": "Agus Prasetyo", "rating": 5, "comment": "Paket komplit, cocok untuk pemula seperti saya", "date": "2024-01-05"}
]

for review in reviews:
    stars = "⭐" * review["rating"]
    st.write(f"**{review['name']}** {stars}")
    st.write(f"{review['comment']}")
    st.caption(review["date"])
    st.divider()
