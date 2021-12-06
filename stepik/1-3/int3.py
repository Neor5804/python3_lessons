b = int(input())
a = b-1
c = b+1
print("Следующее за числом " + str(b) + " число: " + str(c))
print("Для числа " + str(b) + " предыдущее число: " + str(a))

x, y, z, w = int(input()), int(input()), int(input()), int(input())
pc1 = 3*(x+y+z+w)
print(pc1)

x, y = int(input()), int(input())
summa = x + y
raznost = x - y
proizvedenie = x * y
print(str(x) + " + " + str(y) + " = " + str(summa))
print(str(x) + " - " + str(y) + " = " + str(raznost))
print(str(x) + " * " + str(y) + " = " + str(proizvedenie))