print("=======================")
#Три города
# Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
city1 = input()
city2 = input()
city3 = input()
the_longest = max(city1, city2, city3, key=len)
the_shortest = min(city1, city2, city3, key=len)
print(the_shortest)
print(the_longest)



print("=======================")
#Арифметические строки
# Вводятся 3 строки в случайном порядке.
# Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.
str1 = input()
str2 = input()
str3 = input()
a = len(str1)
b = len(str2)
c = len(str3)
if (2*b-c-a)*(2*c-b-a)*(2*a-b-c) == 0:
    print("YES")
else:
    print("NO")


