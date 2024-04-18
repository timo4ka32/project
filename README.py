from pygame import *
from random import randint


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT]:
            self.rect.x -= 5
        if keys_pressed[K_RIGHT]:
            self.rect.x += 5

class Enemy(GameSprite):
    directionX = 'right'
    directionY = 'down'
    def update(self):
        global health
        if self.rect.x <= 470:
            self.directionX = 'right'
        if self.rect.x > 600:
            self.directionX = 'left'
        
        if self.rect.y >= 435:
            self.directionY = 'up'
        if self.rect.y <= 0:
            self.directionY = 'down'



        if self.directionY == 'up':
            self.rect.y -= self.speed
        if self.directionY == 'down':
            self.rect.y += self.speed
        
        
        if self.rect.y >= 499:
            self.rect.y = randint(-200, 50)
            self.rect.x = randint(0, 650)
            health -= 1

        
clock = time.Clock()
window = display.set_mode((700, 500))
display.set_caption("Пинг понг")
background = transform.scale(image.load("Fon.jpg"), (700, 500))


sprite1 = Player('Player_dos.png', 250, 400, 7)

Enemys = sprite.Group()
for i in range(1):
    EnemyE = Enemy('sharik.png', randint(0, 650), randint(-200, -50), randint(1, 4))
    Enemys.add(EnemyE)

bullets = sprite.Group()

FPS = 60


score = 0
health = 3

    

font.init()
font = font.Font(None, 50)

lose = font.render('+1', True, (255, 255, 255))
final_text = font.render('Ты проиграл', True, (255, 255, 255))


game = True

finish = False
while game:
    if not finish:
        window.blit(background, (0, 0))
        sprite1.reset()
        sprite1.update()
        Enemys.update()
        Enemys.draw(window)
        
        if health == 0:
            finish = True
            window.blit(final_text, (250, 200))

    collides = sprite.groupcollide(Enemys, bullets, True, True)
    for c in collides:
        EnemyE = Enemy('sharik.png', randint(0, 650), randint(-200, -50), randint(1, 4))
        Enemys.add(EnemyE)

    if sprite.spritecollide(sprite1, Enemys, False):
        finish = True
    


    schet = font.render('Счет: '+ str(score), True, (255, 255, 255))
    propysh = font.render('Жизней: ' + str(health), True, (255, 255, 255))
    window.blit(schet, (10, 20))
    window.blit(propysh, (10, 50))

    for j in Enemys:
        if sprite.collide_rect(sprite1, j):
            window.blit(lose, (200, 0))
            score += 1


    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
clock.tick(FPS)






from typing import Any
from pygame import *
from random import * 
score = 0
missing = 0

font.init()
font2 = font.Font(None,30)

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
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx,self.rect.centery,5)
        bullets.add(bullet)



class Enemy(GameSprite):

    def update(self):
        global missing
        self.rect.y += self.speed
        if self.rect.y >= 500:
            missing += 1
            self.rect.y = 0
            self.rect.x = randint(1,500)
        
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()

window = display.set_mode((700,500))
display.set_caption('Шутер')
background = transform.scale(image.load('galaxy.jpg'),(700,500))
clock = time.Clock()
FPS = 60

rocket = Player('rocket.png', 310,410,4)
ufos = sprite.Group()
for i in range(6):
    ufo = Enemy('ufo.png',randint(0,500),randint(-200,-50),randint(1,4))
    ufos.add(ufo)

bullets = sprite.Group()



mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()



finish = False
game = True 
while game:
    if finish != True:
        window.blit(background,(0,0))
        rocket.reset()
        rocket.update()
        ufos.update()
        ufos.draw(window)
        bullets.update()
        bullets.draw(window)
        collides = sprite.groupcollide(ufos,bullets,True, True)
        for c in collides:
            score += 1
            ufo = Enemy('ufo.png',randint(0,500),randint(-200,-50),randint(1,4))
            ufos.add(ufo)
        text1 = font2.render('Счет:' + str(score), 1, (255,255,255))
        text2 = font2.render('Пропусков:' + str(missing),1,(255,255,255))
        
        window.blit(text1,(10,20))
        window.blit(text2,(10,50))




    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                rocket.fire()
    display.update()
    clock.tick(FPS)


