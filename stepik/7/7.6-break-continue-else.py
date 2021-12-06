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
