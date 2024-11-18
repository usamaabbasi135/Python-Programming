# Write a program to take a user's name as input and greet them with their name.

user_name = input("Enter you name: ")
print("Welcome",user_name)

# Create a program that asks for the user's birth year and calculates their age.

current_year = 2024
user_entered_year = input("Enter your birth year: ")
user_entered_year = int(user_entered_year)

ageUser = current_year - user_entered_year
print("Your age is: ", ageUser)


# How can you take two inputs from the user in a single line? Write code to demonstrate this.

x,y = input ("Enter two values").split()
print("The value of first variable is: ", x)
print("The value of second variable is: ", y)

# Write a program that takes three numbers as input and prints their average.

first_value, second_value, third_value = input("Enter three numbers: ").split()
first_value = int(first_value)
second_value = int(second_value)
third_value = int(third_value)
average = (first_value + second_value + third_value)/3
print("The average of the numbers is: ", average)

# Accept a string from the user and print it in reverse.

string_value = input("Enter any string value:")
reversed_string_value = string_value[::-1]
print(reversed_string_value)

# Write a program to display your name and age in a formatted way using f-strings.

my_name = "Usama Bin Hafeez Abbasi"
my_age = 25

print(f'My name is {my_name} and my age is {my_age}')


# Create a program to take two numbers as input and print both their sum and product in a single line.

first_value,second_value = input("Enter two numbers").split()
first_value = int(first_value)
second_value = int(second_value)

sum = first_value + second_value
product = first_value * second_value

print(f"The sum of the number is {sum} and product is {product}")