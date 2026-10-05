import random
from number_art import logo

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

#define functions here
def choose_level():
    chosen_level = input("Choose a difficulty: 'easy' or 'hard': ").lower()
    total_attempts = 0

    if chosen_level == 'easy':
        total_attempts = EASY_ATTEMPTS
    if chosen_level == 'hard':
        total_attempts = HARD_ATTEMPTS
    

    return chosen_level, total_attempts

def check_guess(user_guess, correct_guess, turns):
    if user_guess > correct_guess:
        print("Too high.")
        return turns - 1
    elif guess < correct_guess:
        print("Too Low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {correct_guess}")
    

correct_guess = random.randint(1, 101)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100...")
print(f"correct ans: {correct_guess}")
level, attempts = choose_level()
guess = 0

while guess != correct_guess and attempts > 0:
    print(f"You have {attempts} attempts to guess the number.")
    guess = int(input("Make a guess: "))

    attempts = check_guess(guess, correct_guess, attempts)

    if attempts == 0:
        print("You have run out of turns. You lose.")
    elif guess != correct_guess:
        print("Guess again.")