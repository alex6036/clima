# Main function for system initialization
from src.core.weather_system import WeatherSystem
from src.interface.gradio_interface import create_interface

def main():
    """Initialize the weather station system and launch the interface."""
    weather_system = WeatherSystem()
    create_interface(weather_system)