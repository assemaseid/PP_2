#PYTHON SYNTAX
print("Hello World") #ex 1

if 5 > 2:            #ex 2
 print("YES")



#PYTHON Comment
#This is a comment   ex 1
 
"""                  ex 2
This is a comment
written in 
more than just one line
"""


#PYTHON Variables
carname = "Volvo"    #ex 1

x = 50               #ex 2

x = 5                #ex 3
y = 10
print (x + y)

x = 5                #ex 4
y = 10
z = x + y
print (z)

x, y, z = "Orange", "Banana", "Cherry"       #ex 5

x = y = z = "Orange"           #ex 6

def myfunc() :                 #ex 7
 global x
 x = "fantastic"



#PYTHON Data Types
# what data type would that be?
x = 5                          #ex 1
print (type (x))
#Answer: int

x = "Hello World"              #ex 2
print (type (x))
#Answer: str

x = 20.5                       #ex 3
print (type (x))
#Answer: float

x = ["apple", "banana", "cherry"]       #ex 4
print (type (x) )
#Answer: list

x = ("apple", "banana", "cherry")       #ex 5
print (type (x) )
#Answer: tuple

x = {"name" : "John", "age" : 36}       #ex 6
print (type (x) )
#Answer: dict

x = True                                #ex 7
print (type (x))
#Answer: bool


#PYTHON Numbers
#Insert the correct syntax to convert x into a floating point number.
x = 5                      #ex 1
x = float (x)
print(x)

x = 5.5                    #ex 2
x = int (x)
print(x)

x = 5                      #ex 3
x = complex (x)
print(x)


#PYTHON Strings

x = "Hello World"           #ex 1
print ( len (x))

txt = "Hello World"         #ex 2
x = txt [0]

txt = "Hello World"         #ex 3
x = txt [2:5]

txt = " Hello World "       #ex 4
x = txt.strip()

txt = "Hello World"         #ex 5
txt = txt.upper ()

txt = "Hello World"         #ex 6
txt = txt. lower ()

txt = "Hello World"         #ex 7``
txt = txt. replace ("H", "J")


age = 36                    #ex 8
txt = "My name is John, and I am {}"
print (txt. format (age) ) 