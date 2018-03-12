#!/usr/bin/env python3
"""modify the fruit list"""
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
l = len(fruit_list)
print(fruit_list)
response = input("Please name another fruit > ")
fruit_list.append(response)
print(response +" has bee added to the fruit list")
print(fruit_list)

