# draw.py
# Helper functions for drawing game elements on the GUI.

import tkinter as tk
from params import *
import pdb


def ball(canvas):
    '''Draw ball in initial position on the tkinter canvas.'''
    x = WIDTH * 0.5
    y = HEIGHT * 0.5
    r = RADIUS
    ball = canvas.create_oval(x-r, y-r, x+r, y+r, fill=COLORS['gray'], width=0)
    canvas.setvar("ball_angle", 30)
    canvas.setvar("ball_xdir", -1)
    canvas.setvar("ball_ydir", 1)

    return ball

def boundary(canvas):
    '''Draw the top boundary of the playing area on the tkinter canvas.'''
    x1 = 0
    y1 = 50
    x2 = WIDTH
    y2 = y1
    boundary = canvas.create_line(x1, y1, x2, y2, fill=COLORS['gray'], width=3)

    return boundary

def bricks(canvas):
    '''Draw bricks on the tkinter canvas.'''
    # Setup relevant parameters about the brick wall
    wid = WIDTH / COLUMNS  # width of each brick
    hei = 10  # height of each brick
    y0 = 100  # x-position of top layer of bricks

    # Create individual bricks and store in array
    bricks = []
    for clr in range(len(ORDER)):
        for row in range(ROWS[clr]):
            for col in range(COLUMNS):
                x1 = wid * col
                y1 = y0 + hei * row
                x2 = x1 + wid
                y2 = y1 + hei
                bricks.append(canvas.create_rectangle(x1, y1, x2, y2, fill=COLORS[ORDER[clr]], width=3))
        y0 = y2

    return bricks

def lives(canvas):
    '''Draw lives on the tkinter canvas.'''
    # Setup relevant parameters about the lives objects
    r = RADIUS  # radius of circle depicting each life
    spacing = 3  # multiple of radius for spacing

    # Determine the starting position of life 0
    if LIVES % 2 == 0:  # number of lives is even
        x0 = (WIDTH / 2) - spacing * r * (LIVES // 2 - 0.5)
    else:  # number of lives is odd
        x0 = (WIDTH / 2) - spacing * r * (LIVES // 2)

    # Create individual lives and store in array
    lives = [None] * LIVES
    for i in range(LIVES):
        x = x0 + (spacing * r * i)
        y = 25
        lives[i] = canvas.create_oval(x-r, y-r, x+r, y+r, fill=COLORS['gray'], width=0)
        
    canvas.setvar("remaining_lives", LIVES)
    
    return lives

def player(canvas):
    '''Draw player in initial position on canvas.'''
    # Setup relevant parameters about the player
    wid = WIDTH / COLUMNS  # width of player matches the bricks
    hei = 10  # height of player
    x1 = (WIDTH - wid) / 2
    y1 = HEIGHT - 50
    x2 = x1 + wid
    y2 = y1 + hei

    # Create the player rectangle
    player = canvas.create_rectangle(x1, y1, x2, y2,
        fill=COLORS['blue'],
        width=0)

    return player

def score(canvas):
    '''Draw the text to indicate score on the tkinter canvas.'''
    x = WIDTH - 20
    y = 25
    score = canvas.create_text(x, y, text="0",
        anchor=tk.E,
        fill=COLORS['gray'],
        font=FONT)

    canvas.setvar("current_score", 0)

    return score