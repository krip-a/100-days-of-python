from hangman_art import sketch, logo
from hangman_words import choose_word

print(f"\t\t{logo}")
print("\t\t********************************")
print("\t\t*    Welcome to Hangman!       *")
print("\t\t********************************")

#variables
chosen_word = choose_word()                           #word to be guessed
game_over = False
lives = 6
correct_letters = []                                #for correct guesses
placeholder = ""  
for position in range(len(chosen_word)):            #placeholder to diplay _ _ _ _ _
    placeholder += '_ '

#Info for the round
print(f"Your word is {len(chosen_word)} letters long and you have {lives} total lives.")
print(f"Guess the word!\t {placeholder}")
print("Good luck!")



while not game_over:
    print("********************************" *3)
    print(f"You have {lives} lives remaining")
    print(sketch(lives))

    guess = input("Guess a letter: ").lower()       #user's guess, one letter at a time
    display = "" 
    if guess in correct_letters:
        print(f"You have already guessed {guess}.")
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_ "
    
    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}. That is not in the word. ")
        if lives == 0:
            game_over = True
            print("YOU LOSE.")
            print(f"The correct word is {chosen_word}")
    
    
    
    if "_" not in display:
        game_over = True
        print("YOU WON!!!")
        print(f"You correctly guessed {chosen_word}")
    
    
        