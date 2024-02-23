import math

#ex 1
def converter(degrees):
    #radian = degrees * (math.pi/180)
    radian = math.radians(degrees)
    print(f"Output radian: {radian}")
    return radian

degree = float(input("Input Degree: "))
converter(degree)


#ex2
def area_of_tropezoid(height, base1, base2):
    area = height * ((base1 + base2)/2)
    print(f"Height:{height}")
    print(f"Base, first value: {base1}")
    print(f"Base, second value: {base2}")
    print(f"Expected Output: {area}")


area_of_tropezoid(5, 5, 6)


#ex3
def area_of_polygon(n_of_sides, l_of_side):
    regular_polygon = (n_of_sides / 4) * math.pow(l_of_side, 2) * (1 / math.tan(math.radians(180 / n_of_sides)))
    print(f"The area of the polygon is: {regular_polygon}")

input_number = float(input("Input number of sides:"))
input_length = float(input("Input the length of a side:"))
area_of_polygon(input_number, input_length)


#ex4
def area_of_parallelogram(length, height) :
    parallelogram = length * height
    print(f"Expected Output: {parallelogram}")

input_height = float(input("Height of parallelogram:"))
input_l = float(input("Length of base:"))
area_of_parallelogram(input_l,input_height)
    
