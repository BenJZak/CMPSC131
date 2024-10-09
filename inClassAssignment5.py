#Sridatha Akhil. V and Ben Zakielarz

import math

def func(first_name, middle_name, last_name):
    if len(middle_name) == 1:
        middle_name += "."
    print(f"Hello {first_name} {middle_name} {last_name}!")

func("Benjamin", "J", "Zakielarz")

def circle_area(radius):
    for i in range(10):
        area = math.pi * radius**2
        print(f"{radius} - {round(area, 3)}")
        radius += 1
circle_area(1)

def circle_circumference(radius):
    return(2*math.pi*radius)

radius = int(input("Enter the radius of a circle you'd like to calculate the circumference for: "))
print(round(circle_circumference(radius), 3))