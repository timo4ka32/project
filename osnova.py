from pygame import *
from random import randint

score = 0
missing = 0


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(60,70))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressend = key.get_pressed() 
        if keys_pressend[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressend[K_s] and self.rect.y <= 440:
            self.rect.y += self.speed
        if keys_pressend[K_a] and self.rect.x >= 0:
            self.rect.x -= self.speed
        if keys_pressend[K_d] and self.rect.x <= 640:
            self.rect.x += self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressend = key.get_pressed() 
        if keys_pressend[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressend[K_DOWN] and self.rect.y <= 440:
            self.rect.y += self.speed
        if keys_pressend[K_LEFT] and self.rect.x >= 0:
            self.rect.x -= self.speed
        if keys_pressend[K_RIGHT] and self.rect.x <= 640:
            self.rect.x += self.speed

class Enemy(GameSprite):
     directionX = 'right'
     def update(self):
        if self.rect.x <= 0:
            self.directionX = 'right'
        if self.rect.x >= 650:
            self.directionX = 'left'
        
        if self.directionX == 'right':
            self.rect.x += self.speed
        if self.directionX == 'left':
            self.rect.x -= self.speed


# фон
window = display.set_mode((700, 500))
display.set_caption('Пинг Понг')
background = transform.scale(image.load('zfon.jpg'), (700, 500))
clock = time.Clock()
FPS = 120
# шарик
sharik = Enemy('sharik.png',250, 250, 2)
# ракетки
raketka = Player('racket.png', 0,260,3)
raketka2 = Player2('racket.png', 644,260,3)

finish = False
game = True 
while game:
    if finish != True:
        window.blit(background,(0,0))
        raketka.reset()
        raketka.update()
        raketka2.reset()
        raketka2.update()
        sharik.reset()
        sharik.update()

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(FPS)
