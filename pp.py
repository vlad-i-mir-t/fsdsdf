from pygame import *
from random import *
x_ball = randint(1, 2)
y_ball = randint(1, 2)
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
    def update_player_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
    def update_player_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

class ball(gamesprite):
    def update(self):
        if x_ball == 1:
                self.rect.x += self.speed
        if y_ball == 1:
                self.rect.y += self.speed

                    





window = display.set_mode((700, 500))
background = transform.scale(image.load('i.png'), (700, 500))

sprite_platform = player(10, 'platform.png', 0, 250, 80, 100)
sprite_platform2 = player(10, 'platform2.png', 625, 250, 80, 100)


game = True
clock = time.Clock()

while game:
    window.blit(background, (0, 0))
    for i in event.get():
        if i.type == QUIT:
            game = False
    sprite_platform.reset()
    sprite_platform2.reset()
    sprite_platform.update_player_2()
    sprite_platform2.update_player_1()
    display.update()
    clock.tick(60)
