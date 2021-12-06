import math

num1 = math.sqrt(2)     # вычисление корня квадратного из двух
num2 = math.ceil(3.8)   # округление числа вверх
num3 = math.floor(3.8)  # округление числа вниз

print(num1)
print(num2)
print(num3)


from math import *

num1 = sqrt(2)     # вычисление корня квадратного из двух
num2 = ceil(3.8)   # округление числа вверх
num3 = floor(3.8)  # округление числа вниз

print(num1)
print(num2)
print(num3)


#Список функций модуля math
# Список наиболее часто используемых функций модуля math:
# Функция 	Описание
#
# Округления

# int() 	Округляет число в сторону нуля
# round(x) 	Округляет число x до ближайшего целого. Если дробная часть числа равна 0.5, то число округляется до ближайшего четного числа
# round(x, n) 	Округляет число x до n знаков после точки
# floor(x) 	Округляет число x вниз («пол»)
# ceil(x) 	Округляет число x вверх («потолок»)
# abs(x) 	Модуль числа x (абсолютная величина)


#Корни, логарифмы, степени и факториал

# sqrt(x) 	Квадратный корень числа x
# pow(x, n) 	Возведение числа x в степень n
# log(x) 	Натуральный логарифм числа x. Основание натурального логарифма равно числу e
# log10(x) 	Десятичный логарифм числа x. Основание десятичного логарифма равно числу 10
# log(x, b) 	Логарифм числа x по основанию b
# factorial(n) 	Факториал натурального числа n


#Тригонометрия

# degrees(x) 	Преобразует угол x, заданный в радианах, в градусы
# radians(x) 	Преобразует угол x, заданный в градусах, в радианы
# cos(x) 	Косинус угла x, задаваемого в радианах
# sin(x) 	Синус угла x, задаваемого в радианах
# tan(x) 	Тангенс угла x, задаваемого в радианах
# acos(x) 	Возвращает угол в радианах от 0 до π, cos которого равен x
# asin(x) 	Возвращает угол в радианах от −π/2 до π/2, sin которого равен x
# atan(x) 	Возвращает угол в радианах от −π/2 до π/2, tan которого равен x
# atan2(y, x) 	Полярный угол (в радианах) точки с координатами (x, y)



#Список констант модуля math
# Модуль math предоставляет ряд встроенных математических констант:
#
# pi 3.141592653589793
# e  2.718281828459045