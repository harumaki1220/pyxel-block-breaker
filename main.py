import pyxel

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120

PADDLE_WIDTH = 40
PADDLE_HEIGHT = 5
PADDLE_SPEED = 2

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="ブロック崩し")
        
        self.paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
        self.paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT - 5

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.paddle_x = self.paddle_x - PADDLE_SPEED
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.paddle_x = self.paddle_x + PADDLE_SPEED

    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)
        pyxel.rect(
            self.paddle_x,
            self.paddle_y,
            PADDLE_WIDTH,
            PADDLE_HEIGHT,
            pyxel.COLOR_WHITE
        )

App()