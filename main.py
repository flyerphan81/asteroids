# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player1 = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))

    clock = pygame.time.Clock()
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for thing1 in updatable:
            thing1.update(dt)
        for thing2 in drawable:
            thing2.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000 

if __name__ == "__main__":
    main()