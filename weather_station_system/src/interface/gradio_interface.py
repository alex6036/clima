# Gradio interface for the weather station system
import gradio as gr
from src.core.weather_system import WeatherSystem
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

def create_interface(weather_system):
    """Create and launch the Gradio interface."""
    def add_station(id, name, location):
        try:
            weather_system.add_station(id, name, location)
            return f"Station {id} added successfully."
        except Exception as e:
            return f"Error adding station: {str(e)}"

    def add_weather_data(station_id, temperature, humidity, pressure, wind_speed):
        try:
            weather_system.add_weather_data(station_id, temperature, humidity, pressure, wind_speed)
            return f"Weather data added for station {station_id}."
        except Exception as e:
            return f"Error adding weather data: {str(e)}"

    def search_station(station_id):
        try:
            station = weather_system.get_station(station_id)
            if not station:
                return "Station not found.", None
            # Get weather data
            weather_data = weather_system.get_weather_data(station_id)
            # Create a DataFrame for display
            df = pd.DataFrame([
                {
                    "Timestamp": wd.timestamp,
                    "Temperature (°C)": wd.temperature,
                    "Humidity (%)": wd.humidity,
                    "Pressure (hPa)": wd.pressure,
                    "Wind Speed (km/h)": wd.wind_speed
                } for wd in weather_data
            ])
            # Create a plot
            if not df.empty:
                plt.figure()
                plt.plot(df["Timestamp"], df["Temperature (°C)"], marker='o')
                plt.xlabel("Timestamp")
                plt.ylabel("Temperature (°C)")
                plt.title(f"Temperature for Station {station_id}")
                plt.xticks(rotation=45)
                plt.tight_layout()
                plot = plt.gcf()
            else:
                plot = None
            return f"Station: {station.id}, Name: {station.name}, Location: {station.location}", df, plot
        except Exception as e:
            return f"Error searching station: {str(e)}", None, None

    with gr.Blocks() as interface:
        gr.Markdown("# Weather Station System")
        
        # Add Station
        with gr.Row():
            with gr.Column():
                gr.Markdown("## Add Station")
                station_id = gr.Textbox(label="Station ID")
                station_name = gr.Textbox(label="Station Name")
                station_location = gr.Textbox(label="Location")
                add_station_btn = gr.Button("Add Station")
                station_output = gr.Textbox(label="Result")
                add_station_btn.click(
                    fn=add_station,
                    inputs=[station_id, station_name, station_location],
                    outputs=station_output
                )

        # Add Weather Data
        with gr.Row():
            with gr.Column():
                gr.Markdown("## Add Weather Data")
                weather_station_id = gr.Textbox(label="Station ID")
                temperature = gr.Number(label="Temperature (°C)")
                humidity = gr.Number(label="Humidity (%)")
                pressure = gr.Number(label="Pressure (hPa)")
                wind_speed = gr.Number(label="Wind Speed (km/h)")
                add_weather_btn = gr.Button("Add Weather Data")
                weather_output = gr.Textbox(label="Result")
                add_weather_btn.click(
                    fn=add_weather_data,
                    inputs=[weather_station_id, temperature, humidity, pressure, wind_speed],
                    outputs=weather_output
                )

        # Search Station
        with gr.Row():
            with gr.Column():
                gr.Markdown("## Search Station")
                search_station_id = gr.Textbox(label="Station ID")
                search_btn = gr.Button("Search")
                search_output = gr.Textbox(label="Station Info")
                search_table = gr.Dataframe(label="Weather Data")
                search_plot = gr.Plot(label="Temperature Plot")
                search_btn.click(
                    fn=search_station,
                    inputs=search_station_id,
                    outputs=[search_output, search_table, search_plot]
                )

    interface.launch()