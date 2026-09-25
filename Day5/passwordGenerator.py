import random
import string

letters = list(string.ascii_letters)
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
n_letters = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))
total_length = n_letters + n_symbols + n_numbers


#Easy Version: letters then symbols then numbers
password1 = ''

for i in range (1, n_letters + 1):
    password1 += random.choice(letters)
for j in range (1, n_symbols + 1):
    password1 += random.choice(symbols)
for k in range (1, n_numbers + 1):
    password1 += random.choice(numbers)

print("Version 1")
print(f"your {total_length}-length password is: {password1}")


#hard Version: No pattern

possibilities = []
for i in range (1, n_letters + 1):
    possibilities.append(random.choice(letters))
for j in range (1, n_symbols + 1):
    possibilities.append(random.choice(symbols))
for k in range (1, n_numbers + 1):
    possibilities.append(random.choice(numbers))

#extra safety 
random.shuffle(possibilities)

password2 = ''
for a in range(1, total_length + 1):
    password2 += random.choice(possibilities)

print("Version 2")
print(f"Your {total_length}-length password is: {password2}")
