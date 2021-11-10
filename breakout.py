# breakout.py
# Python emulation of the classic Atari arcade game Breakout.

import tkinter as tk
import draw
import events
from params import *
import pdb


def main():
    # Setup game interface
    gui = tk.Tk()
    gui.title("Breakout")
    gui.geometry("{}x{}".format(WIDTH, HEIGHT))

    canvas = tk.Canvas(gui, width=WIDTH, height=HEIGHT)
    canvas.configure(background=COLORS['background'])
    canvas.pack()

    # Draw stuff
    bricks = draw.bricks(canvas)
    boundary = draw.boundary(canvas)
    ball = draw.ball(canvas)
    player = draw.player(canvas)
    lives = draw.lives(canvas)
    score = draw.score(canvas)

    # Add event bindings
    gui.bind("<KeyPress>", lambda evt: events.keydown(evt, gui, canvas, player))
    gui.event_add("<<DIE>>", "None")
    gui.bind("<<DIE>>", lambda evt: events.die(evt, gui, canvas, ball, lives))

    # Run game until user quits
    events.move(ball, canvas, gui)
    gui.mainloop()
    print('Thanks for playing!')


if __name__ == "__main__":
    main()