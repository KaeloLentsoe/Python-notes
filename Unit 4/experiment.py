password = "secret"
attempts = 0
while attempts < 3:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Access granted!")
        break
    else:
        print("Invalid password. Try again.")
        attempts += 1
else:
    print("Too many failed attempts. Access denied.")