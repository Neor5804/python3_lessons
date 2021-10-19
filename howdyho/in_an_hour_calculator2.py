#A stupid calculator v2

from colorama import init
from colorama import Fore, Back, Style
init()
print( Fore.BLACK )
print( Back.GREEN )
what = input("What we do? (+, -): ")
print( Back.CYAN )
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print( Back.YELLOW )
if what == "+":
    c = a + b
    print("Result: " + str(c))
elif what == "-":
    c = a - b
    print("Result: " + str(c))
else:
    print("Wrong operation selected")

