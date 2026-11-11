import csv

WEATHER_FILE = "./weather/weather_data.csv"

temperatures = []
with open(WEATHER_FILE, "r") as weather_data:
    data = csv.reader(weather_data)
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)