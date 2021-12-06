#import math
#place_number = int(input())
#x = place_number / 4-5
#print(math.ceil(x))


#minutes_count = int(input())
#hours_count = minutes_count // 60
#ostatok = minutes_count % 60
#print(str(minutes_count) + " мин - это " + str(hours_count) + " час " + str(ostatok) + " минут.")

#     cba
#     123
#num = int(input())
#a = num % 10
#b = (num % 100) // 10
#c = num // 100
#summa = a+b+c
#proizvedenie = a*b*c
#print("Сумма цифр = " + str(summa))
#print("Произведение цифр = " + str(proizvedenie))

n=4
num = int(input())
dig4 = (num % (10 ** 1)) // (10 ** 0)
dig3 = (num % (10 ** 2)) // (10 ** 1)
dig2 = (num % (10 ** (n-1))) // (10 ** (n-2))
dig1 = (num % (10 ** n)) // (10 ** (n-1))

print("Цифра в позиции тысяч равна " + str(dig1))
print("Цифра в позиции сотен равна " + str(dig2))
print("Цифра в позиции десятков равна " + str(dig3))
print("Цифра в позиции удиниц равна " + str(dig4))