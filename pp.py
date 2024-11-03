from pygame import *
class gamesprite(sprite.Sprite):
    def __init__(self, speed, pimage, rect_x, rect_y, size_x, size_y):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(pimage), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class player(gamesprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y  > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 635:
            self.rect.x += self.speed

window = display.set_mode((700, 500))
background = transform.scale(image.load('images.jpg'), (700, 500))



game = True
clock = time.Clock()

while game:
    window.blit(background, (0, 0))
    for i in event.get():
        if i.type == QUIT:
            game = False
    display.update()
    clock.tick(60)