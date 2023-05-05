import pygame
class Button():
    def __init__(self, x=0, y=0, width=0, height=0, text='Default',
                 text_color = (0, 255, 255), text_size=20, normal_color=(20, 20, 20),
                 hover_color=(150, 250, 150), center_x=True
                 ):
        self.rect = pygame.Rect(x, y, width, height)
        self.text_color = text_color
        self.text = text
        self.normal_color = normal_color
        self.hover_color = hover_color
        self.font = pygame.font.Font(None, text_size)
        if center_x == True:
            w_width, w_height = pygame.display.get_window_size()
            w_rect = pygame.Rect(0, 0, w_width, w_height)
            self.rect.centerx = w_rect.centerx
        self.is_hover = False
    def draw(self, window):
        if self.is_hover:
            color = self.hover_color
        else:
            color = self.normal_color
        pygame.draw.rect(window, color, self.rect)
        text = self.font.render(self.text, True, self.text_color)
        text_rect = text.get_rect()
        text_rect.center = self.rect.center
        window.blit(text, (text_rect.x, text_rect.y))
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                if self.rect.collidepoint(event.pos):
                    self.is_hover = True
                    break
                else:
                    self.is_hover = False
    def is_clicked(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    return True
        return False

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((500, 600))
window.fill((255, 255, 255))
clock = pygame.time.Clock()
btn = Button(y=200, width=150, height=40, text='lskajhfaf', text_size=30)

run = True
while run:
    events = pygame.event.get()
    if btn.is_clicked(events):
        print('btn click')
    btn.update(events)
    btn.draw(window)
    for event in events:
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    clock.tick(30)