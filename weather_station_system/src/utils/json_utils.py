# JSON utility functions for serialization/deserialization
import json
from datetime import datetime

def weather_data_to_json(weather_data):
    """Convert WeatherData object to JSON string."""
    return json.dumps({
        'temperature': weather_data.temperature,
        'humidity': weather_data.humidity,
        'pressure': weather_data.pressure,
        'wind_speed': weather_data.wind_speed,
        'timestamp': weather_data.timestamp.isoformat()
    })

def json_to_weather_data(json_str):
    """Convert JSON string to WeatherData object."""
    from src.models.weather_data import WeatherData
    data = json.loads(json_str)
    return WeatherData(
        temperature=data['temperature'],
        humidity=data['humidity'],
        pressure=data['pressure'],
        wind_speed=data['wind_speed'],
        timestamp=datetime.fromisoformat(data['timestamp'])
    )