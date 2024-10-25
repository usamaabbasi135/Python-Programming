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

