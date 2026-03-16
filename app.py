import streamlit as st
import joblib
import pandas as pd

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Mobile Price Predictor",
    page_icon="📱",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

body {
background: linear-gradient(135deg,#1f4037,#99f2c8);
}

.main {
background-color: #f8f9fa;
padding: 20px;
border-radius: 10px;
}

.title {
text-align:center;
font-size:45px;
font-weight:700;
color:#2c3e50;
}

.subtitle{
text-align:center;
font-size:18px;
color:gray;
margin-bottom:30px;
}

.stButton>button {
background: linear-gradient(90deg,#11998e,#38ef7d);
color:white;
font-size:18px;
border:none;
border-radius:10px;
padding:12px 25px;
}

.result-card{
background:white;
padding:30px;
border-radius:15px;
box-shadow:0px 6px 20px rgba(0,0,0,0.1);
text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------

model = joblib.load("Mobile_Prices.joblib")
df = pd.read_csv("Flipkart_Mobiles.csv")

# ---------------- HEADER ----------------

st.markdown('<p class="title">📱 Flipkart Mobile Price Predictor</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Machine Learning Model to Predict Mobile Prices</p>', unsafe_allow_html=True)

st.divider()

# ---------------- SIDEBAR ----------------

st.sidebar.title("📊 Mobile Specifications")

brand = st.sidebar.selectbox("Select Brand", df["Brand"].unique())

df_brand = df[df["Brand"] == brand]

mobile_model = st.sidebar.selectbox("Select Model", df_brand["Model"].unique())

df_model = df_brand[df_brand["Model"] == mobile_model]

color = st.sidebar.selectbox("Select Color", df_model["Color"].unique())

df_color = df_model[df_model["Color"] == color]

memory = st.sidebar.selectbox("Select Memory", df_color["Memory"].unique())

df_memory = df_color[df_color["Memory"] == memory]

storage = st.sidebar.selectbox("Select Storage", df_memory["Storage"].unique())

rating = st.sidebar.selectbox("Select Rating", df["Rating"].unique())

# ---------------- PREDICTION SECTION ----------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("📱 Selected Configuration")

    st.write(f"**Brand:** {brand}")
    st.write(f"**Model:** {mobile_model}")
    st.write(f"**Color:** {color}")
    st.write(f"**Memory:** {memory}")
    st.write(f"**Storage:** {storage}")
    st.write(f"**Rating:** {rating}")

with col2:

    st.subheader("💡 Prediction")

    if st.button("Predict Price"):

        input_df = pd.DataFrame({
            "Brand":[brand],
            "Model":[mobile_model],
            "Color":[color],
            "Memory":[memory],
            "Storage":[storage],
            "Rating":[rating]
        })

        prediction = model.predict(input_df)

        st.markdown(f"""
        <div class="result-card">
        <h2>💰 Predicted Mobile Price</h2>
        <h1 style="color:#27ae60;">₹ {prediction[0]:,.0f}</h1>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# ---------------- FOOTER ----------------

st.markdown(
"""
<center>
Built with ❤️ using Python, Scikit-Learn & Streamlit  
</center>
""",
unsafe_allow_html=True
)