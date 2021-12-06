from math import *


#Евклидово расстояние
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

p = sqrt((x1 - x2)**2 + (y1 - y2)**2)
print(p)



print("=======================")
#Площадь и длина
# Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R.
# Программа должна вывести два числа – площадь круга и длину окружности радиуса R.
from math import *
R = float(input())
S = pi*(R**2)
C = 2*pi*R
print(S)
print(C)



print("=======================")
#Средние значения
# среднее арифметическое чисел
# среднее геометрическое чисел
# среднее гармоническое чисел
# среднее квадратичное чисел
from math import *
a = float(input())
b = float(input())
arifmet = (a+b)/2
geometr = sqrt(a*b)
garmoni4 = (2*a*b)/(a+b)
kvadrati4 = sqrt(((a**2)+(b**2))/2)
print(arifmet)
print(geometr)
print(garmoni4)
print(kvadrati4)



print("=======================")
#Тригонометрическое выражение
# Напишите программу, вычисляющую значение тригонометрического выражения
# sin x + cos x + tan**2 x
# по заданному числу градусов x.
from math import *
x = float(input()) #градусы
#градусы => радианы
x = radians(x)
sinus = sin(x)
cosinus = cos(x)
tangens = (tan(x))**2
virazhenie = sinus + cosinus + tangens
print(virazhenie)


print("=======================")
#Пол и потолок
# Напишите программу, вычисляющую значение ⌈x⌉ +⌊x⌋ по заданному вещественному числу x.
from math import *
x = float(input())
potolok = ceil(x)
pol = floor(x)
summa = potolok + pol
print(summa)



print("=======================")
#Квадратное уравнение
# Даны три вещественных числа a, b, c. Напишите программу, которая находит вещественные корни квадратного уравнения
#  ((a*x)**2) + (b*x) + c = 0
from math import *
a = float(input())  # a != 0
b = float(input())  # a != b
c = float(input())  # a != c
D = (b**2) - (4*a*c)
if D > 0:  #два различных корня:
    x1 = (-b + sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    x2 = (-b - sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    print(min_x)
    print(max_x)
elif D == 0: #один корень
    x1 = x2 = -(b / (2 * a))
    print(x1)
elif D < 0: #корней нет
    print("Нет корней")



print("=======================")
#Правильный многоугольник
# Правильный многоугольник — выпуклый многоугольник,
# у которого равны все стороны и все углы между смежными сторонами.
# Площадь правильного многоугольника с длиной стороны a и количеством сторон n вычисляется по формуле
from math import *
n = int(input())
a = float(input())
S = (n * (a**2)) / (4*tan(pi/n))
print(S)



