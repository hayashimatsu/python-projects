"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage
# Constants
THRESHOLD = 1.29    # Controls the threshold of detecting green screen pixel
BLACK_PIXEL = 120   # Controls the upper bound for black pixel
def combine(background, me):
    """
    :param background_img: 這是一張迪士尼海洋樂園的某一項遊樂設施內提供的服務,「單身騎士single rider」
    單人騎士就是如果你不在意一個人乘坐設施的話，可以從單人騎士專用入口進入，如果有零星的位置，就會優先被安排入座
    但!是!
    簡單來說，在這裡排隊的人就是在告訴別人你!沒!有!朋!友!拉!
    :param figure_img: 「好啦好啦，啊我就找不到朋友陪我來迪士尼咩」
    :return:
    """
    for y in range(background.height):
        for x in range(background.width):
            pixel_me = me.get_pixel(x, y)
            avg = (pixel_me.red + pixel_me.blue + pixel_me.green) // 3  # 使用平均判斷綠色的地方
            total = pixel_me.red+pixel_me.blue+pixel_me.green        # 判斷黑色的地方
            if pixel_me.green > avg * THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = background.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
    return me
def main():
    """
    TODO:SHIFT+F10
    """
    space_ship = SimpleImage("images/single.jpg")
    space_ship.show()
    figure = SimpleImage("images/me.jpg")
    figure.show()
    result = combine(space_ship, figure)
    result.show()



if __name__ == '__main__':
    main()
