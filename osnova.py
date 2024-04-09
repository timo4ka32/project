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


class Enemy(GameSprite):

    def update(self):
        global missing
        self.rect.y += self.speed
        if self.rect.y >= 500:
            missing += 1
            self.rect.y = 0
            self.rect.x = randint(1,500)
        

    



window = display.set_mode((700, 500))
display.set_caption('пинг понг')
background = transform.scale(image.load('zfon.jpg'), (700, 500))
clock = time.Clock()
FPS = 120
 
shariks = sprite.Group()
for i in range(1):
    sharik = Enemy('sharik.png',randint(0,500),randint(-200,-50),randint(1,4))
    shariks.add(sharik)




raketka = Player('racket.png', 310,410,4)
ufos = sprite.Group()
bullets = sprite.Group()


finish = False
game = True 
while game:
    if finish != True:
        window.blit(background,(0,0))
        raketka.reset()
        raketka.update()
        shariks.update()
        shariks.draw(window)
        bullets.update()

    for e in event.get():
        if e.type == QUIT:
            game = False
    


    display.update()
    clock.tick(FPS)
