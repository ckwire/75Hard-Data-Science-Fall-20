import sys

try:
    with open('pi_di0its.txt') as file_object:
        contents = file_object.read()
        print(contents)
except FileNotFoundError as e:
    print("File error! Please try again.")
