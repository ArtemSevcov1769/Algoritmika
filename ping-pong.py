from pygame import *
FPS = 60

WIDTH, HEIGHT = 600, 400
mw = display.set_mode((WIDTH, HEIGHT))
back_img = 'pixil-frame-0 (4).png'
display.set_caption('Ping_pong')
class GameSprite(sprite.Sprite):
    def __init__(self, sprite_img, x=0, y=0, w=50, h=50):
        self.image = transform.scale(image.load(sprite_img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

background = GameSprite(back_img, 0, 0, 600, 400)
game = True
clock = time.Clock()
while game:
    background.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
    
