
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

# Example usage:
filter_prime([56, 345, 456, 5, 66, 89, 2])
print(primtlist)

#ex 5
import itertools # this line should be in the top. but i decided to show that it relates to this task 

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
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            print("True")
        else:
            print("False")
    return nums
        
has_33([1, 3, 2])

'''
has_33([1, 3, 1, 3]) 
has_33([3, 1, 3])
'''
