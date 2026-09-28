import random

def choose_word():
    word_list = ["aardvark", "baboon", "camel", "donald",
                 "apple", "house", "water", "table", "chair",
                 "plant", "phone", "mouse", "bread", "pizza",
                 "cloud", "happy", "green", "light", "music",
                 "paper", "beach", "river", "train", "school",
                 "garden", "orange", "purple", "summer", "winter",
                "rocket", "forest", "island", "castle", "planet",
                "camera", "laptop", "pencil", "coffee", "banana",
                "doctor", "friend", "family", "animal", "window", 
                "adventure", "beautiful", "computer", "knowledge",
                "important", "mountain", "elephant", "chocolate",
                "butterfly", "dinosaur", "restaurant", "telephone",
                "basketball", "university", "technology", "something",
                "dangerous", "wonderful", "education", "discovery",
                "jazz", "quiz", "zebra", "xylophone", "jungle",
                "oxygen", "wizard", "quartz", "vortex", "puzzle",
                "awkward", "zephyr", "whiskey", "jackpot", "zigzag",
                "galaxy", "sphinx", "rhythm", "crypt", "knapsack"]
    word_list2 = word_list.shuffle()                                     #for more randomization
    chosen_word = random.choice(word_list2)
    return chosen_word