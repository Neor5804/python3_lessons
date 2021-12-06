print("="*30, end="")
#Количество чисел
# На вход программе подаются два целых числа a и b (a≤b).
# Напишите программу, которая подсчитывает количество чисел в диапазоне от a до b включительно,
# куб которых оканчивается на 4 или 9.
a = int(input())
b = int(input())
count = 0
for i in range(a, b + 1):
    if ((((i**3) % 10**1) // 10**0) == 4) or ((((i**3) % 10**1) // 10**0) == 9):
        count +=1
print(count)


print("===================")
#Сумма чисел
# На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной строке.
# Напишите программу, которая подсчитывает сумму введенных чисел.
n = int(input())
count = 0
for i in range(n):
    num = int(input())
    count += num
print(count)


#Сумма чисел
# На вход программе подается натуральное число n.
# Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно)
# квадрат которых оканчивается на 2,5 или 8.
from math import *
n = int(input())
counter = 0
for i in range(1, n+1):
    if ((((i**2) % 10**1) // 10**0) == 2) or ((((i**2) % 10**1) // 10**0) == 5) or ((((i**2) % 10**1) // 10**0) == 8):
        counter += i
print(counter)



print("===================")
#Асимптотическое приближение
from math import *
n = int(input())
counter = 0
for i in range(1, n+1):
    num = (1 / i)
    counter = counter + num
result = counter - log(n)
print(result)


#Факториал
# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет n!.
from math import *
n = int(input())
print(factorial(n))




#Без нулей
# Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
# Примечание. Гарантируется, что хотя бы одно из 10 чисел является ненулевым.
counter1 = 0
total = 1
for i in range(10):
    num = int(input())
    if num >= 0:
        counter1 = counter1 + 1
    if num != 0:
        total *= num
print(total)



#Сумма делителей
# На вход программе подается натуральное число n. Напишите программу, которая вычисляет сумму всех его делителей.
# Примечание. Функция подсчета суммы всех делителей числа является очень важной в теории чисел.
n = int(input())
counter1 = 0
total = 0
for i in range(1, n+1):
    if n % i == 0:
        total = total + i
print(total)



#Знакочередующаяся сумма
# На вход программе подается натуральное число n.
# Напишите программу вычисления знакочередующей суммы
#      1−2+3−4+5−6+ … +((−1)**(n+1))*n.
n = int(input())
counter = 0
for i in range(n):
    if i % 2 == 0:
        counter += i + 1
    else:
        counter -= i + 1
print(counter)




print("===================")
#Наибольшие числа 🌶️🌶️
# На вход программе подается натуральное число n, а затем n различных натуральных чисел,
# каждое на отдельной строке. Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.
# Программа должна вывести два наибольших числа, каждое на отдельной строке.
n = int(input())
largest = 0
prelargest = 0
for i in range(n):
    a = int(input())
    if a > largest:
        prelargest = largest
        largest = a
    elif a < largest and a > prelargest:
        prelargest = a
print(largest)
print(prelargest)



#Only even numbers 🌶️
# Напишите программу, которая считывает последовательность из 10 целых чисел и определяет является ли каждое из них четным или нет.
# На вход программе подаются 10 целых чисел, каждое на отдельной строке.
# Программа должна вывести строку «YES», если все числа четные и «NO» в ином случае.

#РЕШЕНИЕ 1
counter = 0
for i in range(10):
    num = int(input())
    if num % 2 == 0:
        counter += 1
    else:
        counter = 0
if counter == 10:
    print("YES")
else:
    print("NO")

#РЕШЕНИЕ 2
flag = 'YES'
for _ in range(10):
    a = int(input())
    if a % 2 != 0:
        flag = 'NO'
print(flag)



#Последовательность Фибоначчи 🌶️
# Напишите программу, которая считывает натуральное число nnn и выводит первые nnn чисел последовательности Фибоначчи.
# На вход программе подается одно число n (n≤100) – количество членов последовательности.
# Программа должна вывести члены последовательности Фибоначчи, отделенные символом пробела.
# 1, 1, 2, 3, 5, 8, 13, 21, 35, ...

#РЕШЕНИЕ 1
num = int(input())
summa = 1
p1 = 0
p2 = summa
for i in range(num):
    if i < 2:
        summa = p1 + p2
        print(summa, end=' ')
    elif i >= 2:
        p1 = p2
        p2 = summa
        summa = p1 + p2
        print(summa, end=' ')


#РЕШЕНИЕ 2
n = int(input())
f1 = 0
f2 = 1
for i in range(0, n):
    f1,f2 = f2,f1+f2
    #f1 = f2
    #f2 = f1+f2
    print(f1, end=' ')
