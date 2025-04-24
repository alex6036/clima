# WeatherSystem class for coordinating system components
from src.models.list_of_lists import ListOfLists
from src.models.hash_table import HashTable
from src.models.station import Station
from src.models.weather_data import WeatherData
from src.functions.database.init_db import init_db
from src.functions.database.add_station import add_station
from src.functions.database.add_weather_data import add_weather_data
from src.functions.database.get_station import get_station
from src.functions.database.get_weather_data import get_weather_data

class WeatherSystem:
    def __init__(self):
        self.list_of_lists = ListOfLists()  # Dynamic list-of-lists for stations and weather data
        self.hash_table = HashTable()       # Hash table for fast station lookup
        init_db()                           # Initialize SQLite database

    def add_station(self, id, name, location):
        """Add a new station to the system."""
        if self.hash_table.search(id):
            raise ValueError(f"Station with ID {id} already exists")
        station = Station(id, name, location)
        # Add to list of lists
        self.list_of_lists.add_station(station)
        # Add to hash table
        self.hash_table.add(id, station)
        # Add to database
        add_station(station)

    def add_weather_data(self, station_id, temperature, humidity, pressure, wind_speed):
        """Add weather data to a station."""
        station = self.hash_table.search(station_id)
        if not station:
            raise ValueError(f"Station with ID {station_id} not found")
        weather_data = WeatherData(temperature, humidity, pressure, wind_speed)
        # Add to station's weather data list
        station.weather_data.size += 1
        from src.functions.list_functions.insert import insert
        insert(station.weather_data, weather_data, key=lambda x: x.timestamp)
        # Add to database (encrypted)
        add_weather_data(station_id, weather_data)

    def get_station(self, station_id):
        """Retrieve a station by ID."""
        # Try hash table first (faster)
        station = self.hash_table.search(station_id)
        if station:
            return station
        # Fallback to database
        return get_station(station_id)

    def get_weather_data(self, station_id):
        """Retrieve all weather data for a station."""
        station = self.get_station(station_id)
        if not station:
            return []
        # Get from database (decrypted)
        return get_weather_data(station_id)