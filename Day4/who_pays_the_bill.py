import random 

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#1 way
payer1 = random.choice(friends)
#2nd way
payer = friends[random.randint(0, len(friends)-1 )]

print(f"The lucky person paying the bill is: {payer1}") 