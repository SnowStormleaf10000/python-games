import turtle, time

def The_Boredom_Tracksetup():
    screen = turtle.Screen()
    screen.title("I'm Bored :(")
    screen.bgcolor("white")
    screen.setup(width=300, height=150)

    mover = turtle.Turtle()
    mover.shape("turtle")
    mover.color("red")
    mover.penup()
    mover.speed(0)
    mover.goto(-80, -40)
    mover.pendown()
    mover.penup()

    track = turtle.Turtle()
    track.shape("circle")
    track.color("cyan")
    track.speed(0)
    track.penup()
    track.goto(-80, -40)
    track.pendown()
    track.setheading(0)
    track.forward(160)
    track.setheading(45)
    track.forward(40)
    track.setheading(90)
    track.forward(30)
    track.setheading(135)
    track.forward(40)
    track.setheading(180)
    track.forward(160)
    track.setheading(225)
    track.forward(40)
    track.setheading(270)
    track.forward(30)
    track.setheading(315)
    track.forward(40)
    track.penup()
    track.hideturtle()

    def The_Boredom_Trackred():
        for _ in range(160):  # Move the turtle in small steps
            mover.setheading(0)
            mover.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(40):
            mover.setheading(45) 
            mover.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothnes
        for _ in range(30):
            mover.setheading(90) 
            mover.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(40):
            mover.setheading(135) 
            mover.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(160):  # Move the turtle in small steps
            mover.setheading(180)     
            mover.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(40):
            mover.setheading(225) 
            mover.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(30):
            mover.setheading(270) 
            mover.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(40):
            mover.setheading(315) 
            mover.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        The_Boredom_Trackred()      

    The_Boredom_Trackred()

The_Boredom_Tracksetup()
