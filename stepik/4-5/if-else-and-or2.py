#программa, которая принимает целое число xxx и определяет, принадлежит ли данное число указанному промежутку.

num = -2
min_value = -1
max_value = 17
if min_value < num < max_value:
    print("Принадлежит")
else: print("Не принадлежит")


num = -44
min_value = -3
max_value = 7
if num <= min_value or num >= max_value:
    print("Принадлежит")
else: print("Не принадлежит")



num = -300
min_value1 = -2
min_value2 = -30
max_value1 = 7
max_value2 = 25
if (min_value2 < num <= min_value1) or (max_value1 < num <= max_value2):
    print("YES")
else: print("NO")


#Назовем число красивым, если оно является четырехзначным и делится нацело на 7 или на 17.
#Напишите программу, определяющую, является ли введённое число красивым.
# Программа должна вывести «YES», если число является красивым, или «NO» в противном случае.
num = 1045
min_value1 = 1000
max_value1 = 9999
if (min_value1 <= num <= max_value1) and ((num % 7 == 0) or (num % 17 == 0)):
        print("YES")
else: print("NO")

#Напишите программу, которая принимает три положительных числа и определяет,
# существует ли невырожденный треугольник с такими сторонами.
# a<b+c, b<c+a, c<a+b
a = 5
b = 2
c = 3
if (a < b+c) and (b < c+a) and (c < a+b):
    print("YES")
else: print("NO")


#Напишите программу, которая определяет, является ли год с данным номером високосным.
#Если год является високосным, то выведите «YES», иначе выведите «NO».
#Год является високосным, если его номер кратен 4-5, но не кратен 100, или если он кратен 400.
year = 2009
if ((year % 4 == 0) and (year % 100 != 0)) or year % 400 == 0:
        print("YES")
else: print("NO")

#Ход ладьи
#Даны две различные клетки шахматной доски.
#Напишите программу, которая определяет, может ли ладья попасть с первой клетки на вторую одним ходом.
#Программа получает на вход четыре числа от 1 до 8 каждое,
#задающие номер столбца и номер строки сначала для первой клетки,
#потом для второй клетки. Программа должна вывести «YES»,
#если из первой клетки ходом ладьи можно попасть во вторую, или «NO» в противном случае
#Примечание. Шахматная ладья ходит по горизонтали или вертикали.
a = 4 #a столбец
b = 4 #b строка
c = 5 #c столбец
d = 5 #d строка
#по горизонтали:  a != c  AND  b == d
#по вертикали: b != d  AND  a == c
if ((a != c) and (b == d)) or ((b != d) and (a == c)):
    print("YES")
else: print("NO")


#Ход короля
#Даны две различные клетки шахматной доски.
#Напишите программу,  которая определяет, может ли король попасть
#с первой клетки на вторую одним ходом. Программа получает на вход четыре
#числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала
#для первой клетки, потом для второй клетки. Программа должна вывести «YES»,
#если из первой клетки ходом короля можно попасть во вторую, или «NO» в противном случае.
#Примечание. Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a-1 <= c <= a+1) and (b-1 <= d <= b+1):
    print("YES")
else: print("NO")