def print_hello(name):
    """Print Privetstvie"""
    print("Congratulations " + name + "! Wish you all the best!")

def summa(x, y):
    return x +y

#2! = 1 * 2
#3! = 1 * 2 * 3
#4! = 1 * 2 * 3 * 4
def factorial(x):
    """Calculate factorial"""
    otvet = 1
    for i in range(1, x + 1):
        otvet = otvet * i
    return otvet

#--------------------
print_hello("Denis")
print_hello("Vadim")

x = summa(33, 22)
print(x)

for i in range(1, 10):
    print(str(i) + "!\t = " + str(factorial(i)))

