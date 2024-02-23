
#ex 1
def squares(N):
    for i in range(N): #or range(1, N + 1) если N влючительно
        yield i**2
    return N

for square in squares(5):
    print(square)

#ex 2
def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))
even_nums = list(even_numbers(n))
print("Even numbers from", n, "to 0:", end=" ")
print(", ".join(map(str, even_nums)))

#ex 3
def divisible_by_three_and_four(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for num in divisible_by_three_and_four(40):
    print(num)

#ex 4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

for square in squares(1, 5):
    print(square) 

#ex 5
def countdown_generator(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter a value for n: "))
list_nums = list(countdown_generator(n))
print("Countdown from", n, "to 0:", end=" ")
print(", ".join(map(str, list_nums)))

