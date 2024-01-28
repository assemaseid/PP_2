#Boolean Values
 
print(10 > 9)       #ex1
answer:True

print(10 == 9)      #ex2
answer:False

print(10 < 9)       #ex3
answer:False

print(bool("abc"))  #ex3
answer:True

print(bool(0))      #ex4
answer:False


#PYTHON Operations

print(10 * 5)       #ex1

print(10 / 2)       #ex2

fruits = ["apple", "banana"]     #ex3
if "apple" in fruits:
    print("Yes, apple is a fruit")


if 5 != 10:                     #ex4
    print("5 and 10 is not equal")

if 5 == 10 or 4 == 4:           #ex5
    print("At least one of the statements is true")


#PYTHON Lists
    
fruit = ["apple", "banana", "cherry"]  #ex1
print(fruit[1])

fruit = ["apple", "banana", "cherry"]  #ex2
fruit[0] = "kiwi"

fruits = ["apple", "banana", "cherry"]  #ex3
fruits.append("orange")

fruits = ["apple", "banana", "cherry"]  #ex4
fruits.insert(1, "lemon")
print(fruits)

fruits = ["apple", "banana", "cherry"]  #ex5
fruits.remove("banana")

fruits = ["apple", "banana", "cherry"]  #ex6
print(fruits[-1])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]  #ex7
print (fruits [2:5])

fruits = ["apple", "banana", "cherry"]  #ex8
print ( len (fruits))



#PYTHON Tuples
fruits = ("apple", "banana", "cherry")  #ex1
print(fruits[0])

fruits = ("apple", "banana", "cherry")  #ex2
print(len(fruits))

fruits = ("apple", "banana", "cherry")  #ex3
print(fruits[-1])

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango") #ex4
print(fruits[2:5])


#PYTHON Sets

fruits = {"apple","banana", "cherry"}       #ex1
if "apple" in fruits:   
    print("Yes, apple is a fruit")

fruits = {"apple", "banana", "cherry"}       #ex2
fruits.add("orange")

fruits = {"apple", "banana", "cherry"}       #ex3
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

fruits = {"apple", "banana", "cherry"}       #ex4
fruits.remove("banana")

fruits = {"apple", "banana", "cherry"}       #ex5
fruits.discard("banana")


#PYTHON Dictionaries

car =  {                     #ex1
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.get("model"))

car =  {                     #ex2
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car["year"] = 2020

car =  {                     #ex3
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["color"] = "red"

car =  {                     #ex4
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.pop("model")

car =  {                     #ex5
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.clear()

#PYTHON if...else

a = 50                     #ex1
b = 10
if a > b:
    print("Hello World!")


a = 50                     #ex2
b = 10
if a != b:
    print("Hello World!")

a = 50                     #ex3
b = 10
if a == b:
    print("Yes")
else:
     print("No")


a = 50                      #ex4
b = 10
if a == b :
    print ("1")
elif a > b:
    print ("2")
else:
    print ("3")

c = 50
d = 40
if a == b and c == d:       #ex5
    print ("Hello")

if a == b or c == d:       #ex6
    print ("Hello")

if 5 > 2:                    #ex7
    print ("YES")

a = 2                        #ex8
b = 5
print("YES") if a == b else print ( "NO" )

a = 2                        #ex9
b = 50
c = 2
if a == c or b == c:
    print ("YES")

#PYTHON WHILE Loops
    
i = 1                       #ex1
while i < 6:
    print (i)
    i += 1

i = 1                       #ex2
while i < 6:
  if i == 3:
    break
  i += 1

i = 1                       #ex3
while i < 6:
  i +=1
  if i == 3:
    continue
  print(i)


i = 1                       #ex4
while i < 6:
   print(i)
   i +=1
else:
    print("i is no longer less than 6")


#Python For Loops
    
fruits = ["apple", "banana", "cherry"]       #ex1
for x in fruits:
    print (x)

fruits = ["apple", "banana", "cherry"]       #ex2
for x in fruits:
    if x == "banana":
      continue
    print (x)

for x in range (6):                  #ex3
    print (x)


fruits = ["apple", "banana", "cherry"]       #ex4
for x in fruits:
    if x == "banana":
      break
    print (x)

