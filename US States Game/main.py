import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "US States Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_label = turtle.Turtle()
state_label.penup()
state_label.hideturtle()


game_running = True
states = pandas.read_csv("US States Game/50_states.csv")

state_list = states["state"].to_list()
# print(state_list)

score = 0
guessed_states = []
while game_running:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("US States Game/states_to_learn.csv")
        break

    if answer_state in states["state"].to_list():
        state = states.loc[states["state"] == answer_state]
        guessed_states.append(answer_state)
        score += 1
        state_x_cor = state["x"].item()
        state_y_cor = state["y"].item()
        state_label.goto(state_x_cor, state_y_cor)
        state_label.write(answer_state, font=("Arial", 8, "normal"))

