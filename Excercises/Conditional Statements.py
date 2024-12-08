# Write a Python program to check if a number is positive, negative, or zero.

number = int(input("Enter a number:"))

if(number > 0):
    print("Number is positive")
elif(number == 0):
    print("Number is 0")
else:
    print("Number is negative")


# Create a program to check if a given year is a leap year or not.
year = int(input("Enter year:"))

if (year % 4 == 0 ):
    print("The year is a leap year")
else:
    print("The year is not a leap year")

#write a program that asks for a number and checks whether it is divisible by both 3 and 5.
number = int(input("Enter any number:"))
if(number % 3 == 0 and number % 5 == 0):
    print("The number is divisible by both 3 and 5")
else:
    print("The number is not divisible")

# Create a program to take a character input from the user and check if it is a vowel or consonant.

character_value = input("Enter any character:")
if(character_value == 'a' or character_value == 'e' or character_value== 'i' or character_value == 'o' or character_value == 'u' ):
    print("The character is a vowel")
else:
    print("Character is consonant")

# Write a program that asks the user for their marks and prints the grade based on specific ranges.

marks = int(input("Enter your marks:"))

if marks >=  95 and marks <= 100:
    print("your grade is A+")
elif marks >= 90 and marks <= 94:
    print("Your grade is A")
elif marks >= 85 and marks <= 89:
    print("Your grade is B+")
elif marks >= 80 and marks <= 84:
    print("Your grade is B")
elif marks >= 75 and marks <= 79:
    print("Your grade is C+")
elif marks >= 70 and marks <= 74:
    print("Your grade is C")
elif marks >= 65 and marks <= 69:
    print("Your grade is D+")
elif marks >= 60 and marks <= 64:
    print("Your grade is D")
else:
    print("Your grade is F")

# Write a Python program to check if a number is prime.

number = int(input("Enter a number: "))

temp = 0
for x in range(2, int(number / 2)):
     if(number % x == 0):
         temp = 1

if (temp == 1):
    print("Not a prime number")
else:
    print("The number is prime")


# Create a program to determine if a number is even, odd, or zero.

number = int(input("Enter a number:"))

if number > 0:
   if (number == 0):
    print("The number is 0")
   elif (number % 2 == 0):
    print("The number is even")
   else:
    print("The number is odd")
else:
    print("The number is negative")

# Write a program that accepts a username and password and grants access if they are correct, otherwise denies access.

user_name = 'Usama Bin Hafeez Abbasi'
password = 'ilove6662'

u_name = input("Enter user name:")
pass_word = input("Enter password:")

if u_name == user_name and pass_word == password :
    print("Access granted")
else:
    print("Access denied")


# Write a Python program that checks if a given string is a palindrome.

string_value = input("Enter any string:")
reverse_string_value = string_value[::-1]

if(string_value.lower() == reverse_string_value.lower()):
    print("This is a palindrome string")
else:
    print("This is not a palindrome string")

# Create a program that takes three numbers as input and prints the largest of them
number_1,number_2,number_3 = input("Enter three numbers:").split()
number_1 = int(number_1)
number_2 = int(number_2)
number_3 = int(number_3)
largest_number = number_1

if(largest_number < number_2):
    largest_number = number_2
if(largest_number < number_3):
    largest_number = number_3
print("The largest number is: ", largest_number)
    
