#Напишите программу, которая определяет,
# оканчивается ли год с данным номером на два нуля.
# Если год оканчивается, то выведите «YES», иначе выведите «NO».
year = input()
n = len(year)
dig4 = (int(year) % (10 ** 1)) // (10 ** 0) #единицы
dig3 = (int(year) % (10 ** 2)) // (10 ** 1) #десятки
dig2 = (int(year) % (10 ** (n - 1))) // (10 ** (n - 2)) #сотни
dig1 = (int(year) % (10 ** n)) // (10 ** (n-1)) #тысяча
if dig3 == 0 and dig4 == 0:
    print("YES")
else:
    print("NO")

print("===========")
#Заданы две клетки шахматной доски.
# Напишите программу, которая определяет имеют ли указанные клетки один цвет или нет.
# Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета — то «NO».
white = []
black = []
for i in range(1, 9):
    for j in range(1, 9):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
            white.append([j, i])
        else:
            black.append([j, i])
input1 = [2, 3]
input2 = [7, 7]
if (input1 in white and input2 in white) or (input1 in black and input2 in black):
    print("YES")
else:
    print("NO")



print("===========")
#Футбольная команда набирает девочек от 10 до 15 лет включительно.
# Напишите программу, которая запрашивает возраст и пол претендента,
# используя обозначение пола буквы m (от male – мужчина) и f (от female – женщина)
# и определяет подходит ли претендент для вступления в команду или нет.
# Если претендент подходит, то выведите «YES», иначе выведите «NO».
age = int(input())
gender = input()
if age in range(10, 16) and gender == "f":
    print("YES")
else:
    print("NO")