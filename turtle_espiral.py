import turtle 
turtle.speed(0)
turtle.bgcolor('black')
colors=['white','grey']
for numbers in range(700):
    turtle.forward(numbers + 1)
    turtle.right(89)
    turtle.pencolor(colors[numbers%2])

turtle.mainloop()