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

#Code34
#if else Anweisungen
wert = 9
if wert < 5:
    print('Wert ist kleiner als 5')
elif wert == 5:
    print('Wert ist exakt 5')
else:
    print('Wert ist größer als 5')

#Code35
wert = 9
if wert < 5:
    print('Wert ist kleiner als 5')
else:
    print('Wert ist größer als 4')

#Code36
vornamen = ['Alex', 'Lisa', 'Lukas']
for einzelwert in vornamen:
     if einzelwert == "Alex":
            print("Ich")
else:
            print(einzelwert)
print
("nach der for-Schleife")

#Code37
vornamen = ['Alex', 'Lisa', 'Lukas']

nummer = 0
for einzelwert in vornamen:
    print(nummer, einzelwert)
    nummer += 1

#Code38
import random
lottozahlen = []
lottozahlen.extend(range(1,50))
random.shuffle(lottozahlen)
for x in range(6):
    print(lottozahlen[x])

#Code39
#if.. else
number = 5

# äußeren
if number >= 0:
    # inneren
    if number == 0:
      print('Number is 0')
    
    # inneren
    else:
        print('Number is positive')
#äußeren
else:
    print('Number is negative')

#Code40
# Hier Link: https://webtigerjython.ethz.ch/?prog=https://www.tjgroup.ch/progs/gp/Gp7a.py
from gpanel import *

makeGPanel(-30, 30, 0, 60)

x = -30
while x <= 30:
    if x <= 0:
        setColor("magenta")
    else:    
        setColor("cyan")
    line(0, 50, x, 0)
    x = x + 1




