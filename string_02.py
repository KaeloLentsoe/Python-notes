# Banking login form

correct_username = "user123"
correct_password = "pass456"

# Get user input for username and password
username =  input("Enter your name: ")
password = input("Enter your password: ")

# Check if the entered credentials match the correct ones
if username == correct_username and password == correct_password:
    print("Login successful! Welcome to your account.")
else:
    print("Incorrect username or password. Please try")