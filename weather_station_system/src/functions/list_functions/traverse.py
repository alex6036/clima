# Traverse function for linked lists
def traverse(lst):
    current = lst.head
    while current:
        if hasattr(current.info, 'weather_data'):
            # For stations, show ID, name, and traverse weather data
            print(f"Station: {current.info.id}, Name: {current.info.name}, Location: {current.info.location}")
            print("Weather Data:")
            weather_current = current.info.weather_data.head
            while weather_current:
                wd = weather_current.info
                print(f"  {wd.timestamp}: Temp={wd.temperature}°C, Hum={wd.humidity}%, Press={wd.pressure}hPa, Wind={wd.wind_speed}km/h")
                weather_current = weather_current.next
        else:
            # For weather data or other elements
            print(current.info)
        current = current.next