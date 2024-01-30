import pygame
import sys

partikel = 25
schlange = [[13,13],[13,14]]

pygame.init()
clock = pygame.time.clock()

screen = pygame.display.set_mode([700,700])

def zeichner():
    screen.fill((0,102,0))

    kopf = True
    for x in schlange:
        Coords = [x[0] * partikel, x[1] * partikel]
        if kopf:
            pygame.draw.rect(screen, (0,0,0), (Coords[0], Coords[1],partikel,partikel),0)
            kopf = False
        else:
            pygame.draw.rect(screen, (47,79,79), (Coords[0], Coords[1],partikel, partikel),0)

go = True
anhang = None
apfelInd = -1
ende = False
score = 0
while go:
    for event in pygame.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_UP and richtung !=2:
                richtung = 0
            if event.key == pygame.K_RIGHT and richtung != 3:
                richtung = 1
            if event.key == pygame.K_DOWN and richtung != 0:
                richtung = 2
            if event.key == pygame.K_LEFT and richtung != 1:
                richtung = 3