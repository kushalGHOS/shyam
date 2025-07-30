import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Trader Portfolio - Shyam Sundar Kr Singh", layout="wide")

# ---- HEADER ----
st.markdown("<h1 style='text-align: center; color: #0099ff;'>📈 Shyam Sundar Kr Singh - Professional Trader Portfolio</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Quantitative Analyst | Futures & Crypto Trader | Algo Strategist</p>", unsafe_allow_html=True)
st.markdown("---")

# ---- ABOUT ----
with st.container():
    st.markdown("### 👋 About Me")
    st.markdown("""
    Hello! I'm **Shyam**, a result-oriented trader with extensive experience in **futures**, **crypto**, and **equities**.  
    I build data-driven trading systems and emphasize consistent performance, risk management, and discipline.
    """)

# ---- STRATEGY ALLOCATION PIE CHART ----
with st.container():
    st.markdown("### 📊 Strategy Allocation")
    labels = ['Futures', 'Crypto', 'Intraday', 'Swing', 'Risk Management']
    sizes = [30, 25, 20, 15, 10]
    colors = ['#4fc3f7', '#ffb74d', '#aed581', '#9575cd', '#ef9a9a']

    fig1, ax1 = plt.subplots()
    wedges, texts, autotexts = ax1.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        textprops={'color': "black"}
    )
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)

# ---- STRATEGIES ----
st.markdown("### 🧠 Trading Skills")
st.markdown("""  
- ✅ **Futures Trading**: Directional & hedge-based trading in index and commodities  
- ✅ **Crypto Trading**: Momentum-based setups & on-chain signals  
- ✅ **Intraday Momentum**: Quant models based on price & volume  
- ✅ **Swing Trading**: Technical breakout + volume confirmations  
- ✅ **Risk Management**: Fixed stop-loss %, adaptive position sizing
""")
# ---- STRATEGIES SECTION ----
st.header("📊 Trading Strategies")

st.markdown("""
### 1. ICT SMC Volume Profile  
Combines **Inner Circle Trader (ICT)** concepts with **Smart Money Concepts (SMC)** and the **Volume Profile** to identify institutional price levels and volume-based zones for reversals or breakouts.

### 2. EMA Bookmap Liquidity Hunting  
Uses **Exponential Moving Averages (EMA)** alongside **Bookmap heatmaps** to track institutional liquidity zones, hunting for fake-outs and traps around high-liquidity clusters.

### 3. Fibonacci Retracement  
A classic tool to determine potential **pullback zones** in trending markets using key Fibonacci levels like 0.382, 0.5, and 0.618 for entries, stop-loss placements, and take-profit zones.
""")

# ---- CERTIFICATES SECTION ----
st.markdown("### 📜 Verified Certificates")
st.markdown("Below are **10 verified payout and strategy certificates**:")

cert_cols = st.columns(5)
for i in range(10):
    with cert_cols[i % 5]:
        st.image(f"certificates/certificate_{i + 1}.jpg", caption=f"Certificate {i + 1}", use_container_width=True)

# ---- CONTACT ----
st.markdown("### 📬 Contact Info")
st.markdown("""
- 📞 **Phone:** 7439913770  
- 📧 Email: **me9shyam@gmail.com** 
""")

st.markdown("---")
st.caption("© 2025 | Designed by Shyam Sundar Kr Singh | Powered by Streamlit")
