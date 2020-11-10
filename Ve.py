def X(x, y, colors):
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


def O(x, y, colors):
    colors['o'].penup()
    colors['o'].goto(x + 0.5, y + 0.15)
    colors['o'].pendown()
    colors['o'].begin_fill()
    colors['o'].circle(0.35)
    colors['o'].end_fill()
    colors['o'].penup()
    colors['x'].ht()
