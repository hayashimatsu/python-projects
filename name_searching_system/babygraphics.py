"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['chartreuse4', 'IndianRed4', 'DarkGoldenrod3', 'turquoise4', 'Maroon3', 'DeepSkyBlue4']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


# def get_x_coordinate(width, year_index):
#     """
#     Given the width of the canvas and the index of the current year
#     in the YEARS list, returns the x coordinate of the vertical
#     line associated with that year.
#
#     Input:
#         width (int): The width of the canvas
#         year_index (int): The index of the current year in the YEARS list
#     Returns:
#         x_coordinate (int): The x coordinate of the vertical line associated
#                               with the specified year.
#     """


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas
    # Write your code below this line
    #################################
    space = CANVAS_WIDTH // len(YEARS)
    for i in range(len(YEARS)):
        canvas.create_line(GRAPH_MARGIN_SIZE + i * space, 0, GRAPH_MARGIN_SIZE + i * space, CANVAS_HEIGHT,
                           width = 1, fill = 'black')
        canvas.create_text(GRAPH_MARGIN_SIZE + i * space + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW, fill='Navy')
    canvas.create_line(0, GRAPH_MARGIN_SIZE, CANVAS_WIDTH, GRAPH_MARGIN_SIZE, width=1, fill='black')
    # 上面的線
    canvas.create_line(0, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=1, fill='black')
    # 下面的線

def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    ↓↓↓↓↓↓↓↓↓↓　N O T I C E ↓↓↓↓↓↓↓↓↓↓↓↓
    Make a list of the years "year_list" in which the name appears so that you can compare the years on the X-axis,
    which will be used in the draw_graphic below. The same as "rank_list"
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid
    # Write your code below this line
    #################################
    for i in range(len(lookup_names)):
        which_one = int(i % len(COLORS))
        color = str(COLORS[which_one])
        target = lookup_names[i]
        year_list = [0 for i in range(len(YEARS))]
        rank_list = [0 for i in range(len(YEARS))]
        for key, value in sorted(name_data[target].items()):
            # items() helps us to arrange the year and corresponded rank
            year = str(key)
            rank = int(value) # just make sure the element is corresponded
            for i in range(len(YEARS)):
                if year == str(YEARS[i]):
                    year_list[i] = year
                    rank_list[i] = rank
        draw_graphic(canvas, target, year_list, rank_list, color)


def draw_graphic(canvas, name, year_list, rank_list, color):
    space = CANVAS_WIDTH // len(YEARS)
    x = 0
    y = 0
    coordinate = []
    for i in range(len(YEARS)):
        x = GRAPH_MARGIN_SIZE + i * space + TEXT_DX
        if year_list[i] == str(YEARS[i]):
            name_rank = name + " " + str(rank_list[i])
            # Using the principle of interpolation, calculate the y coordinate of the rank.
            y = ((CANVAS_HEIGHT-GRAPH_MARGIN_SIZE) * (rank_list[i] - 1) / (1000 - 1)) + 20
            canvas.create_text(x, y, text=name_rank, anchor=tkinter.SW, fill=color)
        else:
            y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
            name_out_of_rank = name + " " + "*"
            canvas.create_text(x, y, text=name_out_of_rank, anchor=tkinter.SW, fill=color)
        coordinate.append((x, y))
        if i >= 1:
            # The coordinates are recorded for each year, but the drawings are drawn after the second point.
            x_1, y_1 = coordinate[i-1]
            x_2, y_2 = coordinate[i]
            canvas.create_line(x_1, y_1, x_2, y_2, width=2, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)
    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
