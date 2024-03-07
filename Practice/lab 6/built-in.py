#Write a Python program with builtin function to multiply all the numbers in a list   math.lcm()

import functools

def multiply_numbers(numbers):
    result = functools.reduce(lambda x, y: x * y, numbers)
    return result

result = multiply_numbers([2, 3, 4, 5])
print(f"The product is: {result}")

#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

def count(words):

    lower_case = 0
    upper_case = 0
    for letter in words:
        if letter == letter.upper():
            upper_case += 1
        else:
            lower_case += 1
    print(f"Number of occureanse of upper case letters: {upper_case}")
    print(f"Number of occureanse of lower case letters: {lower_case}")

count("HelLo")

#Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def palindrome(strings):
    x = strings.lower()
    cleaned_string = ''
    for i in x:
        if i.isalnum():
            cleaned_string += i
    print(cleaned_string)

    
    if  cleaned_string == cleaned_string[::-1]:
        print(f"{strings} is palindrome")
    else:
        print(f"{strings} is not palindrome")

palindrome("Sit on a potato pan, Otis.")

#Write a Python program that invoke square root function after specific milliseconds.

import math
import time

def find_square_root(numder):
    squared_number = math.sqrt(numder)
    return squared_number

def delay(number, ms_time):
    time.sleep(ms_time/1000) # pause the execution of a program
    result = find_square_root(number)
    print(f"Square root of {number} after {ms_time} milliseconds:{result}")
    

delay(25100, 2123)

#Write a Python program with builtin function that returns True if all elements of the tuple are true.

def checking(tuples):
    result = all(tuples)
    print(result)
    
checking((True, True, False))