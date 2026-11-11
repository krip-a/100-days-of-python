#new_dict = {new_key:new_value for item in list}
#new_dict = {new_key:new_value for (key, value) in dict.items()}
#new_dict = {new_key:new_value for (key, value) in dict.items() if test}

#looping through pandas dataframe
    #for (index, row) in std_df.iterrows():
        #if row.student == "Angela":
            #print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd
FILE_PATH = "./nato_phonetic_alphabet.csv"

data = pd.read_csv(FILE_PATH)
alphabet_dict = {row.letter:row.code for (index,row) in data.iterrows()}


word = input("Enter a word: ").upper()
letter_list = [alphabet_dict[letter] for letter in word]

print(letter_list)
