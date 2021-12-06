white = []
black = []
for i in range(1, 9):
    for j in range(1, 9):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
            white.append([j, i])
        else:
            black.append([j, i])
input1 = [int(input()), int(input())]
input2 = [int(input()), int(input())]
if (input1 in white and input2 in white) or (input1 in black and input2 in black):
    print("YES")
else:
    print("NO")
