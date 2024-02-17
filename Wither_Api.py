import requests # This is external Library

class WeatherAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.weatherapi.com/v1"

    def get_current_temperature(self, city):
        endpoint = "/current.json"
        params = {"key": self.api_key, "q": city}
        response = requests.get(self.base_url + endpoint, params=params)
        data = response.json()
        return data["current"]["temp_c"]

    def get_temperature_after(self, city, days, hour=None):
        endpoint = "/forecast.json"
        params = {"key": self.api_key, "q": city, "days": days}
        response = requests.get(self.base_url + endpoint, params=params)
        data = response.json()

        if hour is not None:
            for forecast in data["forecast"]["forecastday"]:
                if forecast["hour"] == hour:
                    return forecast["day"]["avgtemp_c"]
        else:
            return data["forecast"]["forecastday"][-1]["day"]["avgtemp_c"]

    def get_lat_and_long(self, city):
        endpoint = "/search.json"
        params = {"key": self.api_key, "q": city}
        response = requests.get(self.base_url + endpoint, params=params)
        data = response.json()

        if isinstance(data, list) and data:  # Check if data is a non-empty list
            # Assuming you want information from the first item in the list
            location_data = data[0]
            if "location" in location_data:
                location = location_data["location"]
                return location.get("lat"), location.get("lon")
            else:
                print(f"Error: 'location' key not found in data for {city}")
        else:
            print(f"Error: Unexpected response format for {city}")

        return None, None

# Example usage:
api_key = "4f5cf0f9522c482e9b6182402241702"
weather_client = WeatherAPIClient(api_key)

current_temp = weather_client.get_current_temperature("New York")
print(f"Current temperature in New York: {current_temp}°C")

temp_after_3_days = weather_client.get_temperature_after("London", days=3)
print(f"Average temperature in London after 3 days: {temp_after_3_days}°C")

lat, lon = weather_client.get_lat_and_long("Paris")
print(f"Latitude and Longitude of Paris: {lat}, {lon}")
