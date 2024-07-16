import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian states game")
image = "india-state.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("states_data.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 30:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/30 states correct",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        pandas.read_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

