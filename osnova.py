from pygame import *
from random import randint

score = 0
missing = 0

font.init()
font2 = font.Font(None,40)

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(60,70))
        self.speed = player_speed
        self.speedX = player_speed
        self.speedY = player_speed
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
     
     def update(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY
        if self.rect.y <= 0:
            self.speedY *= -1
        if self.rect.y >= 450:
            self.speedY *= -1

        if sprite.collide_rect(sharik, raketka2):
            self.speedX *= -1
            self.speedY *= -1
        if sprite.collide_rect(sharik, raketka):
            self.speedX *= -1
            self.speedY *= -1
            
        
# фон
window = display.set_mode((700, 500))
display.set_caption('Тенис')
background = transform.scale(image.load('zfon.png'), (700, 500))
clock = time.Clock()



FPS = 120
# шарик
sharik = Enemy('sharik.png',250, 250, 2)
# ракетки
raketka = Player('racket.png', 50,240,3)
raketka2 = Player2('racket.png', 594,240,3)

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
    
    text1 = font2.render(str(score), 1, (0,0,0))
    window.blit(text1,(335,20))

    
    display.update()
    clock.tick(FPS)


