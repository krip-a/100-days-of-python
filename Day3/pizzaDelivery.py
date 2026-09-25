print("Welcome to Python Pizza Deliveries!")

size = input("What size of pizza do you want? (S, M, or L): ")
pepperoni = input("DO you want pepperoni on your pizza? (y/n): ")
extra_cheese = input("Do you want extra cheese? (y/n): ")

total = 0

if size.upper() == "S":
    total += 15
elif size.upper() == "M":
    total += 20
elif size.upper() == "L":
    total += 25
   

if pepperoni.upper == "Y":
    if size.upper() == "S":
        total += 2
    elif size.upper() == "M" or size.upper() == "L":
        total += 3

if extra_cheese.upper() == 'Y':
    total += 1

print(f"Your total is: ${total}")