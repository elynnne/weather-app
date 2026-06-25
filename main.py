import requests

API_KEY = "514854dcd25062c8b6309fd16ae3e34c"
city = input("Enter city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
data=response.json()

if data["cod"] == 200:
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity= data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print(f"\n📍 Weather in {city}:")
    print(f"🌡️ Temperature: {temp}°C")
    print(f"🌬️  Feels like: {feels_like}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"☁️ Description: {description}")

    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric&cnt=5"
    forecast_response = requests.get(forecast_url)
    forecast_data = forecast_response.json()

    print(f"\n📅 5-Day Forecast for {city}:")
    for item in forecast_data["list"]:
        date = item["dt_txt"]
        temp_f = item["main"]["temp"]
        desc_f= item["weather"][0]["description"]
        print(f"{date}: {temp_f}°C, {desc_f}")
else:
    print("City not found try again please.")
