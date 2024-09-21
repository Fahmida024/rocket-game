import pygame
from time import*
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode([500,500])
playing=True
img1=pygame.image.load('images/rocket.png')
img2=pygame.image.load('images/background.png')

playerx=200
playery=200

while playing:
    screen.blit(img2,(0,0))
    screen.blit(img1,(playerx,playery))
    pygame.display.flip()
    if playery>500:
        playing=False 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
        if event.type==pygame.KEYDOWN:
            if event.key==K_UP:
                if playery>0:
                    playery=playery-15
            if event.key==K_DOWN:
                if playery<500:
                    playery=playery+15
            if event.key==K_LEFT:
                if playerx>0:
                    playerx=playerx-15
            if event.key==K_RIGHT:
                if playerx<500:
                    playerx=playerx+15
    playery=playery+5
    sleep(0.07)
print('Game over')



    



