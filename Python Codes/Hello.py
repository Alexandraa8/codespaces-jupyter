# Code1
x = "Hello"
y = "My name is Alexandra"

print (x)
print (y)

# Code2
if 5 < 6:
    print("Six is greater than five")

# Code3
myVar="Alexandra"
myVar2="Alex"

#Code4
x, y, z = "Cherry", "Apple", "Banana"
print(x)
print(y)
print(z)

#or

x = y = z = "Cherry"
print(x)
print(y)
print(z)

#Code5
fruits = ["Cherry", "Apple", "Banana"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Code6 
x = "Ich mag Hasen"
print(x)

#Code7
x = "Ich"
y = "mag"
z = "Hasen"
print(x)
print(y)
print(z)

#Code8
x = 5
y = 5
print(x + y)

#Code9
x = 5
y = 5
print(5*5)

#Code10
#if-Anweisungen
a = 50
b = 100
if a < b:
    print("b is greater than a")

#Code11
#if the previous conditions were not true, then try this condition
a = 50
b = 50
if a > b:
        print("a is greater than b")
elif a == b:
        print("a and b are equal")

#Code12
#else
a = 50
b = 100
if a > b:
      print("a is greater than b")
else:
      print("b is greater than a")

#Code13
#if and else in the same line
a = 50
b = 100
print ("50") if a > b else print("100")

#Code14
#range
for x in range(8):
      print(x)
#other example
for y in range(4, 8):
      print(y)

#Code15
for z in range(8):
     if z == 4: break
else:
     print("Fertig!")

#Code16
#Array
cars = ["Mercedes", "BMW", "Audi"]

x = cars[0]
print(x)

#Code17
cars = ["Mercedes", "BMW", "Audi"]

y = len(cars)
print(y)

#Code18
cars = ["Mercedes", "BMW", "Audi"]

for x in cars:
      cars = x
      print(x)

#Code19
#Automarke hinzufügen
cars = ["Mercedes", "BMW", "Audi"]

cars.append("Porsche")
print(cars)

#Code20
#Automarke entfernen
cars = ["Mercedes", "BMW", "Audi"]
cars.pop(1)
print(cars)

#Code21
#Python Math
y = min(7, 14, 21)
x = max(7, 14, 21)

print(x)
print(y)

#Code22
#abs
x = abs(-8.56)

print(x)

#Code23
#pow
p = pow(4, 5)

print(p)

#Code24
#sqrt
import math

s = math.sqrt(64)

print(s)

#Code25
#pi
import math

p = math.pi
print(p)

#Code26
#JSON
import json

x = '{"name": "Alexandra", "age": 19, "city": "Kirchardt" }'

y = json.loads(x)
print(y["name"])

#Code27
#lambda
x = lambda a: a + 10
print(x(5))

#Code28
x = lambda a, b, c: a + b + c
print(x(8, 7, 2))

#Code29
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(4)

print(mydoubler(12))

#Code30
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(4)

print(mydoubler(11)) 
print(mytripler(11))

#Code31
from random import randrange
n = 10
a = [randrange(1, 10) for i in range(n)]
print(a)

#Code32
A = [1, 2, 3, 4, 5]
A[2:4] = [7, 8, 9]
print(A)

#Code33
A = [1, 2, 3, 4, 5, 6, 7]
A[::-2] = [10, 20, 30, 40]
print(A)









