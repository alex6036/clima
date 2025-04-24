# WeatherData class for climate data records
from datetime import datetime

class WeatherData:
    def __init__(self, temperature, humidity, pressure, wind_speed, timestamp=None):
        self.temperature = temperature  # Temperature in °C (float)
        self.humidity = humidity        # Humidity in % (float)
        self.pressure = pressure        # Pressure in hPa (float)
        self.wind_speed = wind_speed    # Wind speed in km/h (float)
        self.timestamp = timestamp or datetime.now()  # Date and time of record