"""
File: sierpinski.py
Name: Lin Wei-Sung
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause
import math

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO: Define the rule to let python draw a fantasy triangle
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: How many times do python draw the triangle with the same rule
	:param length: The length of the side of a triangle, which is half the length of the side of the previous one.
	:param upper_left_x: The starting point of the painting on X- coordinate.
	:param upper_left_y: The starting point of the painting on Y- coordinate.
	(notice that the rule is starting at three point each time.)
	:return: Fantasy triangle
	"""
	if order == 0:
		pass
	else:
		line_nw_se = GLine(upper_left_x, upper_left_y, upper_left_x + length / 2, upper_left_y + length * math.sqrt(3) / 2)
		line_se_ne = GLine(upper_left_x + length / 2, upper_left_y + length * math.sqrt(3) / 2, upper_left_x + length, upper_left_y)
		line_nw_ne = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		window.add(line_nw_se)
		window.add(line_se_ne)
		window.add(line_nw_ne)
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 2, upper_left_y)
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 4, upper_left_y + length * math.sqrt(3) / 4)

if __name__ == '__main__':
	main()