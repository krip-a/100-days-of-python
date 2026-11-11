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