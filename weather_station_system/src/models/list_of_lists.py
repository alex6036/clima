# ListOfLists class for dynamic list-of-lists structure
from src.models.linked_list import LinkedList
from src.models.station import Station

class ListOfLists:
    def __init__(self):
        self.head = None  # Pointer to the first node (stations)
        self.size = 0     # Number of stations

    def add_station(self, station):
        """Add a station to the list, maintaining order by station ID."""
        from src.functions.list_functions.insert import insert
        insert(self, station, key=lambda x: x.id)

    def remove_station(self, station_id):
        """Remove a station by its ID."""
        from src.functions.list_functions.remove import remove
        return remove(self, station_id, key=lambda x: x.id)

    def search_station(self, station_id):
        """Search for a station by its ID."""
        from src.functions.list_functions.search import search
        return search(self, station_id, key=lambda x: x.id)

    def traverse(self):
        """Traverse and display all stations and their weather data."""
        from src.functions.list_functions.traverse import traverse
        traverse(self)