import turtle
import random
import time
import Ve

count = 0  # chan x danh, le O danh
ChienThang = False
dtx = [0, 1, 1, 1]
dty = [1, 0, 1, -1]

def KTChienThang(x, y, type):
    global board, ChienThang
    listDiem, listChienThang = luuListDiem(x, y,type)
    if ttChienThang(listChienThang) == 5:
        ChienThang = True
        return True
    return False

def chuyenDoiDiem(listDiem):
    # print(listDiem)
    tungdiem = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, -1: {}}
    for key in listDiem:
        for diem in listDiem[key]:
            if key in tungdiem[diem]:
                tungdiem[diem][key] += 1
            else:
                tungdiem[diem][key] = 1
    return tungdiem


def diem34(diem3, diem4):
    for key4 in diem4:
        if diem4[key4] >= 1:
            for key3 in diem3:
                if key3 != key4 and diem3[key3] >= 2:
                    return True
    return False


def ttChienThang(listDiem):
    listDiem = chuyenDoiDiem(listDiem)
    if 1 in listDiem[5].values():
        return 5
    elif len(listDiem[4]) >= 2 or (len(listDiem[4])) == 1 and max(listDiem[4].values()) >= 2:
        return 4
    elif diem34(listDiem[3], listDiem[4]):
        return 4
    else:
        diem3 = sorted(listDiem[3].values(), reverse=True)
        if len(diem3) >= 2 and diem3[0] >= diem3[1] >= 2:
            return 3
    return 0


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


def chuyenDuongThangRaMangToaDo(x, y, dx, dy):
    global board
    arr = []
    xt, yt = cuoiCungPhiaTrai(x, y, dx, dy)
    xp, yp = cuoiCungPhiaPhai(x, y, dx, dy)
    arr.append((xt, yt))
    while xt != xp or yt != yp:
        xt = xt + dx
        yt = yt + dy
        arr.append((xt, yt))
    return arr


def chuyenDuongThangRaMangGiaTri(x, y, dx, dy):
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


def diemCuaDay(arr, type):
    trong = arr.count(' ')
    daDanh = arr.count(type)
    if trong + daDanh < 5:
        return -1
    # print daDanh
    return daDanh


def tinhDiem(arr, type):
    res = []
    for i in range(len(arr) - 4):
        res.append(diemCuaDay(arr[i:i + 5], type))
    return res


def luuListDiem(x, y, type):
    global dtx, dty
    arr = {-1: 0, 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    Diem = {(0, 1): [], (1, 0): [], (1, 1): [], (1, -1): []}
    for i in range(len(dtx)):
        MangDT = chuyenDuongThangRaMangGiaTri(x, y, dtx[i], dty[i])
        listDiem = tinhDiem(MangDT, type)
        Diem[(dtx[i], dty[i])] = listDiem
        for i in arr:
            arr[i] += listDiem.count(i)
    return arr, Diem


def DiemNuocDi(x, y):
    tc = 0
    pt = 0
    board[x][y] = 'o'
    listDiem, listChienThang = luuListDiem(x, y, 'o')
    board[x][y] = ' '
    tc += ttChienThang(listChienThang) * 5000 + listDiem[-1] + listDiem[1] + 4 * listDiem[2] + 8 * listDiem[3] + 16 * listDiem[4]
    board[x][y] = 'x'
    listDiem, listChienThang = luuListDiem(x, y, 'x')
    # print (str(x) + " " + str(y))
    # print (listDiem)
    # print ('\n')
    pt += ttChienThang(listChienThang) * 4500 + listDiem[-1] + listDiem[1] + 4 * listDiem[2] + 8 * listDiem[3] + 16 * listDiem[4]
    board[x][y] = ' '
    print(str(x) + " " + str(y) + ": " + str(tc + pt))
    return tc + pt


def nuocDiTotNhat():
    global colors, board
    listToaDo = toaDoCoTheDanh()
    max = 0
    (x, y) = (0, 0)
    for (_x, _y) in listToaDo:
        Diem = DiemNuocDi(_x, _y)
        if (Diem > max):
            max = Diem
            (x, y) = (_x, _y)
    board[x][y] = 'o'
    print("\n\n")
    Ve.O(x, y, colors)
    return x,y


def toaDoCoTheDanh():
    global board, dtx, dty, size
    listToaDoTrong = []
    listToaDoDaDanh = []
    for x in range(size):
        for y in range(size):
            if board[x][y] != ' ':
                listToaDoDaDanh.append((x, y))
    for (x, y) in listToaDoDaDanh:
        for i in range(0, len(dtx)):
            ToaDoTheoDT = chuyenDuongThangRaMangToaDo(x, y, dtx[i], dty[i])
            for (_x, _y) in ToaDoTheoDT:
                if (_x, _y) not in listToaDoDaDanh and (_x, _y) not in listToaDoTrong:
                    listToaDoTrong.append((_x, _y))
    # print listToaDoTrong
    return listToaDoTrong


def click(x, y):
    x = int(x)
    y = int(y)
    global colors, ChienThang

    global size, count, board
    if 0 <= x < size and 0 <= y < size and board[x][y] == ' ' and ChienThang == False:
        Ve.X(x, y, colors)
        board[x][y] = 'x'
        if(KTChienThang(x, y, 'x') == True):
            print('Nguoi Thang')
        else:
            x, y = nuocDiTotNhat()
            if(KTChienThang(x,y, 'o') == True):
                print('May Thang')
        # print("\n\n")


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
