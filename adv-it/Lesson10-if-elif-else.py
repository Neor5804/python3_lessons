age = 12

if (age <= 4):
    print("You are baby")
elif (age > 4) and (age < 12):
    print("You age kid")
elif (age >= 12) and (age < 19):
    print("You are teenager")
else:
    print("You are old!")


all_cars = ["chrusler", "dacia", "bmw", "KIA", "VW", "seat", "skoda", "lada", "audi", "ford", "Chevrolett"]
german_cars = ["bmw", "VW", "audi"]

if "lada" in all_cars:
    print("Yes! Lada is in the list")
else:
    print("No! Lada not in the list")

for xxx in all_cars:
    if xxx in german_cars:
        print(xxx + " is german car")
    else:
        print(xxx + " is not german car")
