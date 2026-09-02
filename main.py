import streamlit as st
import plotly.express as px

st.title("Weather Forcast for the Next Days")

place = st.text_input("Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5)

option = st.selectbox("Select data to view",
                       ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} in {place}")

def get_data(days):
    dates = ["2026-09-02", "2026-09-03", "2026-09-04"]
    temperatures = [25, 26, 24]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t, labels = {"X": "Date", "Y": "Temperature (°C)"})
st.plotly_chart(figure)