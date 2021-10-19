message = ""

while True:
    message = input("Enter password ")
    if message == 'secret':
        break
    print(f"Password: {message} is NOT correct")

print("Password was: " + message)