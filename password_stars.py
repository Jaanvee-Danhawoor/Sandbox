length = 10
password = input("Password: ")
while len(password) != length:
    password = input("Password: ")
print("*" * length)
