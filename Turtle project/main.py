import turtle
mypen = turtle.Turtle()
mypen.shape('turtle')
mypen.speed(5)
window = turtle.Screen()
window.bgcolor('skyblue')
style = ('Black',75,'times new roman')
rainbow = ['red','orange','yellow','green','blue','indigo','violet']
size = 200
mypen.penup()
mypen.goto(0,-80)
for color in rainbow:
    mypen.color(color)
    mypen.fillcolor(color)
    mypen.begin_fill()
    mypen.circle(size)
    mypen.end_fill()
    size -=30
mypen.penup()
mypen.color('Black')
mypen.goto(0,-150)
mypen.penup()
mypen.goto(0,-200)
mypen.penup()
mypen.goto(0,-250)
mypen.hideturtle()
turtle.done()