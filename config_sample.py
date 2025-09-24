"""
Sample configuration file for Weather App
Copy this file to config.py and add your actual API key
"""

# OpenWeatherMap API Configuration
API_KEY = "your_api_key_here"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Default settings
DEFAULT_UNITS = "metric"  # metric, imperial, or kelvin
DEFAULT_LANGUAGE = "en"   # language code for weather descriptions

# App settings
MAX_CITIES_PER_REQUEST = 10
TIMEOUT_SECONDS = 10

# Display settings
SHOW_DETAILED_INFO = True
USE_COLORED_OUTPUT = False  # Set to True if you want colored terminal output
