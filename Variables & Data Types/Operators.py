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


# What is the result of 7 // 2 in Python? Write a code to experiment with floor division.

division_number_result = 3.5 / 2
floor_division_number_result = 3.5 // 2

print("The result when two number are divided simply is: ", division_number_result)
print("The result when two number are floor division is: ", floor_division_number_result)


# Write a Python program that uses both increment (+=) and decrement (-=) operators.

initial_temperature_of_room = 20

user_choice = input("Should we increase or decrease the temperature?Press(I/D):")

if (user_choice == 'I'):
    initial_temperature_of_room += 1
    print("Increased Temperature is: ", initial_temperature_of_room)
elif(user_choice == 'D'):
    initial_temperature_of_room -= 1
    print("Decreased Temperature is: ", initial_temperature_of_room)


# Write a program that accepts a number from the user and prints the square and cube of that number.

user_input_number = input("Enter a number: ")
user_input_number = int(user_input_number)

square_of_number = user_input_number ** 2
cube_of_number = user_input_number ** 3

print(f"The square of the number is {square_of_number} and cube of the number is {cube_of_number}")

# Use logical operators to check if a number lies between 10 and 50.

user_input_number = input("Enter a number: ")
user_input_number = int(user_input_number)

decision_value = user_input_number >= 10 and user_input_number <= 50

if(decision_value == 1):
    print("The number lies between 10 and 50")
else:
    print("The number does not lie between 10 and 50")


# Write a Python code to check if two numbers are equal using a comparison operator.

first_number = input("Enter first number: ")
second_number = input("Enter Second Number: ")

first_number = int(first_number)
second_number = int(second_number)

if (first_number == second_number):
    print("The numbers are equal")

else:
    print("The numbers are not equal")

# Write a program to evaluate True or False and True. What is the result? Why?
# The resut of the condition is true because the comparison operator are evaluated from left
# to right. The process will be that the first condition is true. It will be evaluted with the or
# operator and the second conditon is false so the overall result of the first two conditions will be
# true. Then this true value will be AND with the third condtion which is also true. So the overall
# result of the expression will be true.
first_number = 20
second_number = 10
third_number = 40

if (first_number > second_number or second_number > third_number and third_number > first_number):
    print("The result of the condition was true")
else:
    print("The resutl of the condition was false")


#  Using bitwise operators, write a program to perform bitwise AND, OR, and XOR operations on 
# two numbers.


first_number = input("Enter first Number: ")
second_number = input("Enter second number: ")

first_number = int(first_number)
second_number = int(second_number)

bitwise_and_result = first_number & second_number

bitwise_or_result = first_number | second_number

bitwise_xor_resutl = first_number ^ second_number

print(f"The resutl of bitwise operators are: AND {bitwise_and_result} OR {bitwise_or_result} XOR {bitwise_xor_resutl}")


# Write a program to compute a**b (exponentiation).

first_number = input("Enter first number ")
second_number = input("Enter second Number ")

first_number = int(first_number)
second_number = int(second_number)

exponential_result = first_number ** second_number

print(exponential_result)