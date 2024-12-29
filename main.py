# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
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
        for asteroid in asteroids:
            if player1.collisions(asteroid):
               sys.exit("GAME OVER!")
            for bullet in shots:    
                if asteroid.collisions(bullet):
                    asteroid.kill()
                    bullet.kill() 
        for thing2 in drawable:
            thing2.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000 

if __name__ == "__main__":
    main()