import turtle
import pandas as pd

IMAGE = "./stateQuiz/blank_states_img.gif"
DATA_FILE = "./stateQuiz/50_states.csv"

screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.title("U.S. States Game")

#adding the image from the gif 
screen.addshape(IMAGE)
turtle.shape(IMAGE)
tim = turtle.Turtle()
tim.hideturtle()
tim.penup()

#assigning states by mouseclick
#not necessary hre since csv has x,y
    #def get_mouse_click_coor(x,y):
    #    print(x,y)
    #turtle.onscreenclick(get_mouse_click_coor)


data = pd.read_csv(DATA_FILE)

correct_guesses = []
score = 0
while len(correct_guesses) < 50:
    correct_state = screen.textinput(title= f"{score}/50 States Correct", prompt="What's another state's name?")
    state = correct_state.title()
    #OR
    #all_states = data.state.to_list()
    #state_data = data[data.state == state]
    #tim.goto(state_data.x.item(), state_data.y.item())

    if state == "Exit":
        all_states = data.state.to_list()
        missed_states = []
        for state in all_states:
            if state not in correct_guesses:
                missed_states.append(state)
        df = pd.DataFrame(missed_states)
        df.to_csv("./stateQuiz/states_to_learn.csv")
        break
    state_row = data[data.state == state]
    if not state_row.empty:
        x = int(state_row.x.item())
        y = int(state_row.y.item())
        tim.teleport(x,y)
        tim.write(state)
        correct_guesses.append(state)
        score = len(correct_guesses)

#csv of missed states


 
turtle.mainloop()       #does same thing as screen.exitonclick()
