# Station class for weather stations
from src.models.linked_list import LinkedList

class Station:
    def __init__(self, id, name, location):
        self.id = id                # Unique identifier (e.g., "EST001")
        self.name = name           # Name of the station (e.g., "Station North")
        self.location = location   # Location (e.g., "Buenos Aires")
        self.weather_data = LinkedList()  # Sublist of weather data
        self.next = None           # For linking in the main list