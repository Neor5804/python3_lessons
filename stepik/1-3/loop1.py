#Напишите программу, которая выводит указанный треугольник, состоящий из звездочек (*).
#Sample Output:
#
#*
#**
#***
#****
#*****
#******
#*******

# put your python code here
stroka="*"
while True:
    print(stroka)
    stroka = stroka+"*"
    if stroka == "********":
        break

# put your python code here
a=""
for i in range(7):
    a+="*"
    print (a)