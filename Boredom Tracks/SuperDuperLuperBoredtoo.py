import turtle, time

def The_Boredom_Tracksetup():
    screen = turtle.Screen()
    screen.title("I'm Bored :({[")
    screen.bgcolor("white")
    screen.setup(width=300, height=150)

    movery = turtle.Turtle()
    movery.shape("turtle")
    movery.color("yellow")
    movery.penup()
    movery.speed(0)
    movery.goto(-80, -40)
    movery.pendown()
    movery.penup()

    track = turtle.Turtle()
    track.shape("circle")
    track.color("lime")
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

    def The_Boredom_Trackyellow():
        for _ in range(160):  # Move the turtle in small steps
            movery.setheading(0)
            movery.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(40):
            movery.setheading(45) 
            movery.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothnes
        for _ in range(30):
            movery.setheading(90) 
            movery.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(40):
            movery.setheading(135) 
            movery.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(160):  # Move the turtle in small steps
            movery.setheading(180)     
            movery.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(40):
            movery.setheading(225) 
            movery.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(30):
            movery.setheading(270) 
            movery.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(40):
            movery.setheading(315) 
            movery.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        The_Boredom_Trackyellow()      

    The_Boredom_Trackyellow()

The_Boredom_Tracksetup()
