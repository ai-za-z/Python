import turtle

turtle.Screen().bgcolor("Aqua")
board = turtle.Turtle()

for _ in range(360):
    board.forward(1)  
    board.left(1)     

turtle.done()
