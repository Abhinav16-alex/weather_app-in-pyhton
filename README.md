# 🌤️ Python Weather App

A simple yet comprehensive weather application built with Python that fetches real-time weather data using the OpenWeatherMap API.

## 📋 Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [API Key Setup](#api-key-setup)
- [Screenshots](#screenshots)
- [Error Handling](#error-handling)
- [Project Structure](#project-structure)
- [Learning Outcomes](#learning-outcomes)

## ✨ Features

- 🌍 Get current weather for any city worldwide
- 🌡️ Display temperature, humidity, pressure, and wind information
- ☁️ Show weather conditions and descriptions
- 📊 Support for multiple cities at once
- 🔒 Comprehensive error handling
- 💻 User-friendly command-line interface
- 🌐 Real-time data from OpenWeatherMap API

## 🛠️ Technologies Used

- **Python 3.x** - Core programming language
- **Requests Library** - For making HTTP API calls
- **OpenWeatherMap API** - Weather data source
- **JSON** - Data parsing and handling

## 🚀 Setup Instructions

### Prerequisites
- Python 3.6 or higher installed on your system
- Internet connection for API calls
- OpenWeatherMap API key (free)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd python-weather-app
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   Or manually install:
   ```bash
   pip install requests
   ```

3. **Get your API key**
   - Visit [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Generate your API key

4. **Configure API key**
   - Open `weather_app.py`
   - Replace `"your_api_key_here"` with your actual API key
   - Save the file

5. **Run the application**
   ```bash
   python weather_app.py
   ```

## 🎯 Usage

The application provides an interactive menu with three options:

### Option 1: Single City Weather
```
Enter city name: London
```
Displays detailed weather information for the specified city.

### Option 2: Multiple Cities Weather
```
Enter city names (separated by commas): London, Paris, Tokyo
```
Shows weather data for all specified cities.

### Option 3: Exit
Closes the application gracefully.

## 🔑 API Key Setup

1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Click "Sign Up" to create a free account
3. After verification, go to "API Keys" section
4. Copy your API key
5. Replace the placeholder in the code:
   ```python
   self.api_key = "your_actual_api_key_here"
   ```

**Note**: Free tier allows 1000 API calls per day, which is perfect for learning!

## 📸 Screenshots

### Main Menu
```
🌤️  Welcome to Python Weather App!
========================================

Choose an option:
1. Get weather for a single city
2. Get weather for multiple cities
3. Exit

Enter your choice (1-3):
```

### Weather Display Example
```
╔══════════════════════════════════════╗
║           WEATHER REPORT             ║
╚══════════════════════════════════════╝

🌍 City: London, GB
📅 Date & Time: 2024-01-15 14:30:22

🌡️  TEMPERATURE:
   Current: 8°C
   Feels like: 6°C
   Min: 7°C
   Max: 10°C

☁️  WEATHER:
   Condition: Clouds
   Description: Scattered Clouds

💧 HUMIDITY: 73%
🌬️  WIND:
   Speed: 3.5 m/s
   Direction: 240°
🔽 PRESSURE: 1013 hPa
☀️  VISIBILITY: 10000 meters
```

## ⚠️ Error Handling

The application handles various error scenarios:

- **Invalid city names** - Shows "City not found" message
- **Network issues** - Detects connection problems
- **Invalid API key** - Alerts about authentication errors
- **API rate limits** - Handles quota exceeded scenarios
- **Malformed responses** - Manages JSON parsing errors

## 📁 Project Structure

```
python-weather-app/
│
├── weather_app.py          # Main application file
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── screenshots/           # Application screenshots (if any)
    └── demo.png
```

## 📚 Learning Outcomes

This project demonstrates:

### API Integration
- Making HTTP requests using the `requests` library
- Handling API responses and status codes
- Working with JSON data parsing

### Error Handling
- Using try-except blocks for robust error management
- Handling different types of exceptions
- Providing user-friendly error messages

### Data Processing
- Extracting and formatting data from JSON responses
- Converting units and displaying information clearly

### User Experience
- Creating interactive command-line interfaces
- Input validation and sanitization
- Professional output formatting

### Python Concepts
- Object-oriented programming with classes
- Function definition and usage
- String formatting and manipulation
- Exception handling best practices

## 🎓 Key Programming Concepts Covered

- **HTTP Requests**: Understanding how to communicate with web APIs
- **JSON Handling**: Parsing and extracting data from JSON responses
- **Error Management**: Implementing comprehensive error handling
- **User Input**: Validating and processing user inputs
- **Code Organization**: Structuring code using classes and methods
- **Documentation**: Writing clear, professional documentation

## 🚀 Future Enhancements

Potential improvements for this project:
- Add weather forecast for multiple days
- Implement caching for frequently requested cities
- Create a GUI version using tkinter
- Add weather maps and visual charts
- Support for different temperature units
- Weather alerts and notifications

## 🤝 Contributing

This is a learning project, but feel free to:
- Report bugs or issues
- Suggest improvements
- Share your own enhancements

## 📄 License

This project is created for educational purposes as part of a Python development internship.

---

**Built with ❤️ for learning Python API integration**

*Happy Coding! 🚀*
