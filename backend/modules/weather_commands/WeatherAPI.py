import requests

from backend.engine.settings import USER_CITY, USER_LANGUAGE, WEATHER_API_TOKEN
from backend.utils.utils import translate, serializer


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
    BASEURL = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric"

    def __init__(self):
        self.lang = USER_LANGUAGE
        self.city = USER_CITY
        self.url = self.BASEURL.format(city=self.city, token=WEATHER_API_TOKEN)

    def get_weather(self):
        response = requests.get(self.url)
        return response.json()

    @translate
    @serializer("temperature")
    def get_temperature(self):
        return self.get_weather()["main"]["temp"]

    @translate
    @serializer("humidity")
    def get_humidity(self):
        return self.get_weather()["main"]["humidity"]

    @translate
    @serializer("pressure")
    def get_pressure(self):
        return self.get_weather()["main"]["pressure"]

    @translate
    @serializer("wind_speed")
    def get_wind_speed(self):
        return self.get_weather()["wind"]["speed"]

    @translate
    @serializer("wind_deg")
    def get_wind_deg(self):
        return self.get_weather()["wind"]["deg"]

    @translate
    @serializer("clouds")
    def get_clouds(self):
        return self.get_weather()["clouds"]["all"]

    @translate
    @serializer("weather description")
    def get_weather_description(self):
        return self.get_weather()["weather"][0]["description"]

    @translate
    @serializer("weather icon")
    def get_weather_icon(self):
        return self.get_weather()["weather"][0]["icon"]

    def __str__(self):
        return f"""
        City: {self.city}
        Temperature: {self.get_temperature()}
        Humidity: {self.get_humidity()}
        Pressure: {self.get_pressure()}
        Wind speed: {self.get_wind_speed()}
        Wind direction: {self.get_wind_deg()}
        Clouds: {self.get_clouds()}
        Weather description: {self.get_weather_description()}
        Weather icon: {self.get_weather_icon()}"""


if __name__ == '__main__':
    print(WeatherAPI().get_temperature())
    print(WeatherAPI().get_humidity())
