import requests
import json
import re


from flask import Flask, render_template, request

# Configure application

app = Flask(__name__)


#Main pge showing
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/construction')
def construction():
    return render_template("construction.html")

@app.route('/weather', methods=['GET', 'POST'])
def weather():

#Initiate all the variables
    city = None
    temperature = None
    weather = None
    feel = None
    clothing = None


#Get input - city name -  from dorpdown form
    if request.method =='POST':
        city = request.form.get("city")

    API_KEY = "46e914b64cad62ed6a7405d08a9b999a"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

#Insert user input in the API request
    request_url = f"{BASE_URL}q={city}&lang=fr&units=metric&appid={API_KEY}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = round(data["main"]["temp"],1)
        feel = round(data["main"]["feels_like"],1)

#determine which clothing to wear according to temperature criteria
        clothing = "Choice"
        if temperature >= 20.0:
            clothing = "level 1"
        elif 16.0 <= temperature <=19.9:
            clothing = "level 2"
        elif 12.0 <= temperature <= 15.9:
            clothing = "level 3"
        elif temperature <= 11.9:
            clothing = "level 4"
        return render_template("weather.html", weather=weather, temperature=temperature, feel=feel, clothing=clothing, city=city)

    else:
        return render_template("apology.html")

@app.route('/menu', methods=['GET', 'POST'])
def menu():

#Defines the dates for each menu accodring to weeks
#Week 1
    W1A = ["2024-08-26","2024-09-30","2024-11-04","2024-12-09","2025-01-27","2025-03-10","2025-04-14","2025-05-19"]
    W1B = ["2024-08-27","2024-10-01","2024-11-05","2024-12-10","2025-01-28","2025-03-11","2025-04-15","2025-05-20"]
    W1C = ["2024-08-28","2024-10-02","2024-11-06","2024-12-11","2025-01-29","2025-03-12","2025-04-16","2025-05-21"]
    W1D = ["2024-08-29","2024-10-03","2024-11-07","2024-12-12","2025-01-30","2025-03-13","2025-04-17","2025-05-22"]
    W1E = ["2024-08-30","2024-10-04","2024-11-08","2024-12-13","2025-01-31","2025-03-14","2025-04-18","2025-05-23"]

#Week 2
    W2A = ["2024-09-02","2024-10-07","2024-11-11","2024-12-16","2025-02-03","2025-03-17","2025-04-21","2025-05-26"]
    W2B = ["2024-09-03","2024-10-08","2024-11-12","2024-12-17","2025-02-04","2025-03-18","2025-04-22","2025-05-27"]
    W2C = ["2024-09-04","2024-10-09","2024-11-13","2024-12-18","2025-02-05","2025-03-19","2025-04-23","2025-05-28"]
    W2D = ["2024-09-05","2024-10-10","2024-11-14","2024-12-19","2025-02-06","2025-03-20","2025-04-24","2025-05-29"]
    W2E = ["2024-09-06","2024-10-11","2024-11-15","2024-12-20","2025-02-07","2025-03-21","2025-04-25","2025-05-30"]

#Week 3
    W3A = ["2024-09-09","2024-10-14","2024-11-18","2025-01-06","2025-02-10","2025-03-24","2025-04-28","2025-06-02"]
    W3B = ["2024-09-10","2024-10-15","2024-11-19","2025-01-07","2025-02-11","2025-03-25","2025-04-29","2025-06-03"]
    W3C = ["2024-09-11","2024-10-16","2024-11-20","2025-01-08","2025-02-12","2025-03-26","2025-04-30","2025-06-04"]
    W3D = ["2024-09-12","2024-10-17","2024-11-21","2025-01-09","2025-02-13","2025-03-27","2025-05-01","2025-06-05"]
    W3E = ["2024-09-13","2024-10-18","2024-11-22","2025-01-10","2025-02-14","2025-03-28","2025-05-02","2025-06-06"]

#Week 4
    W4A = ["2024-09-16","2024-10-21","2024-11-25","2025-01-13","2025-02-17","2025-03-31","2025-05-05","2025-06-09"]
    W4B = ["2024-09-17","2024-10-22","2024-11-26","2025-01-14","2025-02-18","2025-04-01","2025-05-06","2025-06-10"]
    W4C = ["2024-09-28","2024-10-23","2024-11-27","2025-01-15","2025-02-19","2025-04-02","2025-05-07","2025-06-11"]
    W4D = ["2024-09-19","2024-10-24","2024-11-28","2025-01-16","2025-02-20","2025-04-03","2025-05-08","2025-06-12"]
    W4E = ["2024-09-20","2024-10-25","2024-11-29","2025-01-17","2025-02-21","2025-04-04","2025-05-09","2025-06-13"]

#Week 5
    W5A = ["2024-09-23","2024-10-28","2024-12-02","2025-01-20","2025-02-24","2025-04-07","2025-05-12","2025-06-16"]
    W5B = ["2024-09-24","2024-10-29","2024-12-03","2025-01-21","2025-02-25","2025-04-08","2025-05-13","2025-06-17"]
    W5C = ["2024-09-25","2024-10-30","2024-12-04","2025-01-22","2025-02-26","2025-04-09","2025-05-14","2025-06-18"]
    W5D = ["2024-09-26","2024-10-31","2024-12-05","2025-01-23","2025-02-27","2025-04-10","2025-05-15","2025-06-19"]
    W5E = ["2024-09-27","2024-11-01","2024-12-06","2025-01-24","2025-02-28","2025-04-11","2025-05-16","2025-06-20"]

#Establish variables
    menu = None
    date_jour = ""

#Get date from user with calendar form

    if request.method =='POST':
        date_jour= request.form.get("date_jour")

#check if input date is included in one of the arrays
        if date_jour in W1A:
            menu = "W1A"
        elif date_jour in W1B:
            menu = "W1B"
        elif date_jour in W1C:
            menu = "W1C"
        elif date_jour in W1D:
            menu = "W1D"
        elif date_jour in W1E:
            menu = "W1E"
        elif date_jour in W2A:
            menu = "W2A"
        elif date_jour in W2B:
            menu = "W2B"
        elif date_jour in W2C:
            menu = "W2C"
        elif date_jour in W2D:
            menu = "W2D"
        elif date_jour in W2E:
            menu = "W2E"
        elif date_jour in W3A:
            menu = "W3A"
        elif date_jour in W3B:
            menu = "W3B"
        elif date_jour in W3C:
            menu = "W3C"
        elif date_jour in W3D:
            menu = "W3D"
        elif date_jour in W3E:
            menu = "W3E"
        elif date_jour in W4A:
            menu = "W4A"
        elif date_jour in W4B:
            menu = "W4B"
        elif date_jour in W4C:
            menu = "W4C"
        elif date_jour in W4D:
            menu = "W4D"
        elif date_jour in W4E:
            menu = "W4E"
        elif date_jour in W5A:
            menu = "W5A"
        elif date_jour in W5B:
            menu = "W5B"
        elif date_jour in W5C:
            menu = "W5C"
        elif date_jour in W5D:
            menu = "W5D"
        elif date_jour in W5E:
            menu = "W5E"

        elif date_jour not in W1A + W1B + W1C + W1D + W1E + W2A + W2B + W2C + W2D + W2E + W3A + W3B + W3C + W3D + W3E + W4A + W4B + W4C + W4D + W4E + W5A + W5B + W5C + W5D + W5E:
                menu = ""
    return render_template("menu.html", menu=menu, date_jour=date_jour)

@app.route('/chart', methods=['GET', 'POST'])
def chart():

#Initiate all the variables
    city = None
    temperature = None
    weather = None
    feel = None
    time = None


#Get input - city name -  from dorpdown form
    if request.method =='POST':
        city = request.form.get("city")

    API_KEY = "46e914b64cad62ed6a7405d08a9b999a"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

#Insert user input in the API request
    request_url = f"{BASE_URL}q={city}&lang=fr&units=metric&appid={API_KEY}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = round(data["main"]["temp"],1)
        feel = round(data["main"]["feels_like"],1)

#determine recommended time outside according to temperature felt criteria
        time = "Choice"
        if -15.9 <= feel <= 29.9:
            time = "green"
        elif 30.9 <= feel <= 39.9:
            time = "yellow"
        elif -27.9 <= feel <= -16.0:
            time = "yellow"
        elif 40.0 <= feel <= 47.9:
            time = "orange"
        elif -81.9 <= feel <= -28.9:
            time = "red-1"
        elif 46.9 <= feel <= 58.0:
            time = "red-2"
        return render_template("chart.html", weather=weather, temperature=temperature, feel=feel, time=time, city=city)

    else:
        return render_template("apology.html")

if __name__ == '__main__':
    app.debug = True
    app.run()