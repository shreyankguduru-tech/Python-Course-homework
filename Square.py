import turtle

background = turtle.Screen()
background.bgcolor("orange")
turtle.screensize(300,400)
square = turtle.Turtle()

numSides = 4
sidelength = 110
sideAngle = 360 / numSides

for i in range (numSides):
   square.forward(sidelength)
   square.right(sideAngle)


turtle.done()


