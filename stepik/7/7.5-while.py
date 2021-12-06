#Напишем программу, которая считывает натуральное число (целое положительное) и обрабатывает его цифры.

n = int(input())
while n != 0:  # пока в числе есть цифры
    last_digit = n % 10  # получить последнюю цифру
    print("Последняя цифра введенного числа: " + str(last_digit))
    # код обработки последней цифры
    n = n // 10  # удалить последнюю цифру из числа
    print()



#Напишем программу, которая определяет есть ли в числе цифра 7.
num = int(input())
has_seven = False  # сигнальная метка

while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        has_seven = True
    num = num // 10

if has_seven == True:
    print('YES')
else:
    print('NO')


print("===================")
# Обратный порядок в столбик
# Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.
# На вход программе подается одно натуральное число.

num = int(input())
while num != 0:
    last_digit = num % 10  # получить последнюю цифру
    print(last_digit)
    num = num // 10  # удалить последнюю цифру из числа



#Обратный порядок в строку
# Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.

num = int(input())
while num != 0:
    last_digit = num % 10  # получить последнюю цифру
    print(last_digit, end='')
    num = num // 10  # удалить последнюю цифру из числа


print("===================")
#Дано натуральное число n, (n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры.
# На вход программе подается одно натуральное число.
# Программа должна вывести максимальную и минимальную цифры введенного числа (с поясняющей надписью).
# РЕШЕНИЕ 1
num = input()
print("Максимальная цифра равна " + max(num))
print("Минимальная цифра равна " + min(num))



print("===================")
#Все вместе
# Дано натуральное число. Напишите программу, которая вычисляет:
# - сумму его цифр;
# - количество цифр в нем;
# - произведение его цифр;
# - среднее арифметическое его цифр;
# - его первую цифру;
# - сумму его первой и последней цифры.
# На вход программе подается одно натуральное число.
# Программа должна вывести значения указанных величин в указанном порядке.
#РЕШЕНИЕ1

num = int(input())
num_str = str(num)
summa = 0
proizvedenie = 1
n = len(num_str)
n = int(n)
last_digit0 = num % 10
first_digit = int(num_str[0])
summa12 = first_digit + last_digit0
while num != 0:
    last_digit = num % 10
    summa = summa + last_digit
    proizvedenie = proizvedenie * last_digit
    num = num // 10
srednee_arifm = summa / n
print(summa)
print(n)
print(proizvedenie)
print(srednee_arifm)
print(first_digit)
print(summa12)

#РЕШЕНИЕ 2
num,summa,count,pr = int(input()),0,0,1
last_digit = num % 10
while num != 0:
    summa += num % 10
    count +=1
    pr *= num % 10
    n1 = num
    num = num // 10
print(summa,count,pr,summa/count,n1,n1+last_digit,sep='\n')




# Вторая цифра
# Дано натуральное число n (n>9). Напишите программу, которая определяет его вторую (с начала) цифру.
# РЕШЕНИЕ 1
print(input()[1])

# РЕШЕНИЕ 2
n = int(input())
while n > 99:
    n //= 10
print(n % 10)




# Одинаковые цифры
# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
# Программа должна вывести «YES» если число состоит из одинаковых цифр и «NO» в противном случае.
# РЕШЕНИЕ 1
num = int(input())
num_str = str(num)
last_digit0 = num % 10
flag = True

while num != 0:
    last_digit = num % 10  # получить последнюю цифру
    if last_digit != last_digit0:
        flag = False
    num = num // 10  # удалить последнюю цифру из числа
if flag == False:
    print("NO")
elif flag == True:
    print("YES")

#РЕШЕНИЕ 2
n = int(input())
m = n % 10
answer = 'YES'
while n != 0:
    if m != n % 10:
        answer = 'NO'
    n = n // 10
print(answer)





# Упорядоченные цифры
# Дано натуральное число. Напишите программу, которая определяет,
# является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.
# Программа должна вывести «YES»
# если последовательность его цифр при просмотре справа налево является упорядоченной по неубыванию и
# «NO» в противном случае.
# РЕШЕНИЕ 1
num = int(input())
last_digit0 = num % 10
flag = True

while num != 0:
    last_digit = num % 10  # получить последнюю цифру
    if last_digit0 <= last_digit:
        last_digit0 = last_digit
    else:
        flag = False
    num = num // 10  # удалить последнюю цифру из числа

if flag == False:
    print("NO")
elif flag == True:
    print("YES")


# РЕШЕНИЕ2
n,b = int(input()),'YES'
while n // 10 != 0 :
    a = n % 10
    n = n // 10
    if a > n % 10:
        b = 'NO'
print(b)










