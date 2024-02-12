import math
a, b = float(input('Input number of sides: ')), float(input('Input the length of a side: '))

apothem = b/(2*math.tan(math.pi / a)) 
perimeter = b*a
S = apothem * perimeter / 2
print("The area of the polygon is:", round(S))