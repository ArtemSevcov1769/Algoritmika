from pygame import *
FPS = 60

WIDTH, HEIGHT = 600, 400
mw = display.set_mode((WIDTH, HEIGHT))
back_img = 'pixil-frame-0 (4).png'
platform_img = 'platforn.png'
display.set_caption('Ping_pong')

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
platform_1 = Player(platform_img, 10, HEIGHT/2, 15, 90, 5, K_w, K_s)
platform_2 = Player(platform_img, 570, HEIGHT/2, 15, 90, 5, K_UP, K_DOWN)

background = GameSprite(back_img, 0, 0, 600, 400)
game = True
clock = time.Clock()
while game:
    background.reset()
    platform_1.update()
    platform_2.update()
    platform_1.reset()
    platform_2.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
    
