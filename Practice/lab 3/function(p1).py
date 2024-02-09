#ex 1
def convert(grams):       
    ounces = 28.3495231 * grams
    return ounces

result = convert(100)
print(result)

#ex 2
def temp(Fahrenheit):
    C = (5 / 9) * (Fahrenheit - 32)
    return C

centigrade = temp(98)
print(int(centigrade))

#ex 3
def solve(numheads, numlegs):

    numChickens = (4 * numheads - numlegs) / 2
    numRubbit = numheads - numChickens
    print(numChickens)
    print(numRubbit)

solve(35, 92)

#ex 4
def filter_prime(numlist):
    global primtlist
    primtlist = []

    for num in numlist:
        if num <= 1:
            print(f"{num} is not a prime")
        else:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primtlist.append(num)

filter_prime([56, 345, 456, 5, 66, 89, 2])
print(primtlist)

#ex 5
import itertools 
# this line should be in the top. but i
# decided to show that it relates to this task 

def permutation(getstring):
    perms = list(itertools.permutations(getstring))
    print(perms)
    
getstring = input("string: ")
permutation(getstring)


# ex 6
def inverse(sentence):
    make_list = sentence.split()
    make_list.reverse()
    reverse_order = ' '.join(make_list)
    return reverse_order

sentence = input("Write a sentence: ")
inverse_sentence = inverse(sentence)
print(inverse_sentence)


# ex 7
def has_33(nums):
    for i in range(len(nums) - 1): # because 1st index is 0
        if nums[i] == 3 and nums[i + 1] == 3:
            return True    
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))


# ex 8

def spy_game(nums):
    i = 0
    while i < len(nums) - 2:
        if nums[i] == 0 and nums[i+1] < 7 and nums[i+2] == 7:
           return True
        elif nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
        elif nums[i] == 0 and nums[i+1] == 7 and nums[i+2] == 0:
           return True
        i += 1
    return False

print(spy_game([1,2,4,0,0,7,5]))  #True
print(spy_game([1,0,2,4,0,5,7]))  # True
print(spy_game([1,7,2,0,4,5,0]))  # False
print(spy_game([1,0,0,7,5]))  # True
print(spy_game([2, 4, 0, 8 ,9 ,0, 0, 7, 0]))

# ex 9
def calculate(radius):
    radius **= 3
    volium = 4/3 * 3.1415926536 * radius
    print(volium)

calculate(10)

# ex10
def numbers(numlist):
    newlist = []
    for i in numlist:
        if i not in newlist:
            newlist.append(i)
    print(newlist)
    return newlist

numbers([1, 1, 3, 4, 3, 4, 6,2,2])
 
# ex11


def palindrome(word_or_phrase):
    cleaned_word = word_or_phrase.replace(" ", "").lower()
    word_list = list(cleaned_word)
    word_list.reverse()
    reversed_word = ''.join(word_list)
    
    if cleaned_word == reversed_word:
        print(f"{word_or_phrase} is a palindrome.")
    else:
        print(f"{word_or_phrase} is not a palindrome.")
    
    return reversed_word

palindrome("A Santa at NASA")

# ex12
def histogram(number):
    i = 0
    while i < len(number):
        num = number[i]
        print('*' * num)
        i += 1

histogram([4, 9, 7])

#ex 13
import random
# this line should be in the top. but i
# decided to show that it relates to this task 

def guess_the_number():
    print("Hello! What is your name?")
    name = input("Your Name: ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    number_to_guess = random.randrange(1, 20)
    guesses = 0

    while guesses < 5:
        guess = int(input("Take a guess: "))
        guesses += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break

    if guesses == 5:
        print(f"Sorry, {name}, you didn't guess my number. The number was {number_to_guess}.")

guess_the_number()