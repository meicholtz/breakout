# params.py
# Relevant "global" parameters for the game.

COLORS = {'background': '#000000',
    'gray': '#cccccc',
    'red': '#a31e0a',
    'orange': '#c2850a',
    'green': '#0a8533',
    'yellow': '#c2c229',
    'blue': '#0a85c2'}
FONT = ("Consolas", 20, "normal")
WIDTH = 400
HEIGHT = 500
ORDER = ['red', 'orange', 'green', 'yellow']  # order of colors from top to bottom
ROWS = [2, 2, 2, 2]  # rows for each color
COLUMNS = 14
LIVES = 3  # number of lives in the game
RADIUS = 5  # radius of ball, lives
SPEED = {'player': 8, 'ball': 5}
DELAY = 30  # number of milliseconds to wait beteween updates
