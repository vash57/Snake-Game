##import turtle
##import random
##import time
##
##delay=0.1
##score=0
##heighestscore=0
##
###snack shape
##bodies=[]
##
###Getting a screen | canvas
##s=turtle.screen()
##s.title("Snake Game")
##s.bgcolor("red");
##s.setup(width=600,height=600)
##
###ceate Snake head
##head=turtle.Turtle()
##head.speed(0)
##head.shape("square")
##head.color("white")
##head.fillcolor("blue")
##head.penup()
##head.goto(0,0)
##head.direction="stop"
##
###snake food
##
##food=turtle.Turtle()
##food.speed(0)
##food.shape("square")
##food.color("yellow")
##food.fillcolor("green")
##food.penup()
##food.ht()
##food.goto(0,200)
##food.st()
##
###score board
##sb=turtle.Turtle()
##sb.shape("square")
##sb.fillcolor("black")
##sb.penup()
##sb.ht()
##sb.goto(-250,250)
##sb.write("score:0  |  Heighest Score: 0")
##
##def moveup():
##    if head.direction!="down":
##            head.direction="up"
##def movedown():
##    if head.direction!="up":
##        head.direction!="down"
##def moveright():
##    if head.direction!="left":
##        head.direction!="right"
##def movestop():
##    head.direction=="stop"
##def move():
##    if head.direction=="up":
##        y=head.ycor()
##        head.sety(y+20)
##    if head.direction=="down":
##        y=head.sety(y-20)
##    if head.direction=="left":
##        x=head.xcor()
##        head.setx(x+20)
##    if head.direction=="up":
##        y=head.ycor()
##        head.sety(y+20)
##
###Event Handling-Key mapping
##s.listen()
##s.onkey(moveup,"Up")
##s.onkey(movedown,"Down")
##s.onkey(moveleft,"Left")
##s.onkey(moveright,"Right")
##s.onkey(movestop,"Space")
##
###main loop
##while True:
##    s.update() #this is to update the screen
##     #check collission with border
##    if head.xcor()>290:
##        head.setx(-290)
##    if head.xcor()<-290:
##        head.setx(290)
##    if head.ycor()>290:
##        head.sety(-290)
##    if head.xcor()>-290:
##        head.sety(290)
##        
##
##
##    #check collision with food
##        if head.distance(food)<20:
##            #move the food to new random place
##            x=random.randint(-290,290)
##            y=random.randint(-290,290)
##            food.goto(x,y)
##
##            #increase the length of the snake
##            body=turtle.Turtle()
##            body=speed(0)
##            body.penup()
##            body.shape("Square")
##            body.color("red")
##            body.fillcolor("black")
##            bodies.append(body) #append new body
##
##            #increase the score
##            score+=10
##
##            #change delay
##            delay-=0.001
##
##            #update the heighest score
##            if score>highestscore:
##                highestscore=score
##            sb.clear()
##            sb.write("Score: {} Highest score: {}" .format(score,highestscore))
##        #move the snake bodies
##        for index in range(len(bodies)-1,0,-1):
##            x=bodies[index-1].xcor()
##            y=bodies[index-1].ycor()
##            bodies[index].goto(x,y)
##        if len(bodies)>0:
##            x=head.xcor()
##            y=head.ycor()
##            bodies[0].goto(x,y)
##        move()
##        #check collision with snake body
##        for body in bodies:
##            if body.distance(head)<20:
##                time.sleep(1)
##                head.goto(0,0)
##                head.direction="stop"
##
##                #hide bodies
##                for body in bodies:
##                    body.ht()
##                bodies.clear()
##                score=0
##                delay=0.1
##                #update Score board
##                sb.clear()
##                sb.write("score: {} Highest Score: {}".format(score,highestscore))
##                time.sleep(delay)
##                s.mainloop()
##                #this is the end of our snake game code
import turtle
import random
import time

delay = 0.1
score = 0
highestscore = 0

# Snake shape
bodies = []

# Getting a screen (canvas)
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("red")
s.setup(width=600, height=600)

# Create Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.hideturtle()  # Initially hide the food turtle
food.goto(0, 200)
food.showturtle()  # Show the food turtle

# Scoreboard
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.hideturtle()  # Initially hide the scoreboard turtle
sb.goto(-250, 250)
sb.write(f"Score: {score}  |  Highest Score: {highestscore}")

# Functions to change snake's direction
def moveup():
    if head.direction != "down":
        head.direction = "up"

def movedown():
    if head.direction != "up":
        head.direction = "down"

def moveright():
    if head.direction != "left":
        head.direction = "right"

def moveleft():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

# Event Handling - Key Mapping
s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveright, "Right")
s.onkey(moveleft, "Left")

# Main game loop
while True:
    s.update()  # Update the screen

    # Check collision with borders (walls)
    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)

    # Check collision with food
    if head.distance(food) < 20:
        # Move the food to a new random location
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Increase the length of the snake by adding a new body segment
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        body.fillcolor("black")
        bodies.append(body)  # Append new body segment to the snake

        # Increase the score
        score += 10

        # Update the delay (make the game faster over time)
        delay -= 0.001

        # Update the highest score
        if score > highestscore:
            highestscore = score

        # Update the scoreboard
        sb.clear()
        sb.write(f"Score: {score}  |  Highest Score: {highestscore}", font=("Arial", 16, "normal"))

    # Move the snake's body segments
    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)

    # Move the first body segment to the position of the head
    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check collision with the snake's body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the body segments
            for body in bodies:
                body.hideturtle()
            bodies.clear()

            # Reset the score and delay
            score = 0
            delay = 0.1

            # Update the scoreboard
            sb.clear()
            sb.write(f"Score: {score}  |  Highest Score: {highestscore}", font=("Arial", 16, "normal"))

    time.sleep(delay)

s.mainloop()  # Keep the window open until the user closes it

