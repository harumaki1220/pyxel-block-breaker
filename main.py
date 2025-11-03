import pyxel

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120

PADDLE_WIDTH = 40
PADDLE_HEIGHT = 5
PADDLE_SPEED = 2

BALL_RADIUS = 2

BLOCK_WIDTH = 20
BLOCK_HEIGHT = 5

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="ブロック崩し")
        
        self.paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT - 5

        self.reset_paddle()
        self.reset_ball()
        self.reset_blocks()

        self.scene = "play"
        pyxel.run(self.update, self.draw)

    def reset_ball(self):
        self.ball_x = self.paddle_x + PADDLE_WIDTH // 2
        self.ball_y = self.paddle_y - 5
        self.ball_vx = 1
        self.ball_vy = -1

    def reset_blocks(self):
        self.blocks = []
        for row in range(5):
            for col in range(8):
                block = {"x": col * BLOCK_WIDTH, "y": row * BLOCK_HEIGHT + 10, "alive": True}
                self.blocks.append(block)

    def reset_paddle(self):
        self.paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        if self.scene == "play":
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
                self.scene = "gameover"

            # パドルとの当たり判定
            if self.paddle_x <= self.ball_x and self.ball_x <= self.paddle_x + PADDLE_WIDTH:
                if self.ball_y + BALL_RADIUS >= self.paddle_y:
                    if self.ball_vy > 0:
                        self.ball_vy = -self.ball_vy

            for block in self.blocks:
                if block["alive"]:
                    if block["x"] <= self.ball_x and self.ball_x <= block["x"] + BLOCK_WIDTH:
                        if block["y"] <= self.ball_y and self.ball_y <= block["y"] + BLOCK_HEIGHT:
                            block["alive"] = False
                            self.ball_vy = -self.ball_vy
                            break

        elif self.scene == "gameover":
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.reset_paddle()
                self.reset_ball()
                self.reset_blocks()
                self.scene = "play"

    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)

        if self.scene == "play":
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
            for block in self.blocks:
                if block["alive"]:
                    pyxel.rect(
                        block["x"],
                        block["y"],
                        BLOCK_WIDTH - 1,
                        BLOCK_HEIGHT - 1,
                        pyxel.COLOR_LIGHT_BLUE
                    )

        elif self.scene == "gameover":
            pyxel.text(60, 60, "GAME OVER", pyxel.COLOR_WHITE)
            pyxel.text(55, 80, "PRESS ENTER", pyxel.COLOR_WHITE)

App()