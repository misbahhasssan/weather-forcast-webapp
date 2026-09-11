import streamlit as st
import plotly.express as px
from datetime import datetime
from backend import get_data

st.set_page_config(page_title="Weather Forecast", layout="wide")
st.title("Weather Forecast")
st.caption("Simple forecast for the next days")

place = st.text_input("Place", placeholder="Type a city name")
days = st.slider("Forecast Days", min_value=1, max_value=5, value=2)

option = st.selectbox("Select data to view", ("Temperature", "Sky"))

if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] - 273.15 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]

            figure = px.line(
                x=dates,
                y=temperatures,
                labels={"x": "Date", "y": "Temperature (°C)"},
                title=f"Temperature forecast for {place}",
            )
            figure.update_layout(template="plotly_white")
            st.plotly_chart(figure, use_container_width=True)

        elif option == "Sky":
            image_map = {
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png",
                "Drizzle": "images/rain.png",
                "Thunderstorm": "images/rain.png",
                "Mist": "images/cloud.png",
            }

            st.subheader(f"Sky conditions for {place}")

            # Use 4 image cards per row for a simple and clean grid.
            columns = st.columns(4)
            for index, item in enumerate(filtered_data):
                sky_condition = item["weather"][0]["main"]
                image_path = image_map.get(sky_condition, "images/cloud.png")

                forecast_time = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")
                display_date = forecast_time.strftime("%A, %b %d, %Y")
                display_time = forecast_time.strftime("%I:%M %p")

                with columns[index % 4]:
                    st.image(image_path, width=130)
                    st.caption(f"{sky_condition}")
                    st.caption(f"{display_date}\n{display_time}")

    except KeyError:
        st.warning("This place does not exist. Please enter a valid place name.")
    except Exception as error:
        st.error(f"Unable to load weather forecast: {error}")

