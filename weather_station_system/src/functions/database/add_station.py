# Add station to SQLite database
import sqlite3
import os

def add_station(station):
    """Add a station to the Stations table."""
    db_path = os.path.join(os.path.dirname(__file__), '../../../data/weather.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Stations (id, name, location)
        VALUES (?, ?, ?)
    ''', (station.id, station.name, station.location))

    conn.commit()
    conn.close()