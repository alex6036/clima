# Initialize SQLite database
import sqlite3
import os

def init_db():
    """Initialize the SQLite database and create tables."""
    db_path = os.path.join(os.path.dirname(__file__), '../../../data/weather.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create Stations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Stations (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            location TEXT NOT NULL
        )
    ''')

    # Create WeatherData table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS WeatherData (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            station_id TEXT NOT NULL,
            encrypted_data BLOB NOT NULL,
            timestamp TEXT NOT NULL,
            FOREIGN KEY (station_id) REFERENCES Stations (id)
        )
    ''')

    conn.commit()
    conn.close()