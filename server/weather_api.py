import requests

# Your API key
API_KEY = "851b80f03ae1ecfe7eaefb63b6fbc2d5"

BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"


# City IDS
# London, UK - City ID: 2643743
# New York, USA - City ID: 5128581
# Paris, France - City ID: 2988507
# Tokyo, Japan - City ID: 1850147
# Los Angeles, USA - City ID: 5368361
# Berlin, Germany - City ID: 2950159
# Moscow, Russia - City ID: 524901
# Sydney, Australia - City ID: 2147714
# Mumbai, India - City ID: 1269515
# Rome, Italy - City ID: 3169070
# Beijing, China - City ID: 1816670
# Cape Town, South Africa - City ID: 3369157
# Mexico City, Mexico - City ID: 3530597
# Dubai, UAE - City ID: 292223
# Rio de Janeiro, Brazil - City ID: 3451190
# Chisinau, Moldova is 617702.
city_id = "1850147"


# Construct the full URL with query parameters
url = f"{BASE_URL}?id={city_id}&appid={API_KEY}&units=metric"  # units=metric for Celsius

# Send a request to the OpenWeather API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON data
    
    # Extract and display the forecasted weather for the next 5 days
    print(f"5-day forecast for city ID {city_id}:")

    # Loop through the forecast data (the API provides forecasts at 3-hour intervals)
    for forecast in data['list']:
        timestamp = forecast['dt_txt']  # Date and time of the forecast
        temperature = forecast['main']['temp']  # Temperature in Celsius
        weather_description = forecast['weather'][0]['description']  # Weather description
        humidity = forecast['main']['humidity']  # Humidity
        
        # Display forecast data
        print(f"Date and Time: {timestamp}")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {weather_description}")
        print(f"Humidity: {humidity}%")
        print("-" * 40)
else:
    print(f"Error: {response.status_code} - {response.text}")