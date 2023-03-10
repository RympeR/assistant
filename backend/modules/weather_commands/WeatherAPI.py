import requests


class WeatherAPI:
    """
    This class is used to get weather data from OpenWeatherMap API.
    You can get data about temperature, humidity, pressure, wind speed, wind direction, clouds and weather description.
    methods:
        get_temperature() - get temperature
        get_humidity() - get humidity
        get_pressure() - get pressure
        get_wind_speed() - get wind speed
        get_wind_deg() - get wind direction
        get_clouds() - get clouds
        get_weather_description() - get weather description
        get_weather_icon() - get weather icon
    """
    API_TOKEN = "caa912829cb525698f5306d64634"
    BASEURL = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric"

    def __init__(self, city):
        self.city = city
        self.url = self.BASEURL.format(city=self.city, token=self.API_TOKEN)

    def get_weather(self):
        response = requests.get(self.url)
        return response.json()

    def get_temperature(self):
        return self.get_weather()["main"]["temp"]

    def get_humidity(self):
        return self.get_weather()["main"]["humidity"]

    def get_pressure(self):
        return self.get_weather()["main"]["pressure"]

    def get_wind_speed(self):
        return self.get_weather()["wind"]["speed"]

    def get_wind_deg(self):
        return self.get_weather()["wind"]["deg"]

    def get_clouds(self):
        return self.get_weather()["clouds"]["all"]

    def get_weather_description(self):
        return self.get_weather()["weather"][0]["description"]

    def get_weather_icon(self):
        return self.get_weather()["weather"][0]["icon"]
