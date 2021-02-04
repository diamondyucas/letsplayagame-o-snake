import turtle
wn = turtle.Screen()
wn.bgcolor("black")
snake = turtle.Turtle()
snake.hideturtle()
snake.penup()
snake.shape(name="square")
snake.fillcolor("pink")
snake.pencolor("hotpink")
snake.setposition(100,100)
snake.pendown()
snake.showturtle()



wn.exitonclick()