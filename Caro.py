import turtle
import random
import time

count = 0  # chan x danh, le O danh
dtx = [1, 1, 1, 0]
dty = [1, -1, 0, 1]


def banCoRong():
    global size
    board = []
    for i in range(size):
        board.append([" "] * size)
    return board


def cuoiCungPhiaTrai(x, y, dx, dy):
    flag = 4
    while x - dx >= 0 and y - dy >= 0 and x + dx < size and y - dy < size and flag > 0:
        x = x - dx
        y = y - dy
        flag = flag - 1
    return x, y


def cuoiCungPhiaPhai(x, y, dx, dy):
    global size
    flag = 4
    while size > x + dx >= 0 and x + dx >= 0 and size > y + dy >= 0 and flag > 0:
        x = x + dx
        y = y + dy
        flag = flag - 1
    return x, y


def chuyenDuongThangRaMang(x, y, dx, dy):
    global board
    arr = []
    xt, yt = cuoiCungPhiaTrai(x, y, dx, dy)
    xp, yp = cuoiCungPhiaPhai(x, y, dx, dy)
    arr.append(board[xt][yt])

    while xt != xp or yt != yp:
        xt = xt + dx
        yt = yt + dy
        arr.append(board[xt][yt])
    return arr


def diemCuaDay(arr):
    if count % 2 == 0:
        return arr.count('x')
    else:
        return arr.count('o')


def kiemTraChienThangCuaDuongThang(arr):
    res = []
    for i in range(len(arr) - 4):
        res.append(diemCuaDay(arr[i:i + 5]))
    return res


def ChienThang(x, y):
    global dtx, dty
    for i in range(len(dtx)):
            MangCuaDT = chuyenDuongThangRaMang(x, y, dtx[i], dty[i])
            if kiemTraChienThangCuaDuongThang(MangCuaDT).count(5) > 0:
                if count % 2 == 0:
                    print ('X thang')
                    return
                else:
                    print ('O thang')
                    return


def click(x, y):
    x = int(x)
    y = int(y)
    global size, count, board
    if 0 <= x < size and 0 <= y < size and board[x][y] == ' ':
        if count % 2 == 0:
            veX(x, y)
            board[x][y] = 'x'
        else:
            veO(x, y)
            board[x][y] = 'o'
        # print board
        ChienThang(x,y)
        count = count + 1


def veX(x, y):
    global colors
    colors['x'].penup()
    colors['x'].goto(x + 0.3, y + 0.3)
    colors['x'].pendown()
    colors['x'].goto(x + 0.7, y + 0.7)
    colors['x'].up()
    colors['x'].goto(x + 0.7, y + 0.3)
    colors['x'].pendown()
    colors['x'].goto(x + 0.3, y + 0.7)
    colors['x'].up()
    colors['x'].ht()


def veO(x, y):
    global colors
    colors['o'].penup()
    colors['o'].goto(x + 0.5, y + 0.15)
    colors['o'].pendown()
    colors['o'].begin_fill()
    colors['o'].circle(0.35)
    colors['o'].end_fill()
    colors['o'].penup()
    colors['x'].ht()


def vebanco(s):
    global board, screen, colors, size
    size = s
    board = banCoRong()

    screen = turtle.Screen()
    screen.onclick(click)
    screen.setup(1200, 1200)
    screen.setworldcoordinates(-1, -1, size + 1, size + 1)
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

    for i in range(0, size + 1):
        border.goto(size, i)
        border.pendown()
        border.goto(0, i)
        if i < size:
            border.goto(0, i + 1)
        border.penup()
    border.goto(size, size)

    for i in range(0, size + 1):
        border.pendown()
        border.goto(size - i, 0)
        border.penup()
        border.goto(size - i - 1, size)

    border.ht()
    screen.listen()
    turtle.mainloop()


if __name__ == '__main__':
    vebanco(20)
