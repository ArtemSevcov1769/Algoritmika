from pygame import *
font.init()
from Button import Button
FPS = 60
WIDTH, HEIGHT = 600, 400
mw = display.set_mode((WIDTH, HEIGHT))
back_img = 'pixil-frame-0 (4).png'
platform_img = 'platforn.png'
ball_img = 'ball.png'
display.set_caption('Ping_pong')
stage = 'menu'

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, x=0, y=0, w=50, h=50):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, sprite_image, x=0, y=0, w=50, h=50, speed=5, key_up=K_w, key_down=K_s):
        super().__init__(sprite_image, x, y, w, h)
        self.speed = speed
        self.key_up = key_up
        self.key_down = key_down

    def update(self):
        keys = key.get_pressed()
        if keys[self.key_up] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[self.key_down] and self.rect.y < 310:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, sprite_image, x=0, y=0, w=32, h=32, speed=5):
        super().__init__(sprite_image, x, y, w, h)
        self.dx = speed
        self.dy = speed

    def update(self):
        if self.rect.y < 0 or self.rect.y > HEIGHT - self.rect.h:
            self.dy *= -1
        self.rect.x += self.dx
        self.rect.y += self.dy
    def player_collide(self, player):
        if sprite.collide_rect(self, player):
            self.dx *= -1
btn_start = Button(y=200, width=150, height=40, text='Начать игру', font_size=26)
btn_credits = Button(y=250, width=150, height=40, text='Разработчики', font_size=26)
btn_exit = Button(y=300, width=150, height=40, text='Выход', font_size=26)

btn_continue = Button(y=200, width=150, height=40, text='Продолжить', font_size=26)
btn_to_menu = Button(y=250, width=150, height=40, text='Вернуться в меню', font_size=26)

platform_1 = Player(platform_img, 10, HEIGHT/2, 15, 90, 5, K_w, K_s)
platform_2 = Player(platform_img, 570, HEIGHT/2, 15, 90, 5, K_UP, K_DOWN)
ball = Ball(ball_img, WIDTH/2, HEIGHT/4, 32, 32, 3)
background = transform.scale(image.load(back_img), (WIDTH, HEIGHT))

clock = time.Clock()

def game():
    mw.blit(background, (0, 0))
    platform_1.update()
    platform_2.update()
    ball.update()
    ball.reset()
    platform_1.reset()
    platform_2.reset()
    ball.player_collide(platform_1)
    ball.player_collide(platform_2)

def menu(events):
    global stage
    mw.blit(background, (0, 0))
    btn_start.update(events)
    btn_credits.update(events)
    btn_exit.update(events)
    btn_start.draw(mw)
    btn_credits.draw(mw)
    btn_exit.draw(mw)
    if btn_exit.is_clicked(events):
        stage = 'off'
    if btn_start.is_clicked(events):
        restart()
        stage = 'game'
def pause(events):
    mw.blit(background, (0, 0))
    btn_continue.update(events)
    btn_to_menu.update(events)
    btn_continue.draw(mw)
    btn_to_menu.draw(mw)
    global stage
    if btn_continue.is_clicked(events):
        stage = 'game'
    if btn_to_menu.is_clicked(events):
        stage = 'menu'
def restart():
    global platform_1, platform_2, ball
    platform_1 = Player(platform_img, 10, HEIGHT/2, 15, 90, 5, K_w, K_s)
    platform_2 = Player(platform_img, 570, HEIGHT/2, 15, 90, 5, K_UP, K_DOWN)
    ball = Ball(ball_img, WIDTH/2, HEIGHT/4, 32, 32, 3)

while stage != 'off':
    events = event.get()
    for e in events:
        if e.type == QUIT:
            stage = 'off'
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                stage = 'pause' 

    if stage == 'menu':
        menu(events)
    elif stage == 'game':
        game()
    elif stage == 'pause':
        pause(events)
    display.update()
    clock.tick(FPS)
    
