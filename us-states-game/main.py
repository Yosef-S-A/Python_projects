# This a US states gussing game
# The code uses a CSV file that contains list of US states to check user's guess

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S> States Game")
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

writer = turtle.Turtle()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name?")

    if answer_state.title() == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("state_to_learn.csv")
        break

    if answer_state.title() in all_states:
        if answer_state.title() in guessed_states:
            continue
        state_row = data[data.state == answer_state.title()]
        x_cor = int(state_row.x)
        y_cor = int(state_row.y)
        print(x_cor, y_cor)
        writer.penup()
        writer.goto(x_cor, y_cor)
        writer.pendown()
        writer.write(answer_state.title())
        guessed_states.append(answer_state.title())

# states_to_learn.csv


turtle.mainloop()
