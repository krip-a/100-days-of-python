import random

def choose_word():
    word_list = ["aardvark", "baboon", "camel", "donald"]

    chosen_word = random.choice(word_list)
    return chosen_word