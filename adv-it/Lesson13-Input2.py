mylist = []
message = ""
#пока message НЕ РАВЕН "stop"
while message != 'stop'.upper():
    message = input("Enter new item, and STOP to finish: ")
    mylist.append(message)

print(mylist)
