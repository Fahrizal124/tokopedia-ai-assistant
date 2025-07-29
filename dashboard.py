import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI Assistant Analisis Bisnis Seller Tokopedia", page_icon="🤖", layout="wide")
BASE_URL = "http://localhost:8000"

@st.cache_data(ttl=60)
def fetch_analysis():
    return requests.get(f"{BASE_URL}/shop/analysis", timeout=60).json()

def main():
    data = fetch_analysis()
    shop_data = data["shop_data"]
    ai_insights = data["ai_insights"]
    hist = data["historical_data"]

    st.title("🤖 AI Assistant Analisis Bisnis Seller Tokopedia")

    # KPI
    st.write(f"**💰 Revenue:** Rp {shop_data['revenue']:,} | **📦 Orders:** {shop_data['orders']} | **🎯 Conversion Rate:** {shop_data['conversion_rate']}%")

    # AI Insights
    st.subheader("🧠 AI Insights")
    for insight in ai_insights:
        st.info(insight)

    # Chart
    df = pd.DataFrame(hist)
    st.write("### 📈 Revenue Trend")
    st.plotly_chart(px.line(df, x="month", y="revenue", title="Revenue Bulanan"))

    # Chat
    st.subheader("💬 Tanya AI Bisnis Tokomu:")
    question = st.text_input("Tanya sesuatu...")
    if question:
        answer = requests.post(f"{BASE_URL}/chat", json={"question": question}, timeout=60).json()["answer"]
        st.success("🤖 " + answer)

if __name__ == "__main__":
    main()
