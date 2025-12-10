import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time

st.title("📊 Monitoring Real-time Sensor")

# Generate simulated sensor data
def generate_sensor_data():
    current_time = datetime.now()
    
    # Simulate sensor readings with some randomness
    base_ph = 6.5 + np.random.normal(0, 0.1)
    base_tds = 800 + np.random.normal(0, 20)
    base_water_level = 70 + np.random.normal(0, 2)
    
    return {
        "timestamp": current_time,
        "pH": round(max(4.0, min(8.0, base_ph)), 2),
        "TDS": round(max(200, min(1500, base_tds)), 0),
        "Water_Level": round(max(0, min(100, base_water_level)), 1),
        "Temperature": round(25 + np.random.normal(0, 0.5), 1),
        "Humidity": round(65 + np.random.normal(0, 2), 1)
    }

# Dashboard layout
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="sensor-card">', unsafe_allow_html=True)
    st.metric("🌡️ pH", "6.5", delta="+0.1", delta_color="normal")
    st.progress(0.75)
    st.caption("Ideal: 5.5-6.5")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="sensor-card">', unsafe_allow_html=True)
    st.metric("💧 TDS", "850 ppm", delta="-15", delta_color="inverse")
    st.progress(0.85)
    st.caption("Target: 800-1200 ppm")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="sensor-card">', unsafe_allow_html=True)
    st.metric("🚰 Water Level", "75%", delta="-2%")
    st.progress(0.75)
    st.caption("Minimum: 50%")
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="sensor-card">', unsafe_allow_html=True)
    st.metric("🌡️ Suhu", "26.5°C", delta="+0.5")
    st.progress(0.65)
    st.caption("Ideal: 25-28°C")
    st.markdown('</div>', unsafe_allow_html=True)

# Real-time update toggle
real_time = st.checkbox("🔄 Real-time Update", value=True)

# Charts
tab1, tab2, tab3 = st.tabs(["📈 Grafik Sensor", "📋 Data History", "⚙️ Pengaturan Alarm"])

with tab1:
    # Generate historical data
    time_points = [datetime.now() - timedelta(minutes=i) for i in range(60, -1, -1)]
    ph_data = [6.5 + np.random.normal(0, 0.2) for _ in range(61)]
    tds_data = [800 + np.random.normal(0, 30) for _ in range(61)]
    
    # Create plotly figure
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=time_points, y=ph_data,
        mode='lines',
        name='pH',
        line=dict(color='green', width=2)
    ))
    
    fig.add_trace(go.Scatter(
        x=time_points, y=[x/100 for x in tds_data],  # Scale for better visualization
        mode='lines',
        name='TDS (scaled)',
        line=dict(color='blue', width=2),
        yaxis='y2'
    ))
    
    fig.update_layout(
        title='Trend pH dan TDS (1 Jam Terakhir)',
        yaxis=dict(title='pH', range=[4, 9]),
        yaxis2=dict(title='TDS (ppm)', overlaying='y', side='right'),
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Water level gauge
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=75,
        title={'text': "Water Level"},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 50], 'color': "red"},
                {'range': [50, 80], 'color': "yellow"},
                {'range': [80, 100], 'color': "green"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 75
            }
        }
    ))
    
    st.plotly_chart(fig_gauge, use_container_width=True)

with tab2:
    st.subheader("📋 Data Historis Sensor")
    
    # Generate sample historical data
    dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
    historical_data = pd.DataFrame({
        'Tanggal': dates,
        'pH': np.random.uniform(5.8, 7.0, 30),
        'TDS': np.random.uniform(700, 1300, 30),
        'Water_Level': np.random.uniform(60, 95, 30),
        'Suhu': np.random.uniform(24, 28, 30)
    })
    
    st.dataframe(historical_data.round(2))
    
    # Export data
    csv = historical_data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Data CSV",
        data=csv,
        file_name="sensor_data.csv",
        mime="text/csv"
    )
    
    # Filter data
    st.subheader("🔍 Filter Data")
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Dari tanggal", dates[0])
    with col2:
        end_date = st.date_input("Sampai tanggal", dates[-1])

with tab3:
    st.subheader("⚙️ Pengaturan Alarm & Notifikasi")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Threshold Sensor**")
        ph_min = st.number_input("pH Minimum", 4.0, 7.0, 5.5)
        ph_max = st.number_input("pH Maksimum", 7.0, 9.0, 6.5)
        
        tds_min = st.number_input("TDS Minimum (ppm)", 0, 2000, 600)
        tds_max = st.number_input("TDS Maksimum (ppm)", 0, 3000, 1200)
        
        water_min = st.slider("Water Level Minimum (%)", 0, 100, 50)
    
    with col2:
        st.write("**Notifikasi**")
        email_notif = st.checkbox("📧 Email Notifikasi", value=True)
        telegram_notif = st.checkbox("💬 Telegram Bot", value=True)
        whatsapp_notif = st.checkbox("📱 WhatsApp", value=False)
        
        if email_notif:
            email = st.text_input("Email untuk notifikasi", "user@example.com")
        
        st.write("**Interval Check**")
        interval = st.select_slider(
            "Cek setiap",
            options=["5 menit", "15 menit", "30 menit", "1 jam", "3 jam", "6 jam"]
        )
    
    if st.button("💾 Simpan Pengaturan", type="primary"):
        st.success("Pengaturan alarm berhasil disimpan!")
        
        # Show current settings
        st.info(f"""
        **Settings Saved:**
        - pH Range: {ph_min} - {ph_max}
        - TDS Range: {tds_min} - {tds_max} ppm
        - Water Level Alert: < {water_min}%
        - Check Interval: {interval}
        """)

# Manual override section
with st.expander("🔧 Manual Control"):
    st.write("Kontrol manual perangkat hidroponik")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        pump_status = st.toggle("Pompa Nutrisi", value=True)
        if pump_status:
            st.success("Pompa ON")
        else:
            st.error("Pompa OFF")
    
    with col2:
        light_status = st.toggle("Lampu LED", value=True)
        if light_status:
            st.success("Lampu ON")
        else:
            st.error("Lampu OFF")
    
    with col3:
        fan_status = st.toggle("Kipas", value=False)
        if fan_status:
            st.success("Kipas ON")
        else:
            st.error("Kipas OFF")
    
    # Manual nutrient adjustment
    st.subheader("Penyesuaian Nutrisi Manual")
    ph_adjust = st.select_slider("Adjust pH", options=["Asam (pH Down)", "Netral", "Basa (pH Up)"])
    if ph_adjust != "Netral":
        amount = st.slider(f"Jumlah {ph_adjust} (ml)", 0.0, 10.0, 1.0, 0.5)
        if st.button(f"Tambahkan {amount}ml"):
            st.success(f"{amount}ml {ph_adjust} ditambahkan!")
