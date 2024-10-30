# Write a Python program to swap two numbers.

first_number = 25
second_number = 35

print("Values before swaping: " , first_number, second_number)
temp_number = second_number
second_number = first_number
first_number = temp_number

print("Values after Swapping are: ", first_number,second_number)


# What will happen if you try to add a string and an integer? Write code to test it.
# We can only concatenate strings values. We can not concatenate string and integer value. We will get the typeError saying that can only concatenate str to str and not integer values can be concatenated with string.

myName = 'Usama Bin Hafeez Abbasi'
myAge = 25

print(myName + myAge)

# How do you declare a variable in Python? Create examples using integer, float, and string data types.
# There is no way to declar a variable in python. However when you assign the value to the variable, the variable is declared and inititalized at that moment.

valueForInteger= 23
valueForFloat = 34.321
valueForString = "My name is usama bin hafeez abbasi. I am currently working in Afiniti as Production Analyst"

print(valueForString)
print(type(valueForInteger),type(valueForFloat),type(valueForString))


# Write a program to input two numbers and print their sum.

firstNumber = input("Enter first Number: ")
secondNumber = input("Enter second Number: ")

firstNumber = int(firstNumber)
secondNumber = int(secondNumber)

print("The entered numbers are: ", firstNumber,secondNumber)
sum = firstNumber + secondNumber
print("The sum of the numbers is: ", sum)

# Write a program that converts temperature from Celsius to Fahrenheit

temperatureInCelsius = input("Enter the temperature: ")
temperatureInCelsius = float(temperatureInCelsius)

print("The temperature in celsius is: ", temperatureInCelsius)
temperatureInFahreinheit = (9/5) * temperatureInCelsius + 32

print("The temperature in Fahreinheit is: ", temperatureInFahreinheit)

# Define a constant in Python. Can you change it later? Show with an example.

# We can not define a constant in python. To indicate a constant value in python we use
# capital letters for the name of the variable to indicate it is constant value. We are not creating 
# constant but a variable which values can be changed.

MAX_AGE = 110

MAx_AGE = 90

# What happens if you assign the value of one variable to another variable? Demonstrate this
# The value is completely copied to the other variable when we assign the second variable the first 
# variable value
firstVariable = "My name is usama"
print("The value for the first variable is: ", firstVariable)
secondVariable = firstVariable
print("The value for the second variable is: ", secondVariable)

# Write a program to input a string from the user and output its length.

user_input = input("Enter a string value: ")
length_of_string = len(user_input)
print("The length of the value is: ", length_of_string)


# What is type casting? Convert an integer to a string and concatenate it with another string.

# Type casting means to convert one type to another type of data. Like converting a integer value to string. String to integer.

myAge = 50
myName = "Usama Bin Hafeez Abbasi"

myAgeString = str(myAge)


conMyAgeMyString = myName + myAgeString

print(conMyAgeMyString)

# Create a variable x and assign it a value of 5. Now multiply it by 10 and print the result

x = 5
x = x * 10
print (x)