mx = 0
summa = 0
for i in range(10):
    x = int(input())
    if x < 0:
        summa += x
    if x < mx:
        mx = x
print(summa)
print(mx)