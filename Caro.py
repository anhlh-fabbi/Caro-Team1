import turtle
import random
import time
count = 0
def click(x, y):
    global size, count
    if(x>=0 and y >= 0 and x <= size and y <= size):
        if count%2==0 :
            veX(x,y)
        else:
            veO(x,y)
        count = count + 1
def veX(x, y):
    global colors
    colors['x'].penup()
    colors['x'].goto(int(x)+0.3, int(y)+0.3)
    colors['x'].pendown()
    colors['x'].goto(int(x)+0.7, int(y)+0.7)
    colors['x'].up()
    colors['x'].goto(int(x)+0.7, int(y)+0.3)
    colors['x'].pendown()
    colors['x'].goto(int(x)+0.3, int(y)+0.7)
    colors['x'].up()
    colors['x'].ht()

def veO(x,y):
    global colors
    colors['o'].penup()
    colors['o'].goto(int(x) + 0.5, int(y)+0.15)
    colors['o'].pendown()
    colors['o'].begin_fill()
    colors['o'].circle(0.35)
    colors['o'].end_fill()
    colors['o'].penup()
    colors['x'].ht()

def vebanco(s):
    global win, board, screen, colors, size
    size = s
    screen = turtle.Screen()
    screen.onclick(click)
    screen.setup(1200, 1200)
    screen.setworldcoordinates(-1, -1, size+1, size+1)
    screen.bgcolor('white')
    screen.tracer(0)

    colors = {'x': turtle.Turtle(), 'o': turtle.Turtle(), 'g': turtle.Turtle()}
    colors['x'].color('blue')
    colors['x'].width(10)

    colors['o'].color('green')
    colors['o'].penup()

    border = turtle.Turtle()
    border.speed(0)
    border.penup()

    for i in range(0,size+1):
        border.goto(size,i)
        border.pendown()
        border.goto(0, i)
        if (i < size):
            border.goto(0,i+1)
        border.penup()
    border.goto(size, size)


    for i in range(0,size+1):
        border.pendown()
        border.goto(size-i, 0)
        border.penup()
        border.goto(size-i-1, size)



    border.ht()
    screen.listen()
    turtle.mainloop()


if __name__ == '__main__':
    vebanco(20)