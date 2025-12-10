
import streamlit as st
import numpy as np
import time
import random

# =================== PAGE CONFIG ===================
st.set_page_config(
    page_title="HydroGrow - Hydroponic System",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =================== CUSTOM CSS ===================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;900&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #f0fdf4 0%, #d1fae5 50%, #a7f3d0 100%);
}

h1 {
    color: #065f46;
    font-weight: 900;
    text-align: center;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}

h2 {
    color: #047857;
    font-weight: 700;
    border-left: 5px solid #10b981;
    padding-left: 15px;
}

h3 {
    color: #059669;
    font-weight: 600;
}

.stButton > button {
    background: linear-gradient(135deg, #10b981, #059669);
    color: white;
    border-radius: 12px;
    border: none;
    font-weight: 700;
    padding: 0.7rem 2rem;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(16, 185, 129, 0.4);
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #064e3b, #065f46);
}

section[data-testid="stSidebar"] .stMarkdown {
    color: white;
}

.product-card {
    background: white;
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    border: 2px solid transparent;
}

.product-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 8px 25px rgba(16, 185, 129, 0.3);
    border-color: #10b981;
}

.monitoring-card {
    background: linear-gradient(135deg, #ffffff, #f0fdf4);
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    border-left: 5px solid #10b981;
}

.team-card {
    background: white;
    border-radius: 20px;
    padding: 1.5rem;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}

.team-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 8px 25px rgba(16, 185, 129, 0.3);
}

.contact-card {
    background: rgba(255,255,255,0.2);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 1.5rem;
    color: white;
    text-align: center;
    transition: all 0.3s ease;
}

.contact-card:hover {
    background: rgba(255,255,255,0.3);
    transform: scale(1.05);
}

.guide-card {
    background: linear-gradient(135deg, #ffffff, #f0fdf4);
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    border-top: 5px solid #10b981;
    height: 100%;
}
</style>
""", unsafe_allow_html=True)

# =================== SIDEBAR NAVIGATION ===================
st.sidebar.markdown("# 🌱 HydroGrow")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "📋 Navigation",
    ["🏠 Home", "📚 Guides", "🛒 Shop", "📊 Monitoring", "👥 Team", "📞 Contact"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🌿 About HydroGrow")
st.sidebar.info("""
Your complete hydroponic solution:
- Professional equipment
- Real-time monitoring
- Expert guidance
- Quality products
""")

# =================== HOME PAGE ===================
if page == "🏠 Home":
    # Hero Section
    st.markdown("""
    <div style='background: linear-gradient(135deg, #10b981, #059669); padding: 4rem 2rem; border-radius: 20px; text-align: center; color: white; margin-bottom: 2rem;'>
        <h1 style='color: white; font-size: 3.5rem; margin-bottom: 1rem;'>🌱 Welcome to HydroGrow</h1>
        <p style='font-size: 1.5rem; color: #d1fae5;'>Your Complete Hydroponic Solution</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div style='background: white; padding: 2rem; border-radius: 15px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1);'>
            <h2 style='color: #10b981; font-size: 2.5rem; margin: 0;'>500+</h2>
            <p style='color: #6b7280; margin: 0;'>Happy Customers</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: white; padding: 2rem; border-radius: 15px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1);'>
            <h2 style='color: #10b981; font-size: 2.5rem; margin: 0;'>50+</h2>
            <p style='color: #6b7280; margin: 0;'>Products</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background: white; padding: 2rem; border-radius: 15px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1);'>
            <h2 style='color: #10b981; font-size: 2.5rem; margin: 0;'>24/7</h2>
            <p style='color: #6b7280; margin: 0;'>Support</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style='background: white; padding: 2rem; border-radius: 15px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1);'>
            <h2 style='color: #10b981; font-size: 2.5rem; margin: 0;'>100%</h2>
            <p style='color: #6b7280; margin: 0;'>Organic</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Features Section
    st.markdown("## 🚀 Why Choose HydroGrow?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #ffffff, #f0fdf4); padding: 2rem; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 1rem;'>
            <h3 style='color: #059669;'>🌱 Complete Systems</h3>
            <p style='color: #4b5563;'>Professional hydroponic kits with everything you need to start growing immediately.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background: linear-gradient(135deg, #ffffff, #f0fdf4); padding: 2rem; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);'>
            <h3 style='color: #059669;'>📊 Smart Monitoring</h3>
            <p style='color: #4b5563;'>Real-time monitoring of pH, TDS, and water levels with automated alerts.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #ffffff, #f0fdf4); padding: 2rem; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 1rem;'>
            <h3 style='color: #059669;'>🎓 Expert Guidance</h3>
            <p style='color: #4b5563;'>Step-by-step tutorials and ongoing support from our team of experts.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background: linear-gradient(135deg, #ffffff, #f0fdf4); padding: 2rem; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);'>
            <h3 style='color: #059669;'>🌍 Eco-Friendly</h3>
            <p style='color: #4b5563;'>Sustainable farming that uses 90% less water than traditional methods.</p>
        </div>
        """, unsafe_allow_html=True)

# =================== GUIDES PAGE ===================
elif page == "📚 Guides":
    st.title("📚 Hydroponic Guides")
    st.markdown("### Learn everything about hydroponic farming")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='guide-card'>
            <div style='width: 60px; height: 60px; background: #10b981; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem;'>
                <span style='font-size: 2rem;'>🌱</span>
            </div>
            <h3 style='text-align: center; color: #059669;'>How to Plant</h3>
            <ul style='text-align: left; color: #4b5563;'>
                <li>Choose suitable seeds for hydroponics</li>
                <li>Prepare growing medium (rockwool/cocopeat)</li>
                <li>Germinate seeds in moist medium</li>
                <li>Transfer seedlings to net pots</li>
                <li>Monitor pH (5.5-6.5) and TDS (800-1200 ppm)</li>
                <li>Ensure adequate lighting (12-16 hours)</li>
                <li>Maintain proper nutrient balance</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='guide-card'>
            <div style='width: 60px; height: 60px; background: #3b82f6; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem;'>
                <span style='font-size: 2rem;'>📦</span>
            </div>
            <h3 style='text-align: center; color: #2563eb;'>Assembly Guide</h3>
            <ul style='text-align: left; color: #4b5563;'>
                <li>Prepare reservoir tank and water pump</li>
                <li>Install growing channels or towers</li>
                <li>Connect irrigation system with timer</li>
                <li>Setup grow lights at proper height</li>
                <li>Install pH and TDS sensors</li>
                <li>Test system before planting</li>
                <li>Calibrate all monitoring equipment</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='guide-card'>
            <div style='width: 60px; height: 60px; background: #8b5cf6; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem;'>
                <span style='font-size: 2rem;'>💧</span>
            </div>
            <h3 style='text-align: center; color: #7c3aed;'>Maintenance</h3>
            <ul style='text-align: left; color: #4b5563;'>
                <li>Check water level daily</li>
                <li>Clean reservoir every 2 weeks</li>
                <li>Replace nutrient solution regularly</li>
                <li>Clean pump filter weekly</li>
                <li>Inspect plants for pests/diseases</li>
                <li>Calibrate sensors monthly</li>
                <li>Prune and harvest regularly</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Video Tutorial Section
    st.markdown("## 🎥 Video Tutorials")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);'>
            <h3>Getting Started with Hydroponics</h3>
            <p style='color: #6b7280;'>Complete beginner's guide to setting up your first hydroponic system</p>
            <button style='background: #10b981; color: white; border: none; padding: 0.7rem 2rem; border-radius: 8px; cursor: pointer;'>▶️ Watch Now</button>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);'>
            <h3>Advanced Growing Techniques</h3>
            <p style='color: #6b7280;'>Master advanced methods for maximum yield and plant health</p>
            <button style='background: #10b981; color: white; border: none; padding: 0.7rem 2rem; border-radius: 8px; cursor: pointer;'>▶️ Watch Now</button>
        </div>
        """, unsafe_allow_html=True)

# =================== SHOP PAGE ===================
elif page == "🛒 Shop":
    st.title("🛒 Hydroponic Products")
    st.markdown("### Everything you need to start your hydroponic journey")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Products
    st.markdown("## 🌿 Hydroponic Systems & Equipment")
    
    products = [
        {"name": "Starter Hydroponic Kit", "price": "Rp 1,250,000", "icon": "🌱", "desc": "Complete kit for beginners"},
        {"name": "NFT System Pro", "price": "Rp 2,500,000", "icon": "💧", "desc": "Professional NFT growing system"},
        {"name": "LED Grow Light", "price": "Rp 850,000", "icon": "💡", "desc": "Full spectrum 100W"},
        {"name": "pH Meter Digital", "price": "Rp 350,000", "icon": "📊", "desc": "Accurate pH measurement"},
        {"name": "Nutrient Solution A+B", "price": "Rp 175,000", "icon": "🧪", "desc": "Complete plant nutrition"},
        {"name": "Net Pots Set (50pcs)", "price": "Rp 125,000", "icon": "🪴", "desc": "Quality net pots"}
    ]
    
    cols = st.columns(3)
    for idx, product in enumerate(products):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class='product-card'>
                <div style='font-size: 4rem; text-align: center;'>{product['icon']}</div>
                <h3 style='text-align: center;'>{product['name']}</h3>
                <p style='text-align: center; color: #6b7280;'>{product['desc']}</p>
                <div style='display: flex; justify-content: space-between; align-items: center; margin-top: 1rem;'>
                    <span style='font-size: 1.5rem; font-weight: bold; color: #10b981;'>{product['price']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"🛒 Buy Now", key=f"product_{idx}"):
                st.success(f"✅ {product['name']} added to cart!")
            st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Seeds Section
    st.markdown("## 🌾 Seeds & Seedlings")
    st.markdown("### Premium quality seeds for optimal growth")
    
    seeds = [
        {"name": "Lettuce Seeds", "price": "Rp 25,000", "icon": "🥬", "type": "Leafy Green"},
        {"name": "Tomato Seeds", "price": "Rp 35,000", "icon": "🍅", "type": "Fruit"},
        {"name": "Strawberry Seeds", "price": "Rp 45,000", "icon": "🍓", "type": "Fruit"},
        {"name": "Spinach Seeds", "price": "Rp 20,000", "icon": "🌿", "type": "Leafy Green"},
        {"name": "Basil Seeds", "price": "Rp 30,000", "icon": "🌿", "type": "Herb"},
        {"name": "Cucumber Seeds", "price": "Rp 28,000", "icon": "🥒", "type": "Fruit"}
    ]
    
    cols = st.columns(3)
    for idx, seed in enumerate(seeds):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class='product-card'>
                <div style='font-size: 4rem; text-align: center;'>{seed['icon']}</div>
                <h3 style='text-align: center;'>{seed['name']}</h3>
                <p style='text-align: center; color: #6b7280;'>{seed['type']}</p>
                <div style='display: flex; justify-content: space-between; align-items: center; margin-top: 1rem;'>
                    <span style='font-size: 1.5rem; font-weight: bold; color: #10b981;'>{seed['price']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"🛒 Buy Now", key=f"seed_{idx}"):
                st.success(f"✅ {seed['name']} added to cart!")
            st.markdown("<br>", unsafe_allow_html=True)

# =================== MONITORING PAGE ===================
elif page == "📊 Monitoring":
    st.title("📊 Real-Time Monitoring")
    st.markdown("### Live sensor data from your hydroponic system")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Create placeholder for real-time updates
    ph_placeholder = st.empty()
    tds_placeholder = st.empty()
    water_placeholder = st.empty()
    
    # Simulate real-time data
    ph_value = round(5.5 + random.random() * 1.5, 1)
    tds_value = int(800 + random.random() * 200)
    water_value = int(70 + random.random() * 25)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class='monitoring-card'>
            <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;'>
                <h3 style='margin: 0;'>🧪 pH Level</h3>
                <span style='background: #10b981; color: white; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.8rem;'>Live</span>
            </div>
            <div style='text-align: center;'>
                <div style='font-size: 3.5rem; font-weight: bold; color: #3b82f6;'>{ph_value}</div>
                <div style='color: #6b7280; margin-bottom: 1rem;'>pH</div>
                <div style='background: #e5e7eb; height: 8px; border-radius: 10px; overflow: hidden;'>
                    <div style='background: linear-gradient(to right, #60a5fa, #3b82f6); height: 100%; width: {(ph_value/14)*100}%; transition: width 0.5s;'></div>
                </div>
                <p style='margin-top: 1rem; color: #6b7280; font-size: 0.9rem;'>Optimal: 5.5 - 6.5</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='monitoring-card'>
            <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;'>
                <h3 style='margin: 0;'>📊 TDS</h3>
                <span style='background: #10b981; color: white; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.8rem;'>Live</span>
            </div>
            <div style='text-align: center;'>
                <div style='font-size: 3.5rem; font-weight: bold; color: #8b5cf6;'>{tds_value}</div>
                <div style='color: #6b7280; margin-bottom: 1rem;'>ppm</div>
                <div style='background: #e5e7eb; height: 8px; border-radius: 10px; overflow: hidden;'>
                    <div style='background: linear-gradient(to right, #a78bfa, #8b5cf6); height: 100%; width: {(tds_value/2000)*100}%; transition: width 0.5s;'></div>
                </div>
                <p style='margin-top: 1rem; color: #6b7280; font-size: 0.9rem;'>Optimal: 800 - 1200 ppm</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class='monitoring-card'>
            <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;'>
                <h3 style='margin: 0;'>💧 Water Level</h3>
                <span style='background: #10b981; color: white; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.8rem;'>Live</span>
            </div>
            <div style='text-align: center;'>
                <div style='font-size: 3.5rem; font-weight: bold; color: #06b6d4;'>{water_value}%</div>
                <div style='color: #6b7280; margin-bottom: 1rem;'>Capacity</div>
                <div style='background: #e5e7eb; height: 8px; border-radius: 10px; overflow: hidden;'>
                    <div style='background: linear-gradient(to right, #22d3ee, #06b6d4); height: 100%; width: {water_value}%; transition: width 0.5s;'></div>
                </div>
                <p style='margin-top: 1rem; color: #6b7280; font-size: 0.9rem;'>Refill when below 30%</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Alert Section
    st.markdown("## 🔔 System Alerts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if ph_value < 5.5 or ph_value > 6.5:
            st.warning(f"⚠️ pH level ({ph_value}) is outside optimal range!")
        else:
            st.success(f"✅ pH level ({ph_value}) is optimal")
        
        if tds_value < 800 or tds_value > 1200:
            st.warning(f"⚠️ TDS ({tds_value} ppm) is outside optimal range!")
        else:
            st.success(f"✅ TDS ({tds_value} ppm) is optimal")
    
    with col2:
        if water_value < 30:
            st.error(f"🚨 Water level ({water_value}%) is critically low! Refill immediately!")
        elif water_value < 50:
            st.warning(f"⚠️ Water level ({water_value}%) is low. Consider refilling soon.")
        else:
            st.success(f"✅ Water level ({water_value}%) is adequate")
    
    # Auto-refresh button
    if st.button("🔄 Refresh Data"):
        st.rerun()

# =================== TEAM PAGE ===================
elif page == "👥 Team":
    st.title("👥 Our Development Team")
    st.markdown("### Meet the experts behind HydroGrow")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    team = [
        {"name": "Rasyid Irvan M.", "role": "Project Lead", "photo": "https://raw.githubusercontent.com/rasyidmaulana19/RasyidClass01Night/main/Image/rasyid.jpeg", "color": "#10b981"},
        {"name": "Luthfi Ilham P.", "role": "Frontend Engineer", "photo": "https://raw.githubusercontent.com/rasyidmaulana19/RasyidClass01Night/main/Image/luthfi.jpeg", "color": "#3b82f6"},
        {"name": "Andrian Ramadhan", "role": "IoT Specialist", "photo": "https://raw.githubusercontent.com/rasyidmaulana19/RasyidClass01Night/main/Image/andrian.jpeg", "color": "#8b5cf6"},
        {"name": "Restu Imam F.", "role": "Data Analyst", "photo": "https://raw.githubusercontent.com/rasyidmaulana19/RasyidClass01Night/main/Image/restu.jpeg", "color": "#06b6d4"},
        {"name": "Ahmad Fauzi", "role": "Backend Developer", "photo": "https://via.placeholder.com/200/10b981/ffffff?text=AF", "color": "#f59e0b"},
        {"name": "Siti Nurhaliza", "role": "UI/UX Designer", "photo": "https://via.placeholder.com/200/ec4899/ffffff?text=SN", "color": "#ec4899"},
        {"name": "Budi Santoso", "role": "Hardware Engineer", "photo": "https://via.placeholder.com/200/6366f1/ffffff?text=BS", "color": "#6366f1"},
        {"name": "Dewi Lestari", "role": "Marketing Lead", "photo": "https://via.placeholder.com/200/14b8a6/ffffff?text=DL", "color": "#14b8a6"},
        {"name": "Eko Prasetyo", "role": "Quality Assurance", "photo": "https://via.placeholder.com/200/f97316/ffffff?text=EP", "color": "#f97316"}
    ]
    
    cols = st.columns(3)
    for idx, member in enumerate(team):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class='team-card'>
                <img src='{member["photo"]}' style='width: 150px; height: 150px; border-radius: 50%; object-fit: cover; border: 4px solid {member["color"]}; margin-bottom: 1rem;'/>
                <h3 style='margin: 0.5rem 0;'>{member["name"]}</h3>
                <p style='color: #6b7280; margin-bottom: 1rem;'>{member["role"]}</p>
                <span style='background: {member["color"]}; color: white; padding: 0.4rem 1rem; border-radius: 20px; font-size: 0.85rem;'>Team Member</span>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
