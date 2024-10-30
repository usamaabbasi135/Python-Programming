# Operators
# Write a program to calculate the area of a circle using the formula: Area = π * r^2.

import math
radius = input("Enter radius of the circle: ")
radius = int(radius)
print("The entered radius is: " , radius)
PI = math.pi
areaOfCircle = PI * radius * radius
print("The area of the circle is: ", areaOfCircle)

# Create a program to check if a number is even or odd.

user_input = input("Enter a number: ")
user_input = int(user_input)

even_odd = user_input % 2
if (even_odd == 0):
    print("The number is even")
else:
    print("The number is odd")