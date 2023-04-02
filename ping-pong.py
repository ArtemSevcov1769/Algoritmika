from pygame import *
FPS = 60

bg_color = (0, 255, 0)
WIDTH, HEIGHT = 600, 400
mw = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Ping_pong')
mw.fill(bg_color)
class GameSprite(sprite.Sprite):
    def __init__(self, sprite_img, x=0, y=0, w=50, h=50):
        self.image = transform.scale(image.load(sprite_img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
game = True
clock = time.Clock()
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
    
