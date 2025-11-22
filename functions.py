# def greet():
#     print("Hello!")
    
# greet()

def say_goodbye():
    print("Goodbye!")
    print("See you later!")
    

#all it multiple times
say_goodbye()
say_goodbye()
say_goodbye()

def check_weather():
    temperature = 32
    if temperature > 30:
        print("It's hot!")
    else:
        print("Nice weather!")
        
#use the function
check_weather()

# def greet(name):
#     print(f"Hello, {name}")
    
# greet(name="Dave")
# greet(name="Alice")

# def greet(first_name, last_name):
#     print(f"Hello, {first_name} {last_name}")
    
# greet(last_name="Alice", first_name="Dave")

# def greet(first_name="John", last_name = "David"):
#     print(f"Hello, {first_name} {last_name}")
    
# # greet(last_name="Meda")
# greet()

# def calculate_total(price, tax_rate, discount):
#     tax = price * tax_rate
#     final_price = price + tax - discount
#     print(f"Total: ${final_price}")

# # Order matters!
# calculate_total(price=100, tax_rate=0.08, discount=10)  # $98



# def create_profile(name, age, city):
#     print(f"{name}, {age}, from {city}")

# # Positional arguments (order matters)
# create_profile("Alice", 25, "NYC")

# # Keyword arguments (order doesn't matter)
# create_profile(city="NYC", age=25, name="Alice")
# create_profile(name="Bob", city="LA", age=30)

# discount= 20

# def calculate_total(price):
    
#     #Default values
#     tax_rate = 0.08
#     discount = 10
    
#     #caluculator

#     tax = price * tax_rate
#     final_price = price + tax - discount
    
#     #Print the final price
#     print(f"Total: ${final_price}")
    
# calculate_total(price=100) 

# print(discount)   

# def add_print(a, b):
#     print(a+b)
    
# add_print(a=5, b=10)

# def add_return(a, b):
#     return a + b

# result = add_return(a=5, b=10)

# def calculate_area(width, height):
#     area = width * height
#     return area

# # Store the returned value
# room_area = calculate_area(10, 12)
# print(f"Room size: {room_area} sq ft")  # Room size: 120 sq ft


# def simple_function():
#     numbers = [1,2,3,4,5]
#     first_number = numbers[0]
#     last_number = numbers[-1]
#     return first_number, last_number

# f, l = simple_function()

# print(f)
# print(l)

# import math

# math.sqrt(16)

# from math import sqrt, pi
# sqrt(16)

# import random

# number = random.randint(1, 10)
# choice = random.choice(["apple", "banana", "orange"])

import datetime

today = datetime.date.today()
print(today)


# import os

# current_dir = os.getcwd()
# print(current_dir)

# #JSON data

# import json
# data = {"name": "Alice", "age": 30}
# json_string = json.dumps(data)


# import math
# result = math.sqrt(16)

# #Import specific functions
# from math import sqrt, pi
# result = sqrt(16)
# circle_area = pi * radius ** 2
#import pandas as pd
# import requests

# # We need coordinates to get weather data
# latitude = 48.85   # Paris latitude
# longitude = 2.35   # Paris longitude

# # Build the API URL with our parameters
# url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# # Make the request
# response = requests.get(url)
# data = response.json()

# print(data)

# type(data)

import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

#Get Temperature for different cities
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)


print(f"Paris: {paris_temp}°C")
print(f"London : {london_temp}°C")
print(f"Tokyo: {tokyo_temp} °C")





