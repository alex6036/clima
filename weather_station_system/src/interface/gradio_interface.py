# Gradio interface for the weather station system
import gradio as gr
from src.core.weather_system import WeatherSystem
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Define a custom CSS for styling
custom_css = """
body {
    background: linear-gradient(to bottom right, #1e3c72, #2a5298);
    color: white;
    font-family: 'Arial', sans-serif;
}
.gradio-container {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}
h1, h2, h3 {
    color: #e0f7fa;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
}
input, button, .gr-button {
    background-color: #2c5f9e !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 10px !important;
    transition: background-color 0.3s ease;
}
input:hover, button:hover, .gr-button:hover {
    background-color: #3b82f6 !important;
}
.gr-group {
    background: rgba(255, 255, 255, 0.15) !important;
    border-radius: 10px !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    padding: 15px !important;
}
"""

def create_interface(weather_system):
    """Create and launch the Gradio interface with enhanced styling."""
    def add_station(id, name, location):
        try:
            weather_system.add_station(id, name, location)
            return f"✅ Station {id} added successfully."
        except Exception as e:
            return f"❌ Error adding station: {str(e)}"

    def add_weather_data(station_id, temperature, humidity, pressure, wind_speed):
        try:
            weather_system.add_weather_data(station_id, temperature, humidity, pressure, wind_speed)
            return f"✅ Weather data added for station {station_id}."
        except Exception as e:
            return f"❌ Error adding weather data: {str(e)}"

    def search_station(station_id):
        try:
            station = weather_system.get_station(station_id)
            if not station:
                return "❌ Station not found.", None, None, None, None
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
            # Create plots
            plots = []
            if not df.empty:
                # Temperature Plot
                plt.figure(figsize=(8, 4))
                plt.plot(df["Timestamp"], df["Temperature (°C)"], marker='o', color='#61d4ff', linewidth=2)
                plt.xlabel("Timestamp", color='white')
                plt.ylabel("Temperature (°C)", color='white')
                plt.title(f"Gráfica de Temperatura", color='white')
                plt.xticks(rotation=45, color='white')
                plt.yticks(color='white')
                plt.grid(True, linestyle='--', alpha=0.7)
                plt.gca().set_facecolor('#1e3c72')
                plt.gcf().set_facecolor('none')  # Cambiado a 'none' para fondo transparente
                plt.tight_layout()
                plots.append(plt.gcf())

                # Humidity Plot
                plt.figure(figsize=(8, 4))
                plt.plot(df["Timestamp"], df["Humidity (%)"], marker='o', color='#61d4ff', linewidth=2)
                plt.xlabel("Timestamp", color='white')
                plt.ylabel("Humidity (%)", color='white')
                plt.title(f"Gráfica de Humedad", color='white')
                plt.xticks(rotation=45, color='white')
                plt.yticks(color='white')
                plt.grid(True, linestyle='--', alpha=0.7)
                plt.gca().set_facecolor('#1e3c72')
                plt.gcf().set_facecolor('none')  # Cambiado a 'none' para fondo transparente
                plt.tight_layout()
                plots.append(plt.gcf())

                # Pressure Plot
                plt.figure(figsize=(8, 4))
                plt.plot(df["Timestamp"], df["Pressure (hPa)"], marker='o', color='#61d4ff', linewidth=2)
                plt.xlabel("Timestamp", color='white')
                plt.ylabel("Pressure (hPa)", color='white')
                plt.title(f"Gráfica de Presión", color='white')
                plt.xticks(rotation=45, color='white')
                plt.yticks(color='white')
                plt.grid(True, linestyle='--', alpha=0.7)
                plt.gca().set_facecolor('#1e3c72')
                plt.gcf().set_facecolor('none')  # Cambiado a 'none' para fondo transparente
                plt.tight_layout()
                plots.append(plt.gcf())
            else:
                plots = [None, None, None]

            return f"🌍 Station: {station.id}, Name: {station.name}, Location: {station.location}", df, *plots
        except Exception as e:
            return f"❌ Error searching station: {str(e)}", None, None, None, None

    # Create the Gradio interface with a custom theme
    theme = gr.themes.Soft(
        primary_hue="blue",
        secondary_hue="cyan",
        neutral_hue="slate",
        text_size="lg",
        spacing_size="md",
        radius_size="lg",
    )

    with gr.Blocks(theme=theme, css=custom_css) as interface:
        gr.Markdown("# 🌦️ Sistema de Estación Meteorológica", elem_classes=["header-title"])
        gr.Markdown("Gestiona estaciones meteorológicas y sus datos climáticos con facilidad.", elem_classes=["subtitle"])

        # Add Station Section
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("## 📍 Agregar Estación", elem_classes=["section-title"])
                with gr.Group():
                    station_id_input = gr.Textbox(label="Identificador de la Estación", placeholder="Ejemplo: EST001")
                    station_name_input = gr.Textbox(label="Nombre de la Estación", placeholder="Ejemplo: Estación Norte")
                    station_location_input = gr.Textbox(label="Ubicación", placeholder="Ejemplo: Buenos Aires")
                    add_station_btn = gr.Button("Agregar Estación", variant="primary")
                    station_output = gr.Textbox(label="Resultado", interactive=False)
                    add_station_btn.click(
                        fn=add_station,
                        inputs=[station_id_input, station_name_input, station_location_input],
                        outputs=station_output
                    )

        # Add Weather Data Section
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("## ☁️ Agregar Datos Meteorológicos", elem_classes=["section-title"])
                with gr.Group():
                    weather_station_id_input = gr.Textbox(label="Identificador de la Estación", placeholder="Ejemplo: EST001")
                    temperature_input = gr.Number(label="Temperatura (°C)", value=0, step=0.1)
                    humidity_input = gr.Number(label="Humedad (%)", value=0, step=0.1)
                    pressure_input = gr.Number(label="Presión (hPa)", value=0, step=0.1)
                    wind_speed_input = gr.Number(label="Velocidad del Viento (km/h)", value=0, step=0.1)
                    add_weather_btn = gr.Button("Agregar Datos Meteorológicos", variant="primary")
                    weather_output = gr.Textbox(label="Resultado", interactive=False)
                    add_weather_btn.click(
                        fn=add_weather_data,
                        inputs=[weather_station_id_input, temperature_input, humidity_input, pressure_input, wind_speed_input],
                        outputs=weather_output
                    )

        # Search Station Section
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("## 🔍 Estación de Búsqueda", elem_classes=["section-title"])
                with gr.Group():
                    search_station_id_input = gr.Textbox(label="Identificador de la Estación", placeholder="Ejemplo: EST001")
                    search_btn = gr.Button("Buscar", variant="primary")
                    search_output = gr.Textbox(label="Información de la Estación", interactive=False)
                    search_table = gr.Dataframe(label="Datos Meteorológicos")
                    with gr.Row():
                        temp_plot = gr.Plot(label="Gráfica de Temperatura")
                        hum_plot = gr.Plot(label="Gráfica de Humedad")
                        press_plot = gr.Plot(label="Gráfica de Presión")
                    search_btn.click(
                        fn=search_station,
                        inputs=search_station_id_input,
                        outputs=[search_output, search_table, temp_plot, hum_plot, press_plot]
                    )

    interface.launch()