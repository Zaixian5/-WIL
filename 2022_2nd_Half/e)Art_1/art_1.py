# 11월 24일 그림그리기
# 저장명: art_1.py

import turtle as t

draw_action = 1
oldx = 0
oldy = 0

def new_clear():
    global draw_action
    global oldx
    global oldy

    t.clear()
    t.pensize(1)
    t.pendown()
    draw_action = 1
    oldx = 0
    oldy = 0

def draw(x, y):
    global oldx
    global oldy

    if draw_action == 1:
        t.goto(x, y)
        oldx = x
        oldy = y

    elif draw_action == 2:
        t.goto(x, oldy)
        t.goto((x + oldx) // 2, y)
        t.goto(oldx, oldy)

    elif draw_action == 3:
        t.goto(x, oldy)
        t.goto(x, y)
        t.goto(oldx, y)
        t.goto(oldx, oldy)

    elif draw_action == 4:
        t.circle(-((x - oldx) // 2))

def drag(x, y):
    if draw_action == 1:
        draw(x, y)

def move(x, y):
    global oldx
    global oldy
    penstatus = t.isdown()
    t.penup()
    t.goto(x, y)
    if penstatus == True:
        t.pendown()
    oldx = x
    oldy = y

def key_l():
    global draw_action
    draw_action = 1

def key_t():
    global draw_action
    draw_action = 2

def key_r():
    global draw_action
    draw_action = 3

def key_c():
    global draw_action
    draw_action = 4

def key_n():
    new_clear()

def key_u():
    t.penup()

def key_d():
    t.pendown()

def key_1():
    t.pensize(1)

def key_3():
    t.pensize(3)

def key_5():
    t.pensize(5)

t.setup(600, 600)
s = t.Screen()
t.shapesize(2)
t.speed(0)
t.left(90)
new_clear()
t.ondrag(drag)

s.onkey(key_l, 'l')
s.onkey(key_t, 't')
s.onkey(key_r, 'r')
s.onkey(key_c, 'c')

s.onkey(key_n, 'n')
s.onkey(key_u, 'u')
s.onkey(key_d, 'd')

s.onkey(key_1, '1')
s.onkey(key_3, '3')
s.onkey(key_5, '5')

s.onscreenclick(draw, 1)
s.onscreenclick(move, 3)

s.listen()





















    















        
