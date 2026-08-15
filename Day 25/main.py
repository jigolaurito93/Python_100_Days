import csv
import pandas

with open("Day 25/weather_data.csv", "r") as weather_data:
    weather_data_list = list(csv.reader(weather_data))
    temperatures = []
    for row in weather_data_list[1:]:
        temperatures.append(int(row[1]))
    print(temperatures)


# from pathlib import Path

# weather_file = Path(__file__).parent / "weather_data.csv"

# with weather_file.open() as weather_data:
#     weather_data_list = weather_data.readlines()

# print(weather_data_list)