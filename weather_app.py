import requests
import json
from datetime import datetime

class WeatherApp:
    def __init__(self):
        # Free API key from OpenWeatherMap (sign up at openweathermap.org)
        # Replace with your actual API key
        self.api_key = "your_api_key_here"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, city_name):
        """
        Get weather data for a specific city
        """
        try:
            # Construct the complete API URL
            complete_url = f"{self.base_url}?q={city_name}&appid={self.api_key}&units=metric"
            
            # Make HTTP GET request
            response = requests.get(complete_url)
            
            # Check if request was successful (status code 200)
            if response.status_code == 200:
                # Parse JSON response
                weather_data = response.json()
                return self.display_weather(weather_data, city_name)
            
            elif response.status_code == 404:
                return f"Error: City '{city_name}' not found. Please check the city name."
            
            elif response.status_code == 401:
                return "Error: Invalid API key. Please check your API key."
            
            else:
                return f"Error: Unable to fetch weather data. Status code: {response.status_code}"
                
        except requests.exceptions.ConnectionError:
            return "Error: No internet connection. Please check your network."
        
        except requests.exceptions.RequestException as e:
            return f"Error: Request failed - {str(e)}"
        
        except json.JSONDecodeError:
            return "Error: Invalid response from weather service."
        
        except Exception as e:
            return f"Error: An unexpected error occurred - {str(e)}"
    
    def display_weather(self, weather_data, city_name):
        """
        Display weather information in a readable format
        """
        try:
            # Extract weather information
            main_data = weather_data['main']
            weather_desc = weather_data['weather'][0]
            wind_data = weather_data['wind']
            sys_data = weather_data['sys']
            
            # Format the weather information
            weather_info = f"""
╔══════════════════════════════════════╗
║           WEATHER REPORT             ║
╚══════════════════════════════════════╝

 City: {city_name.title()}, {sys_data.get('country', 'N/A')}
 Date & Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

  TEMPERATURE:
   Current: {main_data['temp']}°C
   Feels like: {main_data['feels_like']}°C
   Min: {main_data['temp_min']}°C
   Max: {main_data['temp_max']}°C

  WEATHER:
   Condition: {weather_desc['main']}
   Description: {weather_desc['description'].title()}

 HUMIDITY: {main_data['humidity']}%

  WIND:
   Speed: {wind_data.get('speed', 'N/A')} m/s
   Direction: {wind_data.get('deg', 'N/A')}°

 PRESSURE: {main_data['pressure']} hPa

  VISIBILITY: {weather_data.get('visibility', 'N/A')} meters
            """
            
            return weather_info
            
        except KeyError as e:
            return f"Error: Missing weather data field - {str(e)}"
    
    def get_multiple_cities_weather(self, cities):
        """
        Get weather for multiple cities
        """
        results = []
        for city in cities:
            result = self.get_weather(city.strip())
            results.append(result)
            print("-" * 50)
        
        return results

def main():
    """
    Main function to run the weather app
    """
    weather_app = WeatherApp()
    
    print("  Welcome to Python Weather App!")
    print("=" * 40)
    
    while True:
        print("\nChoose an option:")
        print("1. Get weather for a single city")
        print("2. Get weather for multiple cities")
        print("3. Exit")
        
        try:
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                city = input("Enter city name: ").strip()
                if city:
                    print("\nFetching weather data...")
                    result = weather_app.get_weather(city)
                    print(result)
                else:
                    print("Please enter a valid city name.")
            
            elif choice == '2':
                cities_input = input("Enter city names (separated by commas): ").strip()
                if cities_input:
                    cities = cities_input.split(',')
                    print("\nFetching weather data for multiple cities...")
                    weather_app.get_multiple_cities_weather(cities)
                else:
                    print("Please enter valid city names.")
            
            elif choice == '3':
                print("Thank you for using Python Weather App! ")
                break
            
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
                
        except KeyboardInterrupt:
            print("\n\nExiting... Thank you for using Python Weather App! ")
            break
        
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
