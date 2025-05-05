# Problem 1: 

# Write a Python program that prints "Hello, World!" to the console.
# print("Hello, World!")

# Problem 2: Add Two Numbers   (Topic: Variables & Arithmetic Operators)

# Write a Python program to add two numbers and print the result.
# a = 5
# b = 10
# sum = a + b
# print(sum)

# Problem 3: Swap Two Numbers  (Topic: Variables & Swapping)

# Write a Python program to swap two numbers without using a third variable.
# a = 10
# b = 20

# Swapping - We use Python’s multiple assignment feature to swap values: a, b = b, a.
# a, b = b, a  

# print("a =", a)
# print("b =", b)

# Problem 4: Check Even or Odd  (Topic: Conditional Statements)

# Write a Python program that takes a number as input and prints whether it is even or odd.
# num = int(input('Enter a number:'))

# % (modulo) finds the remainder when num is divided by 2.If remainder == 0, the number is even, otherwise odd.
# if num % 2 == 0: 
#     print(num, 'is even')
# else:
#     print(num, 'is odd')


# Problem 5: Find the Largest of Two Numbers  (Topic: Conditional Statements)

# Write a Python program to find the largest of two numbers.
# a = 15
# b = 10

# if a > b:
#     print(a, 'is the largest number')
# else:
#     print(b, 'is the largest number')


# Problem 6: Find the Largest of Three Numbers  (Topic: Conditional Statements)

# Write a Python program to find the largest of three numbers.
# a = 10
# b = 20
# c = 30

# if a > b and a > c:
#     print(a, 'is the largest number')
# elif b > a and b > c:
#     print(b, 'is the largest number')
# else:
#     print(c, 'is the largest number')


# Problem 7: Check if a Number is Positive, Negative, or Zero (Topic: Conditional Statements)

# Write a Python program that checks whether a given number is positive, negative, or zero.
# num = int(input('Enter a number: '))

# if num > 0:
#     print(num, 'is positive')
# elif num < 0:
#     print(num, 'is negative')
# else:
#     print('The number is zero')


# Problem 8: Sum of First N Natural Numbers   (Topic: Loops)

# Write a Python program to find the sum of the first N natural numbers.
# n = int(input('Enter a number: '))

# sum = 0   # Start with sum = 0
# for i in range(1, n + 1):    # Loop from 1 to n
#     sum += i    # Add the current number i to sum
# print('Sum:', sum)


# Problem 9: Factorial of a Number (Topic: Loops)

# Write a Python program to find the factorial of a given number.
# n = int(input('Enter a number: '))

# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i

# print('Factorial:', factorial)
# Explanation::
# The factorial of n is n * (n-1) * (n-2) ... * 1.
# We loop from 1 to n, multiplying each number.


# Problem 10: Reverse a Number  (Topic: Loops & Math)

# Write a Python program to reverse a given number.
# num = int(input('Enter a number: '))
# rev_num = 0

# while num > 0:
#     digit = num % 10            #  % 10 gives the last digit of num. Example: If num = 123, then 123 % 10 = 3.
#     rev_num = rev_num * 10 + digit    # Moves the previous digits left by multiplying by 10 and adds the new digit.
#     num //= 10                        # // 10 removes the last digit from num by integer division. Example: If num = 123, then 123 // 10 = 12.
# print('Reversed Number:', rev_num)


# Problem 11: Count Digits in a Number   (Topic: Loops)

# Write a Python program to count the number of digits in a given number.
# num = int(input('Enter a number: '))
# count = 0

# while num > 0:
#     num //= 10
#     count += 1

# print('Number of digits:', count)


# Problem 12: Sum of Digits of a Number  (Topic: Loops & Math)

# Write a Python program to find the sum of digits of a number.
# num = int(input('Enter a number: '))
# sum_digits = 0

# while num > 0:
#     sum_digits += num % 10
#     num //= 10

# print('Sum of digits:', sum_digits)


# Problem 13: Check if a Number is Palindrome  (Topic: Loops & Math)

# Write a Python program to check if a number is a palindrome (same when reversed).
# num = int(input('Enter a number: '))
# temp = num
# rev_num = 0

# while temp > 0:
#     digit = temp % 10
#     rev_num = rev_num * 10 + digit
#     temp //= 10

# if num == rev_num:
#     print(num, 'is a palindrome')
# else:
#     print(num, 'is not a palindrome')


# Problem 14: Check if a Year is a Leap Year  (Topic: Conditional Statements)

# Write a Python program to check whether a given year is a leap year.
# year = int(input('Enter a year: '))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, 'is a leap year')
# else:
#     print(year, 'is not a leap year')


# Problem 15: Print Fibonacci Series up to N Terms  Topic: (Loops & Recursion)

# Write a Python program to print the Fibonacci series up to N terms.
# n = int(input('Enter the number of terms: '))
# a, b = 0, 1

# for _ in range(n):
#     print(a, end=' ')
#     a, b = b, a + b


# Problem 16: Find the Power of a Number  (Topic: Math & Exponentiation)

# Write a Python program to calculate x^y (x raised to the power y).
# x = int(input('Enter the base: '))
# y = int(input('Enter the exponent: '))

# result = x ** y
# print('Result: ', result)   


# Problem 17: Convert Kilometers to Miles  (Topic: Unit Conversion)

# Write a Python program to convert kilometers to miles.
# km = float(input('Enter distance in kilometers: '))
# miles = km *  0.621371
# print('Distance in miles:', miles)


# Problem 18: Find the ASCII Value of a Character  (Topic: ASCII & Characters)

# Write a Python program to find the ASCII value of a character.
# char = input('Enter a character: ')
# ascii_value = ord(char)            # ord(char) gives the ASCII value of a character.
# print('ASCII value of', char, 'is', ascii_value)


# Problem 19: Find the Sum of Natural Numbers Using Recursion   (Topic: Recursion)

# Write a Python program to find the sum of the first N natural numbers using recursion.
# def sum_natural(n):
#     if n == 1:
#         return 1
#     return n + sum_natural(n - 1)

# n = int(input('Enter a number: '))
# print('Sum:', sum_natural(n))


# Problem 20: Reverse a String  (Topic: String Manipulation)

# Write a Python program to reverse a string.
# text = input('Enter a string: ')
# reversed_text = text[::-1]
# print('Reversed string:', reversed_text)



# Problem 21: Given an array containing n-1 unique numbers from 1 to n, find the missing number.
# def find_missing_number(arr, n):
#     expected_sum = n * (n + 1) // 2
#     actual_sum = sum(arr)
#     return expected_sum - actual_sum

# numbers = list(map(int, input('Enter numbers separated by spaces: ').split()))
# n = len(numbers) + 1
# print('Missing Number:', find_missing_number(numbers, n))

# i/o:
# Enter numbers separated by spaces: 1 2 3 5
# Missing Number: 4

