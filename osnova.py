from typing import Any
from pygame import *
from random import * 
score = 0
missing = 0

font.init()
font2 = font.Font(None,30)







window = display.set_mode((700,500))
display.set_caption('...')
background = transform.scale(image.load('fon.jpg'),(700,500))
clock = time.Clock()
FPS = 60

# mixer.init()
# mixer.music.load('muzik.ogg')
# mixer.music.play()

finish = False
game = True 
while game:
    if finish != True:
        window.blit(background,(0,0))
