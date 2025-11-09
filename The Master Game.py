import random, time, turtle

Game = True

if Game == True:
    Select = int (input ("What would you like to do? Number Guessing Game 1 - 100(1), Dice Roll+(2), Collection Game(3), Snakes & Ladders(4), or Let's Go Gambling!(5)?"))

    if Select == 1:
        number = random.randint (0, 100)
        count = 0

        print ('Number Guessing Game! 1 - 100!')

        while True:
            guess = int (input ("what is your guess?"))
            count += 1

            if guess == number:
                print ("you win")
                print ("it took you %d guesses" % count)
                time.sleep(5)
                break
            elif guess < number:
                print ("too low!")
            else:
                 print ("too high!")

    if Select == 2:

        print ('Dice Roll+')
        
        def roll():
            sides = input ('what die will you roll? d4, 6, 8, 10, 12, 20, or 100')
            if sides == "4":    
                die = random.randint (1, 4)
                print ("you rolled a %d!" % die)
                number = input ('roll again? 1 = yes 2 = no')
                if number == "1":
                   roll()
                else:
                   print ('see you soon!')
                   time.sleep (3)

            if sides == "6":    
                die = random.randint (1, 6)
                print ("you rolled a %d!" % die)
                number = input ('roll again? 1 = yes 2 = no')
                if number == "1":
                   roll()
                else:
                   print ('see you soon!')
                   time.sleep (3)

            if sides == "8":    
                die = random.randint (1, 8)
                print ("you rolled a %d!" % die)
                number = input ('roll again? 1 = yes 2 = no')
                if number == "1":
                   roll()
                else:
                   print ('see you soon!')
                   time.sleep (3)

            if sides == "10":    
                die = random.randint (1, 10)
                print ("you rolled a %d!" % die)
                number = input ('roll again? 1 = yes 2 = no')
                if number == "1":
                   roll()
                else:
                   print ('see you soon!')
                   time.sleep (3)

            if sides == "12":    
                die = random.randint (1, 12)
                print ("you rolled a %d!" % die)
                number = input ('roll again? 1 = yes 2 = no')
                if number == "1":
                   roll()
                else:
                   print ('see you soon!')
                   time.sleep (3)

            if sides == "20":    
                die = random.randint (1, 20)
                print ("you rolled a %d!" % die)
                number = input ('roll again? 1 = yes 2 = no')
                if number == "1":
                   roll()
                else:
                   print ('see you soon!')
                   time.sleep (3)

            if sides == "100":    
                die = random.randint (1, 100)
                print ("you rolled a %d!" % die)
                number = input ('roll again? 1 = yes 2 = no')
                if number == "1":
                   roll()
                else:
                   print ('see you soon!')
                   time.sleep (3)

        roll()

    if Select == 3:
        screen = turtle.Screen()
        screen.title("Turtle Collector")
        screen.bgcolor("black")
        screen.setup(width=600, height=600)

        player = turtle.Turtle()
        player.shape("square")
        #turtle, circle,^, or triangle
        player.color("cyan")
        player.penup()
        player.speed(0)

        food = turtle.Turtle()
        food.shape('triangle')
        food.color('light blue')
        food.penup()
        food.speed(0)
        #randomizing location of food
        food.goto(random.randint(-250, 250), random.randint(-250, 250))

        enemy = turtle.Turtle()
        enemy.shape('turtle')
        enemy.color('#e32999')
        enemy.penup()
        enemy.speed(0)
        enemy.goto(random.randint(-270, 270), random.randint(-270, 270))

        score = 0
        score_display = turtle.Turtle()
        score_display.hideturtle()
        score_display.penup()
        score_display.goto(-280, 260)
        score_display.color('white')
        score_display.write(f"Score: {score}", font=("Comic Sans MS", 16, "normal"))

        step = 10

        def move_up():
            player.setheading(90)
            player.forward(step)

        def move_down():
            player.setheading(270)
            player.forward(step)

        def move_left():
            player.setheading(180)
            player.forward(step)

        def move_right():
            player.setheading(0)
            player.forward(step)

        screen.listen()
        screen.onkeypress(move_up,'Up')
        screen.onkeypress(move_down,'Down')
        screen.onkeypress(move_left,'Left')
        screen.onkeypress(move_right,'Right')

        def is_collision(t1,t2):
            distance = t1.distance(t2)
            return distance < 20

        def game_loop():
            global score

            if is_collision(player, food):
                food.goto(random.randint(-270, 270), random.randint(-270, 270))
                enemy.goto(random.randint(-270, 270), random.randint(-270, 270))
                score += 1
                score_display.clear()
                score_display.write(f"Score: {score}", font=("Comic Sans MS", 16, "normal"))

            if score >= 15 :
                score_display.clear()
                score_display.goto(0, 0)
                score_display.write("You Win!", align='center', font=('Papyrus', 24, 'normal'))

            if is_collision(player, enemy):
                score_display.goto(0,0)
                score_display.write("Game Over!", align='center', font=('Papyrus', 24, 'normal'))

            screen.ontimer(game_loop, 100)
       
        game_loop()
        screen.mainloop()

    if Select == 4:
        screen = turtle.Screen()
        screen.title("Snakes and Ladders :)]}")
        screen.setup(width=800, height=800, startx=0, starty=0)
        screen.bgcolor("white")
        screen.tracer(0)

        board_size = 10#10X10 squares
        square_size = 60 #60 pixels wide
        start_x = -300 #starting x pos
        start_y = -300 #starting y pos

        players = []
        player_colors = ['red', 'blue', 'green', 'yellow', 'orange']
        num_players = 5

        for i in range(num_players):
            p = turtle.Turtle()
            p.shape('circle')
            p.color(player_colors[i])
            p.penup()
            p.shapesize(1.5)

            if i == 4:
                players.append({'turtle':p, 'position':0, 'name': "THE SECOND COMING"})
            else:    
                players.append({'turtle':p, 'position':0, 'name': player_colors[i].upper()})

        dice = turtle.Turtle()
        dice.penup()
        dice.hideturtle()
        dice.goto(200, 300)

        status = turtle.Turtle()
        status.penup()
        status.hideturtle()
        status.goto(-380, 300)

        space_pressed = False
        dice_rolling = False

        #start, end
        snakes = [(16, 6), (47, 26), (49, 11), (56,53), (62, 19), (64, 60), (87, 24), (93, 73), (95, 75), (98, 78)]
        ladders = [(4, 14), (9, 31), (21, 42), (28, 84), (36, 44), (51, 67), (71, 91), (80, 100)]

        def get_position(square):
            row = (square-1)//board_size
            col = (square - 1)%board_size if row % 2 == 0 else (board_size - 1 - (square-1) % board_size)

            x = start_x + col * square_size + square_size//2
            y = start_y + row * square_size + square_size//2
            return(x, y)

        def draw_board():
            board = turtle.Turtle()
            board.penup()
            board.hideturtle()
            board.speed(0)

            for row in range(board_size):
                for col in range(board_size):
                    x = start_x + col * square_size
                    y = start_y + row * square_size

                    color = "light gray" if (row + col) % 2 == 0 else "white"

                    board.goto(x, y)
                    board.fillcolor(color)
                    board.begin_fill()
                    for _ in range(4):
                        board.forward(square_size)
                        board.left(90)
                    board.end_fill()
            
                    square_num = row * board_size + (col if row % 2 == 0 else (board_size - 1 - col)) + 1
                    board.goto(x + square_size//2, y + square_size//4)
                    board.write(str(square_num), align="center", font=("Papyrus", 10, "bold"))
            for start, end in snakes:
                start_pos = get_position(start)
                end_pos = get_position(end)

                board.penup()
                board.goto(start_pos[0], start_pos[1])
                board.pendown()
                board.pencolor("red")
                board.pensize(3)
                board.goto(end_pos[0], end_pos[1])
            screen.update()

            for start, end in ladders:
               start_pos = get_position(start)
               end_pos = get_position(end)
               board.penup()
               board.goto(start_pos[0], start_pos[1])
               board.pendown()
               board.pencolor("green")
               board.pensize(3)
               board.goto(end_pos[0], end_pos[1])
            screen.update()

        "def on_space_press():"
            # called AUTOMATICALLY when space is pressed

        "global space_pressed"
        "if not dice_rolling:"
        "space_pressed = True"

        def roll_dice():
            global dice_rolling
            dice_rolling = True

            for x in range(8):
                value = random.randint (1, 6)
                dice.clear()
                dice.write(f"Rolling: {value}", align="center", font=("Comic Sans MS", 24,  "bold"))
                screen.update()
                time.sleep(0.1)

            final_value = random.randint(1, 6)
            dice.clear()
            dice.write(f"Roll: {final_value}", align="center", font=("Comic Sans MS", 24,  "bold"))
            screen.update()

            dice_rolling = False
            return final_value

        def animate_movement(player, start_pos, end_pos, steps=10):
            x1, y1 = start_pos
            x2, y2 = end_pos

            for i in range(steps + 1):
                x = x1 + (x2-x1) * i/steps
                y = y1 + (y2 - y1) * i/steps

                player["turtle"].goto(x, y)
                screen.update()
                time.sleep(0.01)

        def move_player(player, steps):
            global dice_rolling
            dice_rolling = True

            start_pos = player["position"]

            for step in range(1, steps + 1):
                new_pos = start_pos + step

                if new_pos > 100:
                     new_pos = 100

                current_pos = get_position(player["position"])
                next_pos = get_position(new_pos)

                animate_movement(player, current_pos, next_pos)

                player["position"] = new_pos

                if step == steps or new_pos == 100:
                    for start, end in snakes:
                        if new_pos == start:
                            status.clear()
                            status.write(f"{player['name']} slid down a snake from {start} to {end}!", font = ("Comic Sans MS", 14, "normal"))
                            screen.update()
                            time.sleep(1)

                            start_pos = get_position(start)
                            end_pos = get_position(end)
                            animate_movement(player, start_pos, end_pos, steps=20)
                            player["position"] = end
                            break
                    for start, end in ladders:
                        if new_pos == start:
                            status.clear()
                            status.write(f"{player['name']} climbed up a ladder from {start} to {end}!", font = ("Comic Sans Ms", 14, "normal"))
                            screen.update()
                            time.sleep(1)
                            status.clear()

                            start_pos = get_position(start)
                            end_pos = get_position(end)
                            animate_movement(player, start_pos, end_pos, steps=20)
                            player["position"] = end
                            break
            if player["position"] >= 100:
                player["position"] = 100
                return True #game ends
            dice_rolling = False
            return False #game continues
                        
        def game_loop():
            global space_pressed
            current_player = 0
            draw_board()

            for i, player in enumerate(players):
                x, y = get_position(0)
                x += (i % 2) * 15 - 7
                y += (i//2) * 15 - 7
                player["turtle"].goto(x, y)
            screen.update()

            #rolling the die

            while True:
                player = players[current_player]
                status.clear()
                status.write(f"{player['name']} 's turn (press SPACE to roll)", font = ("Comic Sans MS", 14, "normal"))
                screen.update()

                space_pressed = False
                screen.onkey(on_space_press, "space")
                screen.listen()

                while not space_pressed:
                    screen.update()
                    time.sleep(0.1)

                screen.onkey(None, "space")

                roll = roll_dice()
                time.sleep(0.5)

                won = move_player(player, roll)

                #win condition

                if won:
                    status.clear()
                    status.write(f"{player['name']} wins!", font=("Arial", 24, "bold"))
                    screen.update()
                    break

                #switch whose rolling

                current_player = (current_player+1) % num_players

                time.sleep(0.5)

        game_loop()
        turtle.done()

    if Select == 5:
        import random, time

        def GAMBLING():
            print ("Lets Go Gambling!")
            spin = random.randint(1,999)
            time.sleep(1)
            if spin == random.randint(1,999) == random.randint(1,999):
                print ("I can't stop winning!")
                time.sleep(3) 
            else:
                print ("Aw, Dang It")
                time.sleep(1)
                CONTINUE()

        def CONTINUE():
            spin = random.randint(1,999)
            time.sleep(1.3)
            if spin == random.randint(1,999) == random.randint(1,999):
                print ("I can't stop winning!")
                time.sleep(3) 
            else:
                print ("Aw, Dang It")
                time.sleep(0)
                CONTINUE()

        GAMBLING()


        
