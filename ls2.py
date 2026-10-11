import random
print("hello world")
symbols = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
paswlen = int(input("Enter the length of password: "))
password = ""
for i in range(paswlen):
    random_char = random.choice(symbols)
    password += random_char
print(password)
