# Get station from SQLite database
import sqlite3
import os
from src.models.station import Station

def get_station(station_id):
    """Retrieve a station by its ID."""
    db_path = os.path.join(os.path.dirname(__file__), '../../../data/weather.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('SELECT id, name, location FROM Stations WHERE id = ?', (station_id,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return Station(id=result[0], name=result[1], location=result[2])
    return None