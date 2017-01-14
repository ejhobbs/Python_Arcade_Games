import pygame
import math

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
PI = math.pi

pygame.init()

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Title Text")
clock  = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    ## game logic here


    ## drawing code here
    screen.fill(WHITE)
    pygame.draw.line(screen,RED,[100,50],[300,230],5)
    pygame.draw.rect(screen,GREEN,[50,50,100,200],5)
    pygame.draw.ellipse(screen,GREEN,[300,50,100,200],5)
    ##arcs

    pygame.draw.arc(screen, RED, [550, 50, 100,200],PI/2,PI,5)
    pygame.draw.arc(screen,BLACK,[550,50,100,200],0,PI/2,5)
    pygame.draw.arc(screen,RED,[550,50,100,200],3*PI/2,2*PI,5)
    pygame.draw.arc(screen,BLACK,[550,50,100,200],PI,3*PI/2,5)
    ## X
    for x_offset in range(30,300,30):
        pygame.draw.line(screen,GREEN,[x_offset,300],[x_offset-10,290],5)
        pygame.draw.line(screen,GREEN,[x_offset,290],[x_offset-10,300],5)

    ##poly
    pygame.draw.polygon(screen,RED,[[50,350],[70,350],[65,400]],5)

    ##text
    calibri = pygame.font.SysFont('Calibri',18,False,False)
    text = calibri.render("The Game",True,RED)
    screen.blit(text,[30,400])

    pygame.display.flip()
    clock.tick(60)
pygame.quit()