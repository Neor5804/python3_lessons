#a1, d, n = int(input()), int(input()), int(input())
#an = a1 + d * (n - 1)
#print(an)

#Напишите программу, которая считывает целое положительное число xxx и выводит на экран последовательность чисел x, 2x, 3x, 4xx, \, 2x, \, 3x,\,4xx,2x,3x,4x и 5x5x5x, разделённых тремя черточками.
x = int(input())
print([str(i * x) for i in range(1, 6)])
print('---'.join([str(i * x) for i in range(1, 6)]))
print(x, x*2, x*3, x*4, x*5, sep="---")