# Write a program to print numbers from 1 to 10 using a for loop.
for numbers in range(1, 11):
    print("The number is: ", numbers)


# Create a program that prints all even numbers between 1 and 50 using a while loop.
start_point = 1
ending_point = 50

while start_point <= ending_point:
    if(start_point % 2 == 0):
        print("The even number is: ", start_point)
    start_point +=1

# Write a program that prints the sum of all numbers from 1 to 100.
sum_of_numbers = 0
for number in range(1,101):
    sum_of_numbers += number
print("The sum of numbers is: ",sum_of_numbers)

# Write a program to print the multiplication table of any number entered by the user.
number = int(input("Enter a number:"))
for numbers in range(1,11):
    print(f"{number} * {numbers} = ", number * numbers)

# Write a Python program to find the factorial of a number using a loop.
number = int(input("Enter a number: "))
factorial = 1
for numbers in range(1,number + 1, 1):
    print(numbers)
    factorial *= numbers
print("The factorial of the number is: ",factorial)

# Create a program that prints the Fibonacci series up to n terms, where n is given by the user.
user_input = int(input("Enter a number:"))
sum = 0
first_number = 0
second_number = 1
print("The fibonnaci Series is: ", first_number,second_number)
while sum <  user_input:
    sum = first_number + second_number
    print(sum)
    first_number = second_number
    second_number = sum

# Write a program to reverse a given number using a while loop.
# Use a for loop to print all the elements of a list.
# Create a program that takes an integer from the user and prints all its divisors.
# Write a program to sum the digits of a number using a while loop.
