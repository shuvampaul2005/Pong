"""
Created on Wed Aug 12 21:44:41 2020

@author: Shuvam Paul
"""

import turtle
import os


window=turtle.Screen()
window.title("Pong by Shuvam")
window.bgcolor("black")
window.setup(width=800 , height=600)
window.tracer(0)

#Scoring system

score1=0
score2=0

#Paddle 1

paddle1=turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.penup()
paddle1.goto(-350,0)
paddle1.shapesize(stretch_wid=5, stretch_len=1)

#Paddle 2

paddle2=turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.penup()
paddle2.goto(350,0)
paddle2.shapesize(stretch_wid=5, stretch_len=1)

#Ball

ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5

#Score initialisation
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier",24,"normal"))

#functions for movements

def paddle1_up():
    y=paddle1.ycor()
    y=y+20
    paddle1.sety(y)
    
def paddle1_down():
    y=paddle1.ycor()
    y=y-20
    paddle1.sety(y)
    
def paddle2_up():
    y=paddle2.ycor()
    y=y+20
    paddle2.sety(y)
    
def paddle2_down():
    y=paddle2.ycor()
    y=y-20
    paddle2.sety(y)
    
#to input keyboard commands

window.listen()
window.onkeypress(paddle1_up, "w")
window.onkeypress(paddle1_down, "s")
window.onkeypress(paddle2_up, "Up")
window.onkeypress(paddle2_down, "Down")

#main game loop
while True:
    window.update()
    #Ball movement
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #boreder stop
    
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.mp3&")# if you are using windows , please make this line a comment
        
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.mp3&")# if you are using windows , please make this line a comment
        
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *=-1
        score1 +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score1,score2), align="center", font=("Courier",24,"normal"))
        
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *=-1
        score2 +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score1,score2), align="center", font=("Courier",24,"normal"))
        
    # paddle and ball hit
    
    if ball.xcor()>340 and ball.xcor()<350 and (ball.ycor()<paddle2.ycor() + 40) and (ball.ycor()>paddle2.ycor()-40):
        ball.setx(340)
        ball.dx *=-1
        os.system("afplay bounce.mp3&")# if you are using windows , please make this line a comment
        
    if ball.xcor()<-340 and ball.xcor()>-350 and (ball.ycor()<paddle1.ycor() + 40) and (ball.ycor()>paddle1.ycor()-40):
        ball.setx(-340)
        ball.dx *=-1
        os.system("afplay bounce.mp3&")# if you are using windows , please make this line a comment
