
#ex 1
class StringHandler:
    def __init__(self):
        self.string = None

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

handler = StringHandler()
handler.getString()
handler.printString()

#ex 2
class Shape:
    def __init__(self):
        pass

    def area(self):
       return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    
    def area(self):
        return self.length * self.length

square = Square(5)
print("Area of the Square:", square.area())

#ex 3
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

rectangle = Rectangle(4, 5)
print("Area of the Rectangle:", rectangle.area())

#ex 4
import math
# this line should be on the top. but i
# decided to show that it relates to this task
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, x_delta, y_delta):
        self.x += x_delta
        self.y += y_delta

    def dist(self, other_point):
        x_delta = self.x - other_point.x
        y_delta = self.y - other_point.y
        return math.sqrt(x_delta ** 2 + y_delta ** 2)

p1 = Point(2, 3)
p2 = Point(3, 3)
p1.show() 
p1.move(10, -10)
p1.show()  
p2.show()
print(f"Distance between points p1 and p2: {p1.dist(p2)}") 

#ex 5

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        
        self.balance += amount

    def withdraw(self, amount):
        
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def show_balance(self):
       
        print("Owner:", self.owner)
        print("Balance:", self.balance)

account = Account("Alice", 100)
account.deposit(50)
account.withdraw(25)
account.show_balance() 
account.withdraw(100)

#ex 6

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Original List:", numbers)
print("Prime Numbers:", prime_numbers)
