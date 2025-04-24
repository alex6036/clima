# clima
https://github.com/alex6036/clima.git

# 🌦️ Clima - Sistema de Estación Meteorológica

Clima es un sistema de gestión de estaciones meteorológicas que permite registrar, almacenar y visualizar datos climáticos como temperatura, humedad, presión y velocidad del viento. Este proyecto utiliza una arquitectura modular con estructuras de datos personalizadas, una base de datos SQLite y una interfaz gráfica interactiva creada con Gradio.

## 🚀 Características

- **Gestión de estaciones meteorológicas**: Agrega, busca y elimina estaciones.
- **Registro de datos climáticos**: Almacena datos como temperatura, humedad, presión y velocidad del viento.
- **Visualización de datos**: Gráficas interactivas para analizar tendencias climáticas.
- **Seguridad**: Los datos se almacenan cifrados utilizando AES-256.
- **Estructuras de datos personalizadas**: Uso de listas enlazadas, tablas hash y listas de listas.
- **Base de datos SQLite**: Persistencia de datos para estaciones y registros climáticos.

## 📂 Estructura del Proyecto

weather_station_system/ ├── main.py # Punto de entrada principal ├── data/ │ └── weather.db # Base de datos SQLite ├── src/ │ ├── core/ # Lógica principal del sistema │ ├── functions/ # Funciones auxiliares │ ├── interface/ # Interfaz gráfica con Gradio │ ├── models/ # Estructuras de datos personalizadas │ └── utils/ # Utilidades y configuración └── tests/ # Pruebas unitarias

## 🛠️ Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/clima.git
   cd clima

   pip install -r requirements.txt

   python weather_station_system/main.py