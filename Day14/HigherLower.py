import random
from high_low_art import logo, vs
from game_data import data

def choose_person():
    """Chose a random dicttionary from the list of data"""
    A = random.choice(data)
    return A

def eliminate_same_person(A, B):
    """If A and B randomly get assigned the same values, loop until new B is found"""
    while A == B:
        B = choose_person()
    return A, B

def format_descriptions(person):
    """tokenize the dictionary values into smaller variables"""
    person_name = person["name"]
    person_description = person["description"]
    person_country = person["country"]
    person_followers = person["follower_count"]
    person_statement = f"{person_name}, a {person_description}, from {person_country}"
    return person_statement, person_followers

def higher(a, b):
    """takes the followers and returns the choice with higher follower"""
    if a > b:
          return "A"
    else:
         return "B"
    
def play():
    """Play the game!"""
    print(logo)
    score = 0
    play_game = True

    X = choose_person()
    Y = choose_person()
    A, B = eliminate_same_person(X, Y)

    while play_game:
        
        A_statement, A_followers = format_descriptions(A)
        B_statement, B_followers = format_descriptions(B)
        correct_answer = higher(A_followers, B_followers)

        print(f"Compare A: {A_statement}\n{vs}\nAgainst B: {B_statement}")
        #print(f"Hint: correct guess is: {correct_answer}")
        guess = input("\nWho has more followers? 'A' or 'B'? ").upper()
        
        print("\n" * 20)
        print(logo)
        
        if guess == correct_answer:
                score += 1
                print(f"You're right! Current score: {score}")
                P = B
                Q = choose_person()
                A, B = eliminate_same_person(P, Q)
        else:
                print(f"Sorry, that's incorrect :( Final Score: {score}\n")
                play_game = False


play()