import pyxel

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120

PADDLE_WIDTH = 40
PADDLE_HEIGHT = 5
PADDLE_SPEED = 2

BALL_RADIUS = 2

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="ブロック崩し")
        
        self.paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
        self.paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT - 5

        self.reset_ball()

        pyxel.run(self.update, self.draw)

    def reset_ball(self):
        self.ball_x = self.paddle_x + PADDLE_WIDTH // 2
        self.ball_y = self.paddle_y - 5
        self.ball_vx = 1
        self.ball_vy = -1

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        
        if pyxel.btn(pyxel.KEY_LEFT):
            self.paddle_x = self.paddle_x - PADDLE_SPEED
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.paddle_x = self.paddle_x + PADDLE_SPEED

        if self.paddle_x < 0:
            self.paddle_x = 0
        if self.paddle_x > SCREEN_WIDTH - PADDLE_WIDTH:
            self.paddle_x = SCREEN_WIDTH - PADDLE_WIDTH

        self.ball_x += self.ball_vx
        self.ball_y += self.ball_vy

        # 当たり判定のロジック
        if self.ball_x <= BALL_RADIUS or self.ball_x >= SCREEN_WIDTH - BALL_RADIUS:
            self.ball_vx = -self.ball_vx
        if self.ball_y <= BALL_RADIUS:
            self.ball_vy = -self.ball_vy
        if self.ball_y >= SCREEN_HEIGHT - BALL_RADIUS:
            self.reset_ball()

        # パドルとの当たり判定
        if self.paddle_x <= self.ball_x and self.ball_x <= self.paddle_x + PADDLE_WIDTH:
            if self.ball_y + BALL_RADIUS >= self.paddle_y:
                if self.ball_vy > 0:
                    self.ball_vy = -self.ball_vy

    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)
        pyxel.rect(
            self.paddle_x,
            self.paddle_y,
            PADDLE_WIDTH,
            PADDLE_HEIGHT,
            pyxel.COLOR_WHITE
        )
        pyxel.circ(
            self.ball_x,
            self.ball_y,
            BALL_RADIUS,
            pyxel.COLOR_WHITE
        )

App()