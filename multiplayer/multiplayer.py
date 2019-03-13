import turtle
import math
import random

##this function will check if two turtle objects are touching each other
##if they are, the funcion will return True. Else it will return False.
def collision(t1, t2):
    distance = math.sqrt((t2.xcor() - t1.xcor())**2 + (t2.ycor() - t1.ycor())**2)
    
    return distance < 20


def turnLeftP1():
	player1.left(90)
	
def turnRightP1():
    player1.right(90)
    
    
screen = turtle.Screen()
screen.setup(1000, 700)
## uncomment the next line to change the background to an image of your choice!
# screen.bgpic("yourPic.jpg")
# screen.addshape("shapeOfPlayer1.png)
	
	
player1 = turtle.Turtle()
# player1.shape("shapeOfPlayer1.png")
player1.penup()
player1.sety(-100)
## You might also find it useful to have a speed variable
player1_speed = 3

##Add more players here
player2 = turtle.Turtle() #implement the controls for player 2
player2.penup()
player2.sety(100)
player2_speed = 3

## Add more for each keyboard press you want to perform an action for
turtle.listen()

## Player 1 controls
turtle.onkey(turnLeftP1, "a")
turtle.onkey(turnRightP1, "d")


## You can use this list to hold all lots of turtle objects
coins = []
for i in range(5):
	coin = turtle.Turtle()
	coin.hideturtle()
	coin.color("yellow")
	coin.shape("circle")
	coin.penup()
	coin.setx((100 * i) + 20) #use random here
	coin.showturtle()
	coins.append(coin)


## Time for the game loop, inside this loop is what you want to repeat
## over and over such as moving the turle and checking for collisions
## checking the player goes out the the screen bounds
while True:
	player1.forward(player1_speed)
	for coin in coins:
		if collision(player1, coin):
			coin.hideturtle()
			coins.remove(coin)
			break

