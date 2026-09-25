import random

print("Rock => 0\nPaper => 1\nScissors =>2")
user_choice = int(input("Rock, Paper Scissors? "))

computer_choice = random.randint(0,2)

if user_choice < 0 or user_choice > 2:
    print("Invalid number.")
elif user_choice == computer_choice:
    print("Draw")
elif user_choice == 0 and computer_choice == 1:
    print("Computer chose Paper")
    print("You Lose")
elif user_choice == 0 and computer_choice == 2:
    print("Computer chose Scissors")
    print("You Win")
elif user_choice == 1 and computer_choice == 0:
    print("Computer chose Rock")
    print("You Win")
elif user_choice == 1 and computer_choice == 2:
    print("Computer chose Scissors")
    print("You Lose")
elif user_choice == 2 and computer_choice == 0:
    print("Computer chose Rock")
    print("You Lose")
elif user_choice == 2 and computer_choice == 1:
    print("Computer chose Rock")
    print("You Win")
else:
    print("Invalid choice.")