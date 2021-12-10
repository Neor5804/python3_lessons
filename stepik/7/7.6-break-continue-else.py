# Напишем программу, определяющую, что число является простым:

num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False
        break               # останавливаем цикл если встретили делитель числа

if flag == True:
    print('Число простое')
else:
    print('Число составное')



# Напишем программу, использующую цикл for, которая считывает 10 чисел и суммирует их до тех пор,
# пока не обнаружит отрицательное число. В этом случае выполнение цикла прерывается командой break:
result = 0
for i in range(10):
    num = int(input())
    if num < 0:
        break
    result += num
print(result)



# Напишем, программу, которая определяет, содержит ли введенное пользователем число, цифру 7.
num = int(input())
number = num
flag = False
while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        flag = True
        break        # прерываем цикл, так как число гарантированно содержит цифру 7
    num //= 10

if flag == True:
    print('Число', number, 'содержит цифру 7')
else:
    print('Число', number, 'не содержит цифру 7')



# Завершение цикла на основе условий внутри тела цикла, а не на основе условий в его заголовке:
while True:
    if условие 1:  # условие для остановки цикла
        break
    if условие 2:  # еще одно условие для остановки цикла
        break
    if условие 3:  # еще одно условие для остановки цикла
        break


# Напишем программу, которая выводит все числа от 1 до 100, кроме чисел 7, 17, 29 и 78.
for i in range(1, 101):
    if i == 7 or i == 17 or i == 29 or i == 78:
        continue  # переходим на следующую итерацию
    print(i)


# Наименьший делитель
# На вход программе подается число n>1.
# Напишите программу, которая выводит его наименьший отличный от 1 делитель.
num = int(input())
for i  in range(2, num + 1):
    if num % i == 0:
        print(i)
        break


# Следуй правилам
# На вход программе подается натуральное число nnn.
# Напишите программу, которая выводит числа от 1 до n включительно за исключением:
#     чисел от 5 до 9 включительно;
#     чисел от 17 до 37 включительно;
#     чисел от 78 до 87 включительно.
# Программа должна вывести числа в соответствии с условием задачи, каждое на отдельной строке.
# Примечание. Используйте оператор continue
num = int(input())
for i in range (1, num +1 ):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i)



# Напишем, программу, которая определяет, содержит ли введенное пользователем число, цифру 7.
n = int(input())
while n != 0:
    last = n % 10
    if last == 7:
        print('Число', n, 'содержит цифру 7')
        break
    n //= 10
else:
    print('Число', n, 'не содержит цифру 7')