def get_weather(city, api_key):
    """Fetch weather information for the given city."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            city_name = data['name']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            weather_desc = data['weather'][0]['description'].capitalize()
            humidity = data['main']['humidity']
            wind = data['wind']['speed']

            print("\n✅ Weather Data Retrieved Successfully!\n")
            print(f"🏙 City: {city_name}")
            print(f"🌡 Temperature: {temp}°C (Feels like {feels_like}°C)")
            print(f"☁️ Condition: {weather_desc}")
            print(f"💧 Humidity: {humidity}%")
            print(f"💨 Wind Speed: {wind} m/s\n")

        else:
            print("⚠️ City not found. Please check the name and try again.")

    except Exception as e:
        print("⚠️ Error connecting to the weather service:", e)
