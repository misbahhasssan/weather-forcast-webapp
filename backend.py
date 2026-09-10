import requests
API_KEY = "80eb2b01d6ba12a26fd2d580fa66e3f9"

def get_data(place, forecast_days, kind):

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    content  = requests.get(url)
    data = content.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    elif kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]

    return filtered_data

if __name__ == "__main__":
    data = get_data(place="Islamabad", forecast_days=1, kind="Temperature")
    print(data)
    print(len(data))
                    