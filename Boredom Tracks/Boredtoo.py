import turtle, time

def The_Boredom_Tracksetup():
    screen = turtle.Screen()
    screen.title("I'm Bored :({")
    screen.bgcolor("white")
    screen.setup(width=300, height=150)

    moverb = turtle.Turtle()
    moverb.shape("turtle")
    moverb.color("cyan")
    moverb.penup()
    moverb.speed(0)
    moverb.goto(-80, -40)
    moverb.pendown()
    moverb.penup()

    track = turtle.Turtle()
    track.shape("circle")
    track.color("red")
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

    def The_Boredom_Trackblue():
        for _ in range(160):  # Move the turtle in small steps
            moverb.setheading(0)
            moverb.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(40):
            moverb.setheading(45) 
            moverb.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothnes
        for _ in range(30):
            moverb.setheading(90) 
            moverb.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(40):
            moverb.setheading(135) 
            moverb.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(160):  # Move the turtle in small steps
            moverb.setheading(180)     
            moverb.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(40):
            moverb.setheading(225) 
            moverb.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(30):
            moverb.setheading(270) 
            moverb.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(40):
            moverb.setheading(315) 
            moverb.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        The_Boredom_Trackblue()      

    The_Boredom_Trackblue()

The_Boredom_Tracksetup()

