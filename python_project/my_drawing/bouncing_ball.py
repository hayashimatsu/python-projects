"""
File: bouncing_ball.py
Name: Lin Wei-Sung
-------------------------
TODO: 我們必須創造一個球使得這顆球會自由落體，落到地板時會彈起來，而且只有在球出界之後才可以產生下一顆球
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 1
DELAY = 10
GRAVITY = 0.1
SIZE = 20
REDUCE = 0.8
START_X = 30
START_Y = 40
window = GWindow(400, 400, title='bouncing_ball.py')
times = 0
ball_tracker = GOval(SIZE, SIZE)

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(free_fall)
def free_fall(mouse):
    """
    我們會在按下滑鼠的那一刻進行「畫圖」的動作
    並且在畫圖之前判斷一些狀況，決定要不要畫圖。
    我的作法 : 使用一個全域變數來記錄球的位置，假如球的位置超過介面了，才允許畫圖。
    另外，當球落到地面時，除了判斷是不是在界面下之外，多給了程式一個想法；只有落下的時候才需要判斷變號。
    這樣可以減少來回震盪的狀況。
    """
    global times
    VY = 0
    if times == 0 or ball_tracker.x > window.width:
        ball = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        ball.filled = True
        ball.fill_color = 'yellow'
        ball.color = 'gray'
        window.add(ball)
        times += 1
        # for 動畫
        while True:
            VY += GRAVITY
            ball.move(VX, VY) # 此時座標是會改變的!
            if VY > 0 and ball.y + ball.height >= window.height:
                VY = -VY * REDUCE  # 碰到邊界就回頭(往反方向)，方向向上，負號
            ball_tracker.x = ball.x
            pause(10)
    else:
        pass


if __name__ == "__main__":
    main()
