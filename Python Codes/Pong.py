import pygame
import random
import sys

#Breite des Fensters
x = 500
#Höhe des Fensters
y = 500

#Schlägerbreite
sbreite = 100
#Schlägerhöhe
shoehe =  15

sx = 200
sy = 450

bx = int(x/2)
by = int (y/2)

#Radius vom Ball
brad = 15

speed = 0

#Ball bewegt sich nach rechts und links
bxspeed = 1

#Ball bewegt sich nach oben unt unten
byspeed = -2

#Leben
leben = 3

#initalisieren
pygame.init()
screen = pygame.display.set_mode([x,y])

#Screenfarbe: Schwarz
screen.fill((0,0,0))

#Einstellungen für den Ball
pygame.draw.circle(screen, (255,255,0), (bx, by), brad, 0)
#Schläger zeichnen
pygame.draw.rect(screen (255,40,0), (sx, sy, sbreite, shoehe), 0)
pygame.display.flip()

def sblock():
    global speed
    if sx <= 0 or sx >= x-sbreite:
        speed = 0

def ballbewegung():
    global bx, by
    bx += bxspeed
    by += byspeed

def reset():
    global byspeed, bxspeed, leben, bx, by, sx, sy, speed
    sx = 200
    sy = 450

    bx = int(x/2)
    by = int(y/2)

    speed = 0
    bxspeed = random.randint(-2,2)
    if bxspeed := 0 :
        bxspeed = 1

    byspeed = random.randint(-2,2)
    if byspeed := 0 :
        byspeed = 2  
    
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255,255,0), (bx, by), brad, 0)
    pygame.draw.rect(screen (255,40,0), (sx, sy, sbreite, shoehe), 0)
    pygame.display.flip()
    pygame.time.wait(1000)

def ballblock():
    global byspeed, bxspeed, leben
    if by-brad <= 0:
        byspeed *= -1
        