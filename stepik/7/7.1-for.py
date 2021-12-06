for i in range(10):
    print("Python is awesome!")

str1 = input()
n = int(input())
for i in range(n):
    print(str1)


for i in range(6):
    print("AAA")
for i in range(5):
    print("BBBB")
print("E")
for i in range(9):
    print("TTTTT")
print("G")


n = int(input())
figura = "*******************"
for i in range(n):
    print(figura)

str1 = input()
for i in range(10):
    print(str(i) + " " + str1)


n = int(input())
for i in range(0, n+1):
    print("Квадрат числа " + str(i) + " равен " + str(i*i))



n = int(input())
for i in range(1, n+1):
    print(((n+1) - i)*"*")

#Популяция
# На вход программе подается три натуральных числа m, p, n:
    # m: стартовое количество организмов;
    # p: среднесуточное увеличение в %;
    # n: количество дней для размножения.
# Напишите программу, которая предсказывает размер популяции организмов.
# Программа должна выводить размер популяции в каждый день, начиная с 1 и заканчивая n-м днем.
m = int(input())
p = (int(input()))/100
n = int(input())
for i in range(0, n):
    print(str(i+1) + " " + str(m*(p+1)**i))
