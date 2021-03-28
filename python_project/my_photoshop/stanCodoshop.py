"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
The concept of stack map is used to compare N images with each other,
in which the RGB average value of specific pixel in N images is used as reference value for comparison.
And select the pixel that is closest to the average value for reorganization.
The result is a background image with the clutter removed.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    color_distance = ((red - pixel.red) ** 2 + (green - pixel.green) ** 2 + (blue - pixel.blue) ** 2) ** 0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red_total = 0
    green_total = 0
    blue_total = 0
    for x in range(len(pixels)):
        rgb_reader = pixels[x]
        red_total += rgb_reader.red
        green_total += rgb_reader.green
        blue_total += rgb_reader.blue
    red_avg = int(red_total / len(pixels))
    green_avg = int(green_total / len(pixels))
    blue_avg = int(blue_total / len(pixels))
    avg = [red_avg, green_avg, blue_avg]
    return avg


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    avg = get_average(pixels)
    dist = []
    for x in range(len(pixels)):
        dist.append(int(get_pixel_dist(pixels[x], avg[0], avg[1], avg[2])))
    for x in range(len(pixels)):
        if x == 0:
            minimum = dist[x]
            record = x
        else:
            temp_min = dist[x]-minimum
            if temp_min < 0:
                minimum = dist[x]
                record = x
            else:
                continue
    best_pixel = pixels[record]
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    compare = {}
    # I think this is a trap: if you use List, you'll have 180,000 Pixels to process,
    # and your computer will be incredibly slow at 4,000 Pixels. So use dictionary instead.
    for x in range(width):
        for y in range(height):
            for w in range(len(images)):
                compare[w] = images[w].get_pixel(x, y)
            best_pixel = get_best_pixel(compare)
            result_pixel = result.get_pixel(x, y)
            # Scratch out the Pixel at the specified point on the white paper.
            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    print(os.listdir(dir))
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    print(filenames)
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    """
    Step.1 Uses sys.argv to read the address of the folder that you want to analyze the photo
    Step.2 The function "load_images" with "jpgs_in_dir" to store the photo address in the list (filename)
    Step.3 Uses the address obtained from "load_images" as input into solve, which has functions that can be used to find the optimal pixel
    Step.4 "Solve" can combine these optimal pixels to create a perfect background image
    """
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
