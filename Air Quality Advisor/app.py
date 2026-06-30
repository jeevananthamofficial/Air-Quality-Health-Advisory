import streamlit as st
import pandas as pd

# U.S. EPA 2024 PM2.5 AQI Breakpoints (effective May 6, 2024)
def calc_pm25_aqi(pm25):
    # Breakpoint structure: (C_low, C_high, I_low, I_high, category, color, advice)
    bp = [
        (0.0, 9.0, 0, 50, "Good", "🟢", "Satisfactory air quality; little/no risk."),
        (9.1, 35.4, 51, 100, "Moderate", "🟡", "Acceptable air quality; sensitive groups should limit exertion."),
        (35.5, 55.4, 101, 150, "Unhealthy for Sensitive Groups", "🟠", "Sensitive groups should reduce prolonged outdoor exertion."),
        (55.5, 125.4, 151, 200, "Unhealthy", "🔴", "Everyone may experience health effects; limit exertion."),
        (125.5, 225.4, 201, 300, "Very Unhealthy", "🟣", "Health alert: everyone should avoid outdoor exertion."),
        (225.5, 500.4, 301, 500, "Hazardous", "🟤", "Emergency conditions: everyone should remain indoors.")
    ]
    for cl, ch, il, ih, cat, col, adv in bp:
        if cl <= pm25 <= ch:
            return round(((ih - il) / (ch - cl)) * (pm25 - cl) + il), cat, col, adv
    return 500, "Hazardous", "🟤", "Emergency conditions: everyone should remain indoors."

# Streamlit Page Design
if __name__ == '__main__':
    st.set_page_config(page_title="Air Quality Advisory", page_icon="🌬️", layout="wide")
    st.markdown("## 🌬️ Air Quality Health Advisory System")
    st.markdown("Explore real-time AQI computations, custom dataset classification, and health recommendations.")

    tab1, tab2 = st.tabs(["🎛️ Live Calculator & Advice", "📊 OpenAQ Dataset Explorer"])

    with tab1:
        st.subheader("Manual AQI Calculator (PM2.5)")
        pm25 = st.slider("Select PM2.5 Concentration (µg/m³):", 0.0, 300.0, 12.0, step=0.1)
        aqi, cat, col, adv = calc_pm25_aqi(pm25)
        
        col1, col2 = st.columns(2)
        col1.metric(label=f"AQI Status: {cat} {col}", value=aqi)
        col2.info(f"**Health Advice:** {adv}")

    with tab2:
        st.subheader("Upload or view OpenAQ CSV/JSON Data")
        uploaded = st.file_uploader("Upload CSV/JSON", type=["csv", "json"])
        if uploaded:
            df = pd.read_csv(uploaded) if uploaded.name.endswith(".csv") else pd.read_json(uploaded)
        else:
            df = pd.DataFrame([
                {"city": "New York", "pm25": 8.5}, {"city": "London", "pm25": 14.2},
                {"city": "New Delhi", "pm25": 185.0}, {"city": "Sydney", "pm25": 4.1},
                {"city": "Cairo", "pm25": 45.3}
            ])
            st.caption("Showing default sample OpenAQ dataset:")
            
        df[["AQI", "Category", "Icon", "Advice"]] = df["pm25"].apply(lambda x: pd.Series(calc_pm25_aqi(x)))
        
        # Color styling for the city column matching its AQI category
        colors = {"Good": "background-color: #00e400; color: black; font-weight: bold;",
                  "Moderate": "background-color: #ffff00; color: black; font-weight: bold;",
                  "Unhealthy for Sensitive Groups": "background-color: #ff7e00; color: white; font-weight: bold;",
                  "Unhealthy": "background-color: #ff0000; color: white; font-weight: bold;",
                  "Very Unhealthy": "background-color: #8f3f97; color: white; font-weight: bold;",
                  "Hazardous": "background-color: #7e0023; color: white; font-weight: bold;"}
        style_city = lambda x: pd.DataFrame([[colors.get(r['Category'], '') if c == 'city' else '' for c in x.columns] for _, r in x.iterrows()], index=x.index, columns=x.columns)
        
        st.dataframe(df.style.apply(style_city, axis=None).background_gradient(subset=["AQI"], cmap="YlOrRd"), width="stretch")
        st.bar_chart(df, x="city", y="AQI", color="Category")
