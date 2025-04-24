# Get weather data from SQLite database
import sqlite3
import os
from src.utils.json_utils import json_to_weather_data
from src.functions.encryption.decrypt import decrypt

def get_weather_data(station_id):
    """Retrieve all weather data for a station, decrypted."""
    db_path = os.path.join(os.path.dirname(__file__), '../../../data/weather.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('SELECT encrypted_data, timestamp FROM WeatherData WHERE station_id = ?', (station_id,))
    results = cursor.fetchall()

    conn.close()

    weather_data_list = []
    for encrypted_data, timestamp in results:
        try:
            json_data = decrypt(encrypted_data)
            weather_data = json_to_weather_data(json_data)
            weather_data_list.append(weather_data)
        except Exception as e:
            print(f"Error decrypting data for {station_id}: {e}")

    return weather_data_list