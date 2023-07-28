import tkinter as tk
import requests
import time
from geopy.geocoders import Nominatim


def getWeather(canvas):

    lat, lon = get_lat_lon(textfield.get())
    api = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) +"&appid=f63d6f1d6c753b6072345d4508b7638c"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] + 36000))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] + 36000))

    final_info = condition + "\n" + str(temp) + "C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + str(sunrise) + "\n" + "Sunset: " + str(sunset)
    label1.config(text=final_info)
    label2.config(text=final_data)


def get_lat_lon(city):
    geolocator = Nominatim(user_agent="location_generator")

    try:
        location = geolocator.geocode(city, exactly_one=True)

        if location is not None:
            latitude = location.latitude
            longitude = location.longitude
            return latitude, longitude
        else:
            return None, None
    except Exception as e:
        print(f"Error: {e}")
        return


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("Poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getWeather)


label1 = tk.Label(canvas, font=t)
label1.pack()

label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()