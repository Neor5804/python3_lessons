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


