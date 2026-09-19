import random
import string

length = int(input("password length: "))

characters = string.ascii_letters + string.digits + "!@#$%"
password = ""

for i in range(length):
    password += random.choice(characters)

print("your password:", password)
