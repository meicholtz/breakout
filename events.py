# events.py
# Define event methods for the GUI.

from params import *
import math
import pdb

def die(evt, gui, canvas, ball, lives):
    '''Lose a life and reset the ball.'''
    # Update relevant game variables
    numlives = canvas.getvar("remaining_lives") - 1
    canvas.setvar("remaining_lives", numlives)
    print(numlives)

    if numlives == 0:
        print("GAME OVER")
        gui.setvar("ball_xdir", 0)
        gui.setvar("ball_ydir", 0)

    # Update graphics objects
    # pdb.set_trace()
    # lives[numlives].destroy()
    coords = canvas.coords(ball)
    canvas.move(ball, -coords[0]-RADIUS, -coords[1]-RADIUS)

    # return "break"
    

def fly(player, canvas, direction):
    '''Helper function to fly the player in a specific direction.'''
    if direction == 'left':
        x0 = canvas.coords(player)[0]
        if x0 - SPEED['player'] < 0:
            dx = -x0
        else:
            dx = -SPEED['player']
        canvas.move(player, dx, 0)
    elif direction == 'right':
        x1 = canvas.coords(player)[2]
        if x1 + SPEED['player'] > WIDTH:
            dx = WIDTH - x1
        else:
            dx = SPEED['player']
        canvas.move(player, dx, 0)
    else:
        print("Invalid player direction. Check code for errors.")

def keydown(evt, gui, canvas, player):
    '''Do something when the user presses a key.'''
    # print(evt.char)
    if evt.char == 'q':  # end the program
        gui.destroy()
    elif evt.char == 'a':  # fly player left
        fly(player, canvas, 'left')
    elif evt.char == 'd':  # fly player right
        fly(player, canvas, 'right')

def move(ball, canvas, gui):
    '''Periodically move the ball on the tkinter canvas.'''
    theta = canvas.getvar("ball_angle")
    xdir = canvas.getvar("ball_xdir")
    ydir = canvas.getvar("ball_ydir")
    dx = xdir * SPEED['ball'] * math.sin(math.radians(theta))
    dy = ydir * SPEED['ball'] * math.cos(math.radians(theta))
    canvas.move(ball, dx, dy)

    # Determine if the ball has dropped!
    # print(canvas.coords(ball))
    y = canvas.coords(ball)[1] + RADIUS  # current y-position of the ball
    if y > (HEIGHT - RADIUS):
        gui.event_generate("<<DIE>>")
    
    # Wait a small amount of time before moving the ball again
    gui.after(DELAY, lambda: move(ball, canvas, gui))

