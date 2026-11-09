
NAME_PATH  = "./Input/Names/invited_names.txt"
LETTER_PATH = "./Input/Letters/starting_letter.txt"
PLACEHOLDER = "[name]"

name_list = []
#get names from file
with open(NAME_PATH, "r") as names_list:
    names = names_list.readlines()
    

with open(LETTER_PATH, "r") as letter_prototype:
    letter = letter_prototype.read()

    for name in names:
        name = name.strip()
        OUTPUT_PATH = f"./Output/ReadyToSend/letter_for_{name}.txt"
        with open(OUTPUT_PATH, "w") as letter_ready:
            new_letter = letter.replace(PLACEHOLDER, name)
            letter_ready.write(new_letter)