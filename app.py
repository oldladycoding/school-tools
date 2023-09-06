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
    W1A = ["2023-08-28","2023-10-02","2023-11-06","2023-12-11","2024-01-29","2024-03-11","2024-04-15","2024-05-20"]
    W1B = ["2023-08-29","2023-10-03","2023-11-07","2023-12-12","2024-01-30","2024-03-12","2024-04-16","2024-05-21"]
    W1C = ["2023-08-30","2023-10-04","2023-11-08","2023-12-13","2024-01-31","2024-03-13","2024-04-17","2024-05-22"]
    W1D = ["2023-08-31","2023-10-05","2023-11-09","2023-12-14","2024-02-01","2024-03-14","2024-04-18","2024-05-23"]
    W1E = ["2023-09-01","2023-10-06","2023-11-10","2023-12-15","2024-02-02","2024-03-15","2024-04-19","2024-05-24"]

#Week 2
    W2A = ["2023-09-04","2023-10-09","2023-11-13","2023-12-18","2024-02-05","2024-03-18","2024-04-22","2024-05-27"]
    W2B = ["2023-09-05","2023-10-10","2023-11-14","2023-12-19","2024-02-06","2024-03-19","2024-04-23","2024-05-28"]
    W2C = ["2023-09-06","2023-10-11","2023-11-15","2023-12-20","2024-02-07","2024-03-20","2024-04-24","2024-05-29"]
    W2D = ["2023-09-07","2023-10-12","2023-11-16","2023-12-21","2024-02-08","2024-03-21","2024-04-25","2024-05-30"]
    W2E = ["2023-09-08","2023-10-13","2023-11-17","2023-12-22","2024-02-09","2024-03-22","2024-04-26","2024-05-31"]

#Week 3
    W3A = ["2023-09-11","2023-10-16","2023-11-20","2024-01-08","2024-02-12","2024-03-25","2024-04-29","2024-06-03"]
    W3B = ["2023-09-12","2023-10-17","2023-11-21","2024-01-09","2024-02-13","2024-03-26","2024-04-30","2024-06-04"]
    W3C = ["2023-09-13","2023-10-18","2023-11-22","2024-01-10","2024-02-14","2024-03-27","2024-05-01","2024-06-05"]
    W3D = ["2023-09-14","2023-10-19","2023-11-23","2024-01-11","2024-02-15","2024-03-28","2024-05-02","2024-06-06"]
    W3E = ["2023-09-15","2023-10-20","2023-11-24","2024-01-12","2024-02-16","2024-03-29","2024-05-03","2024-06-07"]

#Week 4
    W4A = ["2023-09-18","2023-10-23","2023-11-27","2024-01-15","2024-02-19","2024-04-01","2024-05-16","2024-06-10"]
    W4B = ["2023-09-19","2023-10-24","2023-11-28","2024-01-16","2023-02-20","2024-04-02","2024-05-17","2024-06-11"]
    W4C = ["2023-09-20","2023-10-25","2023-11-29","2024-01-17","2024-02-21","2024-04-03","2024-05-18","2024-06-12"]
    W4D = ["2023-09-21","2023-10-26","2023-11-30","2024-01-18","2024-02-22","2024-04-04","2024-05-19","2024-06-13"]
    W4E = ["2023-09-22","2023-10-27","2023-12-01","2024-01-19","2024-02-23","2024-04-05","2024-05-20","2024-06-14"]

#Week 5
    W5A = ["2023-09-25","2023-10-30","2023-12-04","2024-01-22","2024-02-26","2024-04-08","2024-05-13","2024-06-17"]
    W5B = ["2023-09-26","2023-10-31","2023-12-05","2024-01-23","2024-02-27","2024-04-09","2024-05-14","2024-06-18"]
    W5C = ["2023-09-27","2023-11-01","2023-12-06","2024-01-24","2024-02-28","2024-04-10","2024-05-15","2024-06-19"]
    W5D = ["2023-09-28","2023-11-02","2023-12-07","2024-01-25","2024-02-29","2024-04-11","2024-05-16","2024-06-20"]
    W5E = ["2023-09-29","2023-11-03","2023-12-08","2024-01-26","2024-03-01","2024-04-12","2024-05-17","2024-06-21"]

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

if __name__ == '__main__':
    app.run()