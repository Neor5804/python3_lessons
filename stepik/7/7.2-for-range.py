#Напишем программу, которая выводит те числа из промежутка
# [100;999], которые оканчиваются на 7.
#Используя функцию range() с двумя параметрами, получаем:
for i in range(100, 1000):  # перебираем числа от 100 до 999
    if i % 10 == 7:         # используем остаток от деления на 10, для получения последней цифры
        print(i)

#Напишем программу, которая выводит все четные числа из промежутка [56;170].
# Используя функцию range() с тремя параметрами, получаем:
for i in range(56, 171, 2):
    print(i)

#Напишем программу, которая отсчитывает от 5 до 1, а затем выводит текст Взлетаем!!!:
for i in range(5, 0, -1):
    print(i, end=' ')
print('Взлетаем!!!')

#Последовательность чисел от m до n
m = int(input())
n = int(input())
for i in range(m, n+1):
    print(i)

#Последовательность чисел 2
# Даны два целых числа m и n.
# Напишите программу, которая выводит все числа от m до n включительно в порядке возрастания,
# если m<n, или в порядке убывания в противном случае.
m = int(input())
n = int(input())
if m < n:
    for i in range(m, n+1):
        print(i)
elif m > n:
    for i in range(m, n-1, -1):
        print(i)
elif m == n:
    print(m)


# Задача: Последовательность чисел 3
# Даны два целых числа m и n (m>n).
# Напишите программу, которая выводит все НЕЧЕТНЫЕ числа от m до n включительно в порядке убывания.
# Примечание. Попробуйте решить задачу без использования условного оператора if

m,n = [int(input()) for i in range(2)]

for i in range(m+m%2-1, n-1, -2):
    print(i)



#Последовательность чисел 4
# Даны два натуральных числа m и n ( m≤n).
# Напишите программу, которая выводит все числа от m до n включительно удовлетворяющие хотя бы одному из условий:
#     число кратно 17;
#     число оканчивается на 9;
#     число кратно 3 и 5 одновременно.
m = int(input())
n = int(input())
for i in range(m, n+1):
    if (i % 17 == 0) or (((i % 10**1) // 10**0) == 9) or ((i % 3 == 0) and (i % 5 == 0)):
        print(i)


#Таблица умножения
# Дано натуральное число n. Напишите программу, которая выводит таблицу умножения на n.
# Примечание. В качестве знака умножения используйте английскую букву x.
n = int(input())
for i in range(1, 11):
    print(str(n) + " x " + str(i) + " = " + str(n*i))