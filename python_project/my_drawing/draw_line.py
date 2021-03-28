"""
File: draw_line.py
Name: Lin wei-sung
-------------------------
TODO: 我們必須做到把線拉出來的同時，要把原有的圓圈刪掉，因此在畫圖的同時，需要準確抓到原本的圓圈。
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLabel
from campy.gui.events.mouse import onmouseclicked
# 全域變數專區
SIZE = 15
graphic = GWindow(300, 300)
TIMES = 0
first_step = GOval(SIZE,SIZE) #為了記錄第一個點的座標
times_label = GLabel('Times: '+str(TIMES))
def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)  # 這裡要創造出不同於mousemove所使用的方框
    times_label.font ='-10'
    graphic.add(times_label, 0, times_label.height+10)  #+20=往下長20個單位
def draw(mouse):
    """
    onmouseclick會指定變數為滑鼠的座標，並且針對滑鼠的座標給予click的動作，我們要做的事就是指定這個「動作」是甚麼。
    這個在onmouseclick內的變數，其實也是一個"功能/副程式"，他被強制使用一個來自onmouseclick指定的變數「滑鼠的所有資訊」。
    也就是說，本副程式remove_ring內的變數只能有一個---「mouse(名字可任意)」，此變數代表著「滑鼠的資訊」，
    而我們要用到的是滑鼠的「座標」，所以才有mouse.x,mouse,y。至於我們對這個座標做了甚麼事，就要寫在這個功能內。比方說mouseclick之後進入功能內，
    功能就會幫我們在點的地方「畫圖」，我們只要把畫的東西「留」在畫布上(graphic)就可以了。這些事不需要回傳給main，
    因為main只會判斷mouse對畫布做了甚麼事情，與「畫布」會發生甚麼事情。
    :param mouse:由onmouseclick指定的滑鼠座標。
    :return:NONE
    """
    global SIZE, TIMES
    TIMES += 1
    if TIMES %2 == 1:
        first_ring = GOval(SIZE, SIZE, x = mouse.x - SIZE / 2, y= mouse.y - SIZE / 2)
        if mouse.x <= graphic.width / 2:
            color = 'gold'
        else:
            color = 'gray'
        first_ring.filled = False
        first_ring.color = color
        graphic.add(first_ring)
        first_step.x = first_ring.x + SIZE / 2
        first_step.y = first_ring.y + SIZE / 2 #將第一次的座標assign給暫存用的座標，但是要注意的是圖片出現的圓心與顯示的圓心是不一樣的。
    else:
        last_point = graphic.get_object_at(first_step.x, first_step.y)
        line = GLine(first_step.x, first_step.y, mouse.x, mouse.y)
        graphic.add(line)
        graphic.remove(last_point)
    times_label.text = 'Times: ' + str(TIMES) #提醒自己，是第幾點。

if __name__ == "__main__":
    main()
