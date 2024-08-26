import turtle as t
screen=t.Screen() # to create screen for the gameobject from turtle screen
screen.title("ping pong by samuel :)") #print title at the top of the screeen
screen.bgcolor("black") #set the backgroung color 
screen.setup(width=800,height=600) # to set dimentions of the screen
screen.tracer(0) # to stop the screen from refreshing automatically
# first racket
racket1=t.Turtle() # create turtle object
racket1.shape("square") # set the shape of the object is square
racket1.color("white") # the the color of object  white
racket1.penup() # to avoid drawing lines during moving as turtle module do
racket1.speed(0) # the speed of move of turtle 
racket1.goto(-350,0) # we want rocket 1 to start at most left
racket1.shapesize(stretch_wid=6,stretch_len=1)
# second racket
racket2=t.Turtle() # create turtle object
racket2.shape("square") # set the shape of the object is square
racket2.color("white") # the the color of object  white
racket2.penup() # to avoid drawing lines during moving as turtle module do
racket2.speed(0) # animation speed not movement speed 
racket2.goto(350,0) # we want rocket 2 to start at most right
racket2.shapesize(stretch_wid=6,stretch_len=1)
#ball
ball=t.Turtle() # create turtle object
ball.shape("circle") # set the shape of the object is square
ball.color("red") # the the color of object  red
ball.penup() # to avoid drawing lines during moving as turtle module do
ball.speed(0) # the speed of move of turtle 
ball.goto(0,0) # we want the ball starts at middle
ball.dx=0.3
ball.dy=0.3
#score
score1=0
score2=0
score=t.Turtle()
score.color("white") # the the color of object  red
score.penup() # to avoid drawing lines during moving as turtle module do
score.speed(0) # the speed of move of turtle 
score.hideturtle()
score.goto(0,250)
score.write("player1: player2: ",align="center",font=("courier",24,"normal"))

#functions 
#function to up racket1
def rocket1_up():
    y_cor=racket1.ycor() # get y coordinates
    y_cor+=40 # increase the coordinates to go up
    racket1.sety(y_cor) # change the increased coordinates
def rocket2_up(): 
    y_cor=racket2.ycor()
    y_cor+=40
    racket2.sety(y_cor)
def rocket1_down():
    y_cor=racket1.ycor()
    y_cor-=30
    racket1.sety(y_cor)
def rocket2_down():
    y_cor=racket2.ycor()
    y_cor-=30
    racket2.sety(y_cor)
# keyboard binding
screen.listen() # to let program accept from keyboard
screen.onkeypress(rocket1_up,"w") 
screen.onkeypress(rocket1_down,"s")
screen.onkeypress(rocket2_up,"Up")
screen.onkeypress(rocket2_down,"Down")

while True:
    screen.update() # updates screem every time the loop runs
    # change location of ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # check porders 
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score.clear()
        score2+=1
        score.write(f"player1:{score1} player2:{score2} ",align="center",font=("courier",24,"normal"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score.clear()
        score1+=1
        score.write(f"player1:{score1} player2:{score2} ",align="center",font=("courier",24,"normal"))
        
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < racket2.ycor() + 50 and ball.ycor() > racket2.ycor() - 50):
         ball.setx(340)
         ball.dx =ball.dx * -1
       
    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < racket1.ycor() + 50 and ball.ycor() > racket1.ycor() - 50):
         ball.setx(-340)
         ball.dx =ball.dx * -1
