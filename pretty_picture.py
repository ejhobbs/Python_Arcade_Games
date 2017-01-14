import pygame
import math

DARK_GREEN = (63,133,11)
GREEN = (106,201,58)
LIGHT_GREEN = (120,222,69)
SKY_BLUE = (61,219,204)
BROWN = (107,86,17)
SUN_YELLOW = (255,217,0)
PI = math.pi

pygame.init()

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("The Prettiest Picture")
clock  = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(SKY_BLUE)

    #draw sun
    pygame.draw.circle(screen,SUN_YELLOW,[650,50],30)

    #draw hills
    pygame.draw.ellipse(screen,DARK_GREEN,[-300,150,800,600],0)
    pygame.draw.ellipse(screen,GREEN,[300,250,700,600])

    #draw ground
    pygame.draw.ellipse(screen,LIGHT_GREEN,[0,400,700,300])

    pygame.display.flip()
    clock.tick(60)
pygame.quit()