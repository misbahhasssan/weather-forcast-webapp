import requests

API_KEY = "80eb2b01d6ba12a26fd2d580fa66e3f9"


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    if "list" not in data:
        raise KeyError("Place not found")

    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    return filtered_data[:nr_values]


if __name__ == "__main__":
    data = get_data(place="Islamabad", forecast_days=2)
    print(data)
