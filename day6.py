#learning about functions and while loops

# Reeborg's world - solving the maze

def at_goal():
    pass #pre-defined function

def turn_left():
    pass #pre-defined function

def move():
    pass #pre-defined function

def right_is_clear():
    pass #pre-defined function

def front_is_clear():
    pass #pre-defined function

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

