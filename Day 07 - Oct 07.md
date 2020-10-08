## OCTOBER 7th 2020 - DAY 7 - DAILY LOG ##

* What to do today?

Files anybody?

```python
#working with Files & applying except handling from yesterday.

try:
    with open('pi_di0its.txt') as file_object:
        contents = file_object.read()
        print(contents)
except FileNotFoundError as e:
    print("File error! Please try again.")

```


* reference: 
    * [Intermediate Python Programming Course - freecodecamp.org](https://youtu.be/HGOBQPFzWKo?t=7448)
    * [Chapter 8 – Reading and Writing Files](https://automatetheboringstuff.com/chapter8/)


