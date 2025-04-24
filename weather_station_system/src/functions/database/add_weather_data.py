# Add weather data to SQLite database
import sqlite3
import os
from src.utils.json_utils import weather_data_to_json
from src.functions.encryption.encrypt import encrypt

def add_weather_data(station_id, weather_data):
    """Add encrypted weather data to the WeatherData table."""
    db_path = os.path.join(os.path.dirname(__file__), '../../../data/weather.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Convert WeatherData to JSON and encrypt
    json_data = weather_data_to_json(weather_data)
    encrypted_data = encrypt(json_data)

    cursor.execute('''
        INSERT INTO WeatherData (station_id, encrypted_data, timestamp)
        VALUES (?, ?, ?)
    ''', (station_id, encrypted_data, weather_data.timestamp.isoformat()))

    conn.commit()
    conn.close()