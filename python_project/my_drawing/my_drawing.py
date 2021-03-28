"""
File: my_drawing.py
Name: Lin wei-sung
----------------------
TODO: 畫畫
"""

from campy.graphics.gobjects import GRect, GLabel, GArc, GPolygon
from campy.graphics.gwindow import GWindow

def main():
    """
    TODO:Try to use campy.graphic to create a TESLA
    尻特斯拉的弧型花了我3個小時RRRRRRRRRR
    這個project有幾個難關比較難突破:
    1. 圖形的位置很難使用算式；曲線的構圖很難掌握，得要花時間找出起終點與x,y的關係.
    2. 想要找尋改Glabel字體的方式。(使用setFont之前是不是要import一些東西?)
    3. 要畫出一個喜歡的東西相當的難，有點想直接使用simple_image來po自己手繪的東西@@
    """
    # 創造畫布
    graphic = GWindow(500, 500, 'TESLA')
    graphic.filled = True
    rect_background = GRect(500, 500)
    rect_background.filled = True
    rect_background.fill_color = 'ivory'
    graphic.add(rect_background)
    backgroung_c = 'ivory'
    #第一弧
    radius = 170
    angle = 118
    color = 'sienna'
    T_part0 = GArc(radius*9, radius*3, angle, -2 * (angle-90), x=-100, y=100)
    T_part0.filled = True
    T_part0.fill_color = color
    T_part0.color = color
    graphic.add(T_part0)
    # 第二弧(遮瑕)
    T_part1 = GArc(radius*9, radius*5, angle, -2 * (angle-90), x=-100, y=115)
    T_part1.filled = True
    T_part1.fill_color = backgroung_c
    T_part1.color = backgroung_c
    graphic.add(T_part1)
    # 第二弧(身體)
    T_part2 = GArc(radius*8, radius*5, angle, -2 * (angle-90), x=-60 , y=125)
    T_part2.filled = True
    T_part2.fill_color = color
    T_part2.color = color
    graphic.add(T_part2)
    #中間的三角形
    T_part4 = GPolygon()
    point_1 = (235,120)
    point_2 = (285,120)
    point_3 = (260,150)
    T_part4.add_vertex(point_1)
    T_part4.add_vertex(point_2)
    T_part4.add_vertex(point_3)
    T_part4.filled = True
    T_part4.fill_color = backgroung_c
    T_part4.color = backgroung_c
    graphic.add(T_part4)
    rect_body = GRect(100, 230, x=210, y=165)
    rect_body.filled = True
    rect_body.fill_color = color
    rect_body.color = color
    graphic.add(rect_body)
    #中左的三角形(遮瑕)
    T_part5 = GPolygon()
    point_4 = (210, 150)
    point_5 = (210, 395)
    point_6 = (260, 395)
    T_part5.add_vertex(point_4)
    T_part5.add_vertex(point_5)
    T_part5.add_vertex(point_6)
    T_part5.filled = True
    T_part5.fill_color = backgroung_c
    T_part5.color = backgroung_c
    graphic.add(T_part5)
    T_part5_5 = GArc(radius*4.5, radius*3, 90, 40, x=87, y=150)
    T_part5_5.filled = True
    T_part5_5.fill_color = backgroung_c
    T_part5_5.color = backgroung_c
    graphic.add(T_part5_5)
    #中右的三角形(遮瑕)
    T_part6 = GPolygon()
    point_7 = (310, 150)
    point_8 = (310, 395)
    point_9 = (260, 395)
    T_part6.add_vertex(point_7)
    T_part6.add_vertex(point_8)
    T_part6.add_vertex(point_9)
    T_part6.filled = True
    T_part6.fill_color = backgroung_c
    T_part6.color = backgroung_c
    graphic.add(T_part6)
    T_part6_5 = GArc(radius*4.5, radius*3, 90, -40, x=187, y=150)
    T_part6_5.filled = True
    T_part6_5.fill_color = backgroung_c
    T_part6_5.color = backgroung_c
    graphic.add(T_part6_5)
    #左端的三角形(遮瑕)
    T_part7 = GPolygon()
    point_10 = (90, 70)
    point_11 = (90, 250)
    point_12 = (170, 250)
    T_part7.add_vertex(point_10)
    T_part7.add_vertex(point_11)
    T_part7.add_vertex(point_12)
    T_part7.filled = True
    T_part7.fill_color = backgroung_c
    T_part7.color = backgroung_c
    graphic.add(T_part7)
    #右端的三角形(遮瑕)
    T_part8 = GPolygon()
    point_13 = (428, 70)
    point_14 = (428, 250)
    point_15 = (348, 250)
    T_part8.add_vertex(point_13)
    T_part8.add_vertex(point_14)
    T_part8.add_vertex(point_15)
    T_part8.filled = True
    T_part8.fill_color = backgroung_c
    T_part8.color = backgroung_c
    graphic.add(T_part8)
    #標題
    tesla_quote= GLabel('\"I could either watch it happen or be a part of it.\"', x=35, y=440)
    tesla_quote.font = '-17'
    tesla_quote.color = color
    graphic.add(tesla_quote)
    the_man = GLabel('- by Elon Musk', x=340, y=470)
    the_man.font = '-16'
    the_man.color = color
    graphic.add(the_man)
if __name__ == '__main__':
    main()
