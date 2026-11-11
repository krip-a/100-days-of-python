import pandas as pd

DATA_FILE = "./stateQuiz/50_states.csv"

correct_state = input("enter: ")

data = pd.read_csv(DATA_FILE)
#states = data.state
#for state in states:

   
    
state_row = data[data["state"] == correct_state.title()]
print(state_row)
if not state_row.empty:
        x = int(state_row.x.item())
        y = int(state_row.y.item())
print(x)
print(y)
    #x_cor = int(x.to_list())
    #y_cor = int(y.to_list())
    #turtle.goto(x_cor,y_cor)
    #turtle.write(correct_state.title())


#version with list comprehension
correct_guesses = []
if correct_state == "Exit":
        all_states = data.state.to_list()
        #missed_states = []
        #for state in all_states:
        #    if state not in correct_guesses:
        #        missed_states.append(state)

        missed_states = [state for state in all_states if state not in correct_guesses]


        df = pd.DataFrame(missed_states)
        df.to_csv("./stateQuiz/states_to_learn.csv")
        #break