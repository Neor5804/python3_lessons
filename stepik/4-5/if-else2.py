n=4
#num = int(input())
num = 1614
dig4 = (num % (10 ** 1)) // (10 ** 0)
dig3 = (num % (10 ** 2)) // (10 ** 1)
dig2 = (num % (10 ** (n-1))) // (10 ** (n-2))
dig1 = (num % (10 ** n)) // (10 ** (n-1))
print(dig1, dig2, dig3, dig4)
summa = dig1 + dig4
raznost = dig2 - dig3
print(summa)
print(raznost)
if summa == raznost:
    print("ДА")
else:
    print("НЕТ")



num = 16
if num >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")



#арифметическая прогрессия
a = 1
b = 2
c = 3
d = b-a #шаг
if ((b - a) + b == c ):
    print("YES")
else:
    print("NO")


a = 8
b = 11
if a < b:
    print(a)
else:
    print(b)



a = 1
b = 2
c = 3
d = 4
ab = 0
cd = 0
if a < b:
    ab = a
else:
    ab = b
if c < d:
    cd = c
else:
    cd = d
if ab < cd:
    print(ab)
else:
    print(cd)




age = 4
if age <= 13:
    print("детство")
elif age > 14 and age < 24:
    print("молодость")
elif age >= 25 and age < 59:
    print("зрелость")
else:
    print("старость")



a = int(input())
b = int(input())
c = int(input())
summa = 0
if a > 0:
    summa = summa + a
else:
    print()
if b > 0:
    summa = summa + b
else:
    print()
if c > 0:
    summa = summa + c
else:
    print()
print(summa)


