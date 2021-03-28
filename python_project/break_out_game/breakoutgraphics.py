"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 3      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 50       # Height of a brick (in pixels).
BRICK_HEIGHT = 15       # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 10  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.

class BreakoutGraphics:
    """
    This method creates the basic features of a breakout game:
    1. Game interface (color and size of blocks, color and size of plates, mouse control)
    2. Impact rules (rules for whittling bricks when they hit a block, where the ball goes when they hit a flat plate)
    3. Rules of the game (game initialization, in-game death)
    """
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 2.5 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)
        self.ball_radius = ball_radius
        # Create a paddle.
        self.paddle_offset = paddle_offset
        self.paddle = GRect(paddle_width, paddle_height,
                            x=(self.window_width - paddle_width)/2,
                            y=self.window_height - self.paddle_offset)
        self.paddle.filled = True
        self.paddle.color = 'saddlebrown'
        self.paddle.fill_color = 'saddlebrown'
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius * 2, ball_radius * 2,
                          x=(self.window_width - 2 * self.ball_radius)/2,
                          y=self.window_height / 2 + self.ball_radius)
        self.ball.filled = True
        self.ball.color = 'sandybrown'
        self.ball.fill_color = 'sandybrown'
        self.window.add(self.ball)
        # Default initial velocity for the ball.
        self.__vx = 0
        self.__vy = 0
        self.set_ball_velocity()    # Creates the initial speed, but it is still not triggered.
        # Initialize our mouse listeners.
        self.is_moving = False
        onmouseclicked(self.ready_to_start)
        onmousemoved(self.paddle_control)
        # Create a score_board
        self.__score = 0
        self.score_label = GLabel('Score: ' + str(self.__score))
        self.score_label.font = 'Times New Roman-24-bold'

        self.window.add(self.score_label, 0, self.score_label.height + 20)
        # Draw bricks.
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height,
                                   x=(brick_width + brick_spacing) * j,
                                   y=brick_offset + (brick_height + brick_spacing) * i)
                self.brick.filled = True
                self.brick.fill_color = self.brick_colors(i)
                self.brick.color = self.brick_colors(i)
                self.window.add(self.brick)

    def ready_to_start(self, mouse):
        """ When the mouse presses the button, the "is_moving" switch is turned on and read by the main program. """
        self.is_moving = True

    def set_ball_velocity(self):
        """ Use random seeds to determine Vx and Vy. """
        self.__vx = random.randint(1, MAX_X_SPEED)
        self.__vy = random.randint(5, INITIAL_Y_SPEED)
        if random.random() > 0.5:
            self.__vx = - self.__vx
        return self.__vx, self.__vy

    def reset_ball(self):
        """
        When the ball falls out of bounds (by function "outside_ball"), turn off the "is_moving" switch
        to temporarily stop the animation and reset the initial speed.
        """
        self.is_moving = False
        self.ball.x = (self.window.width - self.ball.width)/2
        self.ball.y = (self.window.height - self.ball.height)/2
        self.window.add(self.ball)
        self.__vx, self.__vy = self.set_ball_velocity()
        return self.__vx, self.__vy

    def outside_ball(self):
        """ Define out of bound. """
        is_ball_outside = self.window.height <= self.ball.y + self.ball.height
        return is_ball_outside

    def touch_ball(self, __vx, __vy):
        """
        Use vx and vy in the animation execution to determine which switch will be turned on in a collision.
        ★　When the ball is going at a vertical velocity.0 indicates that the ball is falling, and it will judge:
            1. Is it falling on a paddle?
            2. Was it a rebound that hit the brick?
            The difference between the two is "will you erase the thing you hit?".
        ★　When the horizontal velocity of the ball is Vx<0 means the ball is going to the right and
            is considered to hit the brick with the right side of the ball (MIDDLE_RIGHT).
            Meanwhile, Vx>0 is left (MIDDLE_LEFT):
        :param __vx: The horizontal velocity of the ball at that point in time.
        :param __vy: The vertical velocity of the ball at that point in time.
        :return:Return three switches:
                1. Do you hit the plate?
                2. Did you hit the side of the brick?
                3. Does it hit the upper and lower sides of the brick?
        """
        self.is_ball_on_paddle = False
        self.is_ball_hit_side_bricks = False
        self.is_ball_hit_up_down_bricks = False
        self.ball_1_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        self.ball_2_1 = self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.ball_radius)
        self.ball_1_2 = self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y)
        self.ball_2_2 = self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y + 2 * self.ball_radius)
        self.ball_middle_bottom = self.window.get_object_at(self.ball.x + self.ball_radius,
                                                       self.ball.y + self.ball.height + 1)
        self.ball_middle_top = self.window.get_object_at(self.ball.x + self.ball_radius, self.ball.y - 1)
        self.ball_middle_left = self.window.get_object_at(self.ball.x - 1, self.ball.y + self.ball_radius)
        self.ball_middle_right = self.window.get_object_at(self.ball.x + 2 * self.ball_radius + 1,
                                                           self.ball.y + self.ball_radius)
        if self.ball_1_1 or self.ball_1_2 or self.ball_2_1 or self.ball_2_2 is not None and \
                self.ball_1_1 or self.ball_1_2 or self.ball_2_1 or self.ball_2_2 is not self.score_label:
            # 上面的判斷式是為了使一開始要先抓到東西才能判斷撞到甚麼
            if self.ball_2_1 is not self.paddle and self.ball_2_2 is not self.paddle:
                #     ======================測試角落碰撞=====================     #
                if self.ball_1_1 is not None and self.ball_1_1 is not self.paddle and __vy < 0:
                    if self.ball_middle_top is not None and self.ball_middle_top is not self.paddle and __vy < 0:
                        is_brick = self.window.get_object_at(self.ball_middle_top.x, self.ball_middle_top.y)
                        self.window.remove(is_brick)
                        self.is_ball_hit_up_down_bricks = True
                        self.__score += 1
                        print(str(self.is_ball_hit_up_down_bricks) + " top(1_1)")
                    elif self.ball_middle_left is not None and self.ball_middle_left is not self.paddle and __vx < 0:
                        is_brick = self.window.get_object_at(self.ball_middle_left.x, self.ball_middle_left.y)
                        self.window.remove(is_brick)
                        self.is_ball_hit_side_bricks = True
                        self.__score += 2
                        print(str(self.is_ball_hit_side_bricks) + " left(1_1)")
                    else:
                        is_brick = self.window.get_object_at(self.ball_1_1.x, self.ball_1_1.y)
                        self.window.remove(is_brick)
                        self.is_ball_hit_up_down_bricks = True
                        self.__score += 1
                    self.score_label.text = 'Score: ' + str(self.__score)  # 如果要改文字的話，必須要"再次寫入label"
                elif self.ball_2_1 is not None and self.ball_2_1 is not self.paddle and __vy > 0:
                    if self.ball_middle_bottom is not None and self.ball_middle_bottom is not self.paddle and __vy > 0:
                        is_brick = self.window.get_object_at(self.ball_middle_bottom.x, self.ball_middle_bottom.y)
                        self.window.remove(is_brick)
                        self.is_ball_hit_up_down_bricks = True
                        self.__score += 1
                        print(str(self.is_ball_hit_up_down_bricks) + " bottom(2_1)")
                    elif self.ball_middle_left is not None and self.ball_middle_left is not self.paddle and __vx < 0:
                        is_brick = self.window.get_object_at(self.ball_middle_left.x, self.ball_middle_left.y)
                        self.window.remove(is_brick)
                        self.is_ball_hit_side_bricks = True
                        self.__score += 2
                        print(str(self.is_ball_hit_side_bricks) + " left(2_1)")
                    else:
                        is_brick = self.window.get_object_at(self.ball_2_1.x, self.ball_2_1.y)
                        self.window.remove(is_brick)
                        self.is_ball_hit_up_down_bricks = True
                        self.__score += 1
                    self.score_label.text = 'Score: ' + str(self.__score)  # 如果要改文字的話，必須要"再次寫入label"
                elif self.ball_1_2 is not None and self.ball_1_2 is not self.paddle and __vy < 0:
                    if self.ball_middle_top is not None and self.ball_middle_top is not self.paddle and __vy < 0:
                        is_brick = self.window.get_object_at(self.ball_middle_top.x, self.ball_middle_top.y)
                        self.window.remove(is_brick)
                        self.is_ball_hit_up_down_bricks = True
                        print(str(self.is_ball_hit_up_down_bricks) + " top(1_2)")
                    elif self.ball_middle_right is not None and self.ball_middle_right is not self.paddle and __vx > 0:
                        is_brick = self.window.get_object_at(self.ball_middle_right.x, self.ball_middle_right.y)
                        self.window.remove(is_brick)
                        self.is_ball_hit_side_bricks = True
                        self.__score += 2
                        print(str(self.is_ball_hit_side_bricks) + " right(1_2)")
                    else:
                        is_brick = self.window.get_object_at(self.ball_1_2.x, self.ball_1_2.y)
                        self.window.remove(is_brick)
                        self.is_ball_hit_up_down_bricks = True
                        self.__score += 1
                    self.score_label.text = 'Score: ' + str(self.__score)  # 如果要改文字的話，必須要"再次寫入label"
                elif self.ball_2_2 is not None and self.ball_2_2 is not self.paddle and __vy > 0:
                    if self.ball_middle_bottom is not None and self.ball_middle_bottom is not self.paddle and __vy > 0:
                        is_brick = self.window.get_object_at(self.ball_middle_bottom.x, self.ball_middle_bottom.y)
                        self.window.remove(is_brick)
                        self.is_ball_hit_up_down_bricks = True
                        self.__score += 1
                        print(str(self.is_ball_hit_up_down_bricks) + " bottom(2_2)")
                    elif self.ball_middle_right is not None and self.ball_middle_right is not self.paddle and __vx > 0:
                        is_brick = self.window.get_object_at(self.ball_middle_right.x, self.ball_middle_right.y)
                        self.window.remove(is_brick)
                        self.is_ball_hit_side_bricks = True
                        self.__score += 1
                        print(str(self.is_ball_hit_side_bricks) + " right(2_2)")
                    else:
                        is_brick = self.window.get_object_at(self.ball_2_2.x, self.ball_2_2.y)
                        self.window.remove(is_brick)
                        self.is_ball_hit_up_down_bricks = True
                        self.__score += 2
                    self.score_label.text = 'Score: ' + str(self.__score)  # 如果要改文字的話，必須要"再次寫入label"
                #     ============既然不是在磚塊上，那就是在paddle上囉==========     #
            else:
                self.is_ball_on_paddle = True
                print(self.is_ball_on_paddle)
        return self.is_ball_on_paddle, self.is_ball_hit_side_bricks, self.is_ball_hit_up_down_bricks
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓　S　P　E　C　I　A　L　↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

    def hit_paddle_corner(self, __vx):
        """
        Expect the ball to spray at the corner of the paddle,
        and if the paddle hits the ball in the opposite direction with the corner,
        it will slow the ball down.
        """
        if self.ball_2_1 is None and self.ball_2_2 is self.paddle:
            # Hit the ball from the left to the paddle (VX default is positive)
            if __vx > 0:
                # Make it slow down
                __vx = -1 * random.randint(5, 9) * random.random()
            else:
                # Accelerate it
                __vx = -1 * random.randint(10, 15) * random.random()
        elif self.ball_2_2 is None and self.ball_2_1 is self.paddle:
            # Hit the ball from the right to the paddle (VX default is positive)
            if __vx < 0:
                # Make it slow down
                __vx = random.randint(5, 9) * random.random()
            else:
                # Accelerate it
                __vx = random.randint(10, 15) * random.random()
        return __vx

    def game_over(self):
        """
        When the ball dies three times, it will ruthlessly destroy the ball, and run out of the word "GameOver".
        """
        self.window.remove(self.ball)
        self.game_over = GLabel('Game Over !!!!!')
        self.game_over.font = '-30'
        self.window.add(self.game_over, (self.window_width - self.game_over.width)/2,
                        self.window_height / 2 + self.game_over.height)

# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑　S　P　E　C　I　A　L　↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
    def get_vx(self):
        return self.__vx

    def get_vy(self):
        return self.__vy

    def paddle_control(self, mouse):
        if self.paddle.width/2 <= mouse.x <= self.window.width - self.paddle.width/2:
            self.paddle.x = mouse.x - self.paddle.width/2

    def brick_colors(self, num):
        if num <= 1:
            return "maroon"
        elif num <= 3:
            return "firebrick"
        elif num <= 5:
            return "brown"
        elif num <= 7:
            return "indianred"
        elif num <= 9:
            return "lightcoral"
        elif num <= 11:
            return "salmon"
        elif num <= 13:
            return "peachpuff"


