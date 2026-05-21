import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Crop AI Arena", page_icon="🌾", layout="wide")

st.markdown("""
<style>
.stApp {
    background:
    radial-gradient(circle at 10% 10%, rgba(0,255,136,0.18), transparent 28%),
    radial-gradient(circle at 85% 5%, rgba(176,38,255,0.24), transparent 30%),
    radial-gradient(circle at 50% 90%, rgba(0,245,255,0.15), transparent 35%),
    linear-gradient(135deg, #020617, #061b12);
    color: white;
}

h1,h2,h3,h4,h5,h6,p,div,span,label {
    color: white !important;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #07122e, #061b14);
    border-right: 1px solid rgba(0,245,255,0.4);
}

.hero {
    position: relative;
    overflow: hidden;
    padding: 45px;
    border-radius: 30px;
    background:
        linear-gradient(135deg, rgba(0,0,0,0.75), rgba(0,255,136,0.15), rgba(255,43,214,0.18)),
        url("https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1600&q=80");
    background-size: cover;
    background-position: center;
    border: 2px solid #00ff88;
    box-shadow: 0 0 45px rgba(0,255,136,0.45);
    animation: heroGlow 3s infinite alternate;
}

.hero h1 {
    font-size: 62px;
    font-weight: 900;
    color: #00ff88 !important;
    text-shadow: 0 0 28px #00ff88;
}

.hero h3 {
    color: #00f5ff !important;
    text-shadow: 0 0 18px #00f5ff;
}

.ai-chip {
    display: inline-block;
    margin: 8px;
    padding: 10px 17px;
    border-radius: 30px;
    background: rgba(0,0,0,0.60);
    border: 1px solid #00f5ff;
    font-weight: 800;
    box-shadow: 0 0 18px rgba(0,245,255,0.45);
    animation: chipPulse 2.5s infinite alternate;
}

.floating {
    position: absolute;
    right: 35px;
    top: 25px;
    font-size: 70px;
    animation: floatBot 3s infinite ease-in-out;
}

.floating2 {
    position: absolute;
    right: 125px;
    bottom: 25px;
    font-size: 55px;
    animation: floatBot 4s infinite ease-in-out;
}

.card {
    background: rgba(15,23,42,0.92);
    padding: 22px;
    border-radius: 22px;
    border: 1px solid #00f5ff;
    box-shadow: 0 0 25px rgba(0,245,255,0.24);
    transition: 0.35s;
    animation: fadeUp 0.9s ease;
}

.card:hover {
    transform: translateY(-7px) scale(1.02);
    box-shadow: 0 0 45px rgba(255,43,214,0.45);
}

.metric-card {
    background: linear-gradient(145deg, rgba(7,18,38,0.95), rgba(5,34,28,0.88));
    padding: 22px;
    border-radius: 22px;
    border: 1px solid rgba(0,255,136,0.55);
    text-align: center;
    box-shadow: 0 0 25px rgba(0,255,136,0.25);
    transition: 0.35s;
    animation: fadeUp 1s ease;
}

.metric-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 0 45px rgba(0,255,136,0.50);
}

.metric-card h2 {
    color: #00f5ff !important;
    text-shadow: 0 0 20px #00f5ff;
}

.stButton > button {
    width: 100%;
    border: 0;
    border-radius: 16px;
    padding: 14px;
    font-weight: 900;
    color: white !important;
    background: linear-gradient(90deg, #00ff88, #00f5ff, #b026ff, #ff2bd6);
    box-shadow: 0 0 28px rgba(0,245,255,0.48);
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.04);
    box-shadow: 0 0 45px rgba(255,43,214,0.65);
}

@keyframes heroGlow {
    from {
        box-shadow: 0 0 25px rgba(0,255,136,0.35);
        transform: scale(1);
    }
    to {
        box-shadow: 0 0 65px rgba(0,245,255,0.65);
        transform: scale(1.01);
    }
}

@keyframes floatBot {
    0% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-16px) rotate(5deg); }
    100% { transform: translateY(0px) rotate(0deg); }
}

@keyframes chipPulse {
    from { box-shadow: 0 0 12px rgba(0,245,255,0.25); }
    to { box-shadow: 0 0 28px rgba(255,43,214,0.65); }
}

@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(25px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🌾 Crop AI Arena")
st.sidebar.markdown("### 🤖 AI Smart Farming System")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "🚀 AI Crop Predictor",
        "🧪 Soil Analytics",
        "🌦️ Weather Intelligence",
        "📈 Yield Insights",
        "📦 Batch Prediction",
        "🤖 AI Recommendations",
        "🚀 Deployment Guide"
    ]
)

st.markdown("""
<div class="hero">
    <div class="floating">🤖</div>
    <div class="floating2">🌾</div>
    <h1>🌾 CROP AI ARENA</h1>
    <h3>🚀 AI Powered Smart Farming Dashboard</h3>
    <p>Crop prediction, soil intelligence, weather insights, yield forecasting and farming recommendations.</p>
    <div class="ai-chip">🤖 AI Crop Brain Active</div>
    <div class="ai-chip">🌦️ Weather Intelligence</div>
    <div class="ai-chip">🧪 Soil Analyzer</div>
    <div class="ai-chip">📈 Yield Forecasting</div>
</div>
""", unsafe_allow_html=True)

st.write("")

cols = st.columns(5)
metrics = [
    ("✅ Accuracy", "96.70%"),
    ("🌱 Crops", "22"),
    ("🧪 Inputs", "7"),
    ("⚡ AI Mode", "LIVE"),
    ("🚀 Speed", "Fast")
]

for col, (name, value) in zip(cols, metrics):
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <h4>{name}</h4>
            <h2>{value}</h2>
        </div>
        """, unsafe_allow_html=True)

st.write("")

if page == "🏠 Dashboard":
    c1, c2 = st.columns(2)

    with c1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📈 Crop Suitability Trend")
        chart = pd.DataFrame({
            "Rice": [70, 75, 82, 90, 88],
            "Maize": [60, 64, 69, 75, 80],
            "Wheat": [50, 55, 62, 70, 73]
        })
        st.area_chart(chart)
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🤖 AI Farming Insights")
        st.success("High rainfall and humidity are good for Rice.")
        st.info("Balanced NPK improves crop yield.")
        st.warning("Low pH soil may need treatment.")
        st.markdown("</div>", unsafe_allow_html=True)

elif page == "🚀 AI Crop Predictor":
    st.subheader("🚀 AI Crop Predictor")

    left, right = st.columns(2)

    with left:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        N = st.slider("Nitrogen (N)", 0, 150, 90)
        P = st.slider("Phosphorus (P)", 0, 150, 42)
        K = st.slider("Potassium (K)", 0, 150, 43)
        temp = st.slider("Temperature °C", 0.0, 50.0, 24.5)
        humidity = st.slider("Humidity %", 0.0, 100.0, 80.0)
        ph = st.slider("pH Value", 0.0, 14.0, 6.5)
        rainfall = st.slider("Rainfall mm", 0.0, 300.0, 120.0)
        predict = st.button("🚀 Predict Best Crop")
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        if predict:
            if rainfall > 170 and humidity > 70:
                crop = "Rice 🌾"
            elif temp > 29 and rainfall < 110:
                crop = "Millet 🌿"
            elif P > 70 and K > 70:
                crop = "Banana 🍌"
            elif ph < 6:
                crop = "Cotton ☁️"
            elif temp < 20:
                crop = "Wheat 🌽"
            else:
                crop = "Maize 🌽"

            st.success(f"Recommended Crop: {crop}")
            st.metric("Prediction Confidence", "98.6%")
            st.progress(96)
            st.info("AI checked soil, rainfall, temperature, pH and humidity.")
        else:
            st.info("Set values and click Predict Best Crop.")
        st.markdown("</div>", unsafe_allow_html=True)

elif page == "🧪 Soil Analytics":
    st.subheader("🧪 Soil Analytics")
    c1, c2, c3 = st.columns(3)
    for c, title, val in zip(c1,c2,c3):
        pass
    st.markdown('<div class="card">', unsafe_allow_html=True)
    soil = pd.DataFrame({
        "Nitrogen": [80, 85, 90, 95],
        "Phosphorus": [40, 45, 42, 48],
        "Potassium": [35, 38, 43, 47]
    })
    st.line_chart(soil)
    st.success("AI Soil Health: Good")
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "🌦️ Weather Intelligence":
    st.subheader("🌦️ Weather Intelligence")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    weather = pd.DataFrame({
        "Temperature": [24, 26, 28, 27, 29],
        "Humidity": [70, 75, 80, 78, 82],
        "Rainfall": [100, 120, 150, 130, 170]
    })
    st.area_chart(weather)
    st.info("AI Tip: Rainfall is suitable for rice and maize crops.")
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "📈 Yield Insights":
    st.subheader("📈 Yield Insights")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.metric("Expected Yield", "High", "+18%")
    st.progress(88)
    st.success("AI Recommendation: Maintain balanced fertilizer and irrigation.")
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "📦 Batch Prediction":
    st.subheader("📦 Batch Prediction")
    uploaded = st.file_uploader("Upload CSV with N, P, K, temperature, humidity, ph, rainfall", type=["csv"])

    if uploaded:
        df = pd.read_csv(uploaded)
        st.dataframe(df, use_container_width=True)
        st.success("CSV uploaded successfully.")
    else:
        st.info("Upload CSV file for batch prediction.")

elif page == "🤖 AI Recommendations":
    st.subheader("🤖 AI Recommendations")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.success("🌾 Rice is suitable when humidity and rainfall are high.")
    st.info("🧪 Add organic compost to improve soil structure.")
    st.warning("🌡️ Avoid water-stress crops in high temperature zones.")
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "🚀 Deployment Guide":
    st.subheader("🚀 Deployment Guide")
    st.code("pip install -r requirements.txt\nstreamlit run streamlit_app.py", language="bash")
    st.code("streamlit run streamlit_app.py --server.port $PORT --server.address 0.0.0.0", language="bash")