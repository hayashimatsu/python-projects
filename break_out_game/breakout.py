"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""


from breakoutgraphics import BreakoutGraphics
from campy.gui.events.timer import pause
import random

FRAME_RATE = 4000 / 120 # 120 frames per second.
NUM_LIVES = 3
"""
本次讓我想最久且無法解決的是；側邊撞到磚塊後卻不能完美碰撞消失的問題，
時常會有球卡進磚塊李或是穿越磚塊，我自己是覺得會不會是動畫的關係(比方說Vx移動太快導致前一秒感應沒問題下一秒卻塞入磚塊)
或者是球的大小比磚塊還厚，使得四個角落都是空的(但側邊確實已經有碰到磚塊)的情況，
然而我一直覺得本程式不應該用暴力解法：將所有條件都列出來，會使得程式變得很冗長，因此我用了四個角落判斷之後，再增加兩條判斷式，
決定本次碰撞是由「1.上下2.左右3.角落來」控制。
並且增加了球碰到paddle角落會亂噴的機制，讓vx多一點變化。
-----------------------------------------------
本次作業沒有做到的項目有：
1.改變label字形
2.當全部打完之後把畫面結束(顯示WIN之類的東西)
3.缺少一些遊戲素材
"""
def main():
    graphics = BreakoutGraphics(ball_radius=10)
    lives = NUM_LIVES
    vx = graphics.get_vx()
    vy = graphics.get_vy()
    while True:
        pause(FRAME_RATE)
        if graphics.is_moving == True:
            is_ball_on_paddle, is_ball_hit_side_brick, is_ball_hit_up_down_brick = graphics.touch_ball(vx, vy)
            if vy > 0 and is_ball_on_paddle :
                vy = -vy  # When you hit the edge of the paddle, turn back (in the opposite direction), up, minus
                vx = graphics.hit_paddle_corner(vx)
            if is_ball_hit_up_down_brick:
                vy = -vy
            if is_ball_hit_side_brick:
                # when it hits bricks on the side
                vx = -vx
            graphics.ball.move(vx, vy)
        if graphics.outside_ball():
            lives -= 1
            if lives > 0:
                vx, vy = graphics.reset_ball()
            else:
                graphics.game_over()
                break
        # It bounces when it touches the left and right boundary
        if graphics.ball.x <= 0 and vx < 0 \
                or graphics.ball.x + graphics.ball.width >= graphics.window.width and vx > 0 :
            vx = - vx
        # It bounces when it hits the top
        if graphics.ball.y <= 0 and vy < 0:
            vy = - vy

if __name__ == '__main__':
    main()
