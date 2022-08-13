import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=2854010aff2f442351d8c0ab2e40c279"
    json_data = requests.get(api).json()
    temperature = int(json_data['main']['temp'] - 273.15)
    condition = json_data['weather'][0]['main']
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    srise = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise'] + 28800))
    sset = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset'] + 28800))

    final_info = condition + '\n' + str(temperature) + "°C"
    final_data = 'Pressure: ' + str(pressure) +  "Hg" + '\n' + 'Humidity: ' + str(humidity) + "%" + '\n' + 'Sunrise: ' + srise + '\n' + 'Sunset: ' + sset
    label1.config(text=final_info)
    label2.config(text=final_data)

#canvas for rectangular area
canvas = tk.Tk()
canvas.geometry("600x600")
canvas.title("Weather App")
#font
f = ("vendetta", 14, "italic")
t = ("helvetica", 30, "bold")

#textfields for data entry
textfield = tk.Entry(canvas, justify='center', font=t)
textfield.pack(pady=24)
textfield.focus()
textfield.bind('<Return>', getWeather)


label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()