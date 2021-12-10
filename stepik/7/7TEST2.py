count = 0
proizvedenie = 1
for i in range(1, 11):
    x = int(input())
    if x >= 0:
        proizvedenie *= x
        count += 1
if count > 0:
    print(count)
    print(proizvedenie)
else:
    print("NO")









