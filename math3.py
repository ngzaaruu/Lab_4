import math

a = int(input("Input number of sides: "))
b = int(input("Input the length of a side: "))
c = (a * pow(b,2)) / (4 * math.tan(math.pi / a))

print(f"The area of the polygon is: {c:.f2}") 