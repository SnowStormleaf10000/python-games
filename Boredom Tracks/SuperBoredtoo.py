import turtle, time

def The_Boredom_Tracksetup():
    screen = turtle.Screen()
    screen.title("I'm Bored :({[")
    screen.bgcolor("white")
    screen.setup(width=300, height=150)

    moverg = turtle.Turtle()
    moverg.shape("turtle")
    moverg.color("lime")
    moverg.penup()
    moverg.speed(0)
    moverg.goto(-80, -40)
    moverg.pendown()
    moverg.penup()

    track = turtle.Turtle()
    track.shape("circle")
    track.color("yellow")
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

    def The_Boredom_Trackgreen():
        for _ in range(160):  # Move the turtle in small steps
            moverg.setheading(0)
            moverg.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(40):
            moverg.setheading(45) 
            moverg.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothnes
        for _ in range(30):
            moverg.setheading(90) 
            moverg.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(40):
            moverg.setheading(135) 
            moverg.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(160):  # Move the turtle in small steps
            moverg.setheading(180)     
            moverg.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(40):
            moverg.setheading(225) 
            moverg.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(30):
            moverg.setheading(270) 
            moverg.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        for _ in range(40):
            moverg.setheading(315) 
            moverg.forward(1)  # Adjust step size for speed
            screen.update()  # Update the screen manually
            time.sleep(0.001)  # Add a small delay for smoothness
        The_Boredom_Trackgreen()      

    The_Boredom_Trackgreen()

The_Boredom_Tracksetup()


