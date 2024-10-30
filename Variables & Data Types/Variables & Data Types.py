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

int_value = 23
float_value = 34.321
string_value = "My name is usama bin hafeez abbasi. I am currently working in Afiniti as Production Analyst"

print(type(int_value),type(float_value),type(string_value))

