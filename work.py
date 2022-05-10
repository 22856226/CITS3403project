import os
import sys
import turtle
import levels

def Select_level(num):   #Select level
    level = levels.level_list()
    return level[num]
levels = Select_level(0)

turtle.register_shape('ground.gif')   #ground or space, 0
turtle.register_shape('wall.gif')   #wall, 1
turtle.register_shape('apple.gif')   #ball, 2
turtle.register_shape('box.gif')   #box, 3
turtle.register_shape('cat.gif')   #player, 4
turtle.register_shape('box2.gif')   #when box cover apple, 5

turtle.penup()   # Took up the pen
turtle.tracer(False)

player = 'cat.gif'

def draw():
    global player
    global manx
    global many
    
    turtle.shape('ground.gif')
    for i in range(len(levels)):
        for j in range(len(levels[0])):
            turtle.goto(i*45-200, j*45)
            turtle.stamp()
    
    for i in range(len(levels)):
        for j in range(len(levels[0])):
            img = levels[i][j]
            if img == 1:
                turtle.shape('wall.gif')
            if img == 2:
                turtle.shape('apple.gif')
            if img == 3:
                turtle.shape('box.gif')
            if img == 4 or img == 6:
                turtle.shape(player)
                manx = i
                many = j
            if img == 5:
                turtle.shape('box2.gif')
            
            if img != 0:
                turtle.goto(i*45-200, j*45+5)
                turtle.stamp()
draw()   #Firstly draw the initial map

def move(x, y):
    a = levels[manx+x][many+y]
    if a == 1:   #If player walks towards the wall
        pass
    if a == 0 or a == 2:   #If player walks towards the space or ball
        levels[manx+x][many+y] = a + 4
        levels[manx][many] -= 4
    if a == 3 or a == 5:   # If player push ball
        aa = levels[manx+x+x][many+y+y]
        if aa == 0 or aa == 2:   #If box is pushed into the space or ball
            levels[manx+x+x][many+y+y] += 3
            levels[manx+x][many+y] -= 3
            levels[manx+x][many+y] = levels[manx+x][many+y] + 4
            levels[manx][many] = levels[manx][many] - 4
        if aa == 1 or aa == 3 or aa == 5:
            pass
    
#Keyboard control
turtle.listen()
def left_key():
    move(-1, 0)
    draw()
def right_key():
    move(1, 0)
    draw()
def up_key():
    move(0, 1)
    draw()
def down_key():
    move(0, -1)
    draw()
turtle.onkeypress(left_key, "Left")
turtle.onkeypress(right_key, "Right")
turtle.onkeypress(up_key, "Up")
turtle.onkeypress(down_key, "Down")
    
turtle.mainloop()

