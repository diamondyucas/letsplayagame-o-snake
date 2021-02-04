import turtle
from random import randint

wn = turtle.Screen()
wn.bgcolor("black")
snake = turtle.Turtle()
snake.hideturtle()
snake.penup()
snake.shape(name="square")
snake.fillcolor("pink")
snake.pencolor("hotpink")
snake.setposition(100, 100)
snake.pendown()
snake.showturtle()

food = turtle.Turtle()
food.shape(name="circle")
food.pencolor("blue")
food.fillcolor("lightblue")
food.penup()
food.goto(randint(-100,0), randint(0,100))

wn.exitonclick()
