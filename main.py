from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "514854dcd25062c8b6309fd16ae3e34c"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    forecast = []
    city = None
    error = None

    if request.method == "POST":
        city = request.form["city"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            weather = {
                "city": city,
                "temp": round(data["main"]["temp"]),
                "feels_like": round(data["main"]["feels_like"]),
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"],
                "wind": round(data["wind"]["speed"] * 3.6)
            }

            forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric&cnt=5"
            forecast_response = requests.get(forecast_url)
            forecast_data = forecast_response.json()

            for item in forecast_data["list"]:
                forecast.append({
                    "date": item["dt_txt"][5:16],
                    "temp": round(item["main"]["temp"]),
                    "desc": item["weather"][0]["description"]
                })
        else:
            error = True

    return render_template("index.html", weather=weather, forecast=forecast, city=city, error=error)

if __name__ == "__main__":
    app.run(debug=True)