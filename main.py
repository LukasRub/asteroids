# this allows us to use code from
# the open-source pygame library
# throughout this file
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from constants import *

import sys

import pygame


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable_group = pygame.sprite.Group()
    draweable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()

    Player.containers = (updateable_group, draweable_group)
    Asteroid.containers = (asteroids_group, updateable_group, 
                           draweable_group)
    AsteroidField.containers = (updateable_group)

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    clock = pygame.time.Clock()
    delta_time = 0

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable_group.update(delta_time)
        
        for asteroid in asteroids_group:
            if asteroid.is_colliding(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for drawable in draweable_group:
            drawable.draw(screen)

        pygame.display.flip()

        delta_time = clock.tick(FPS) / 1000.0  # Convert milliseconds to seconds


if __name__ == "__main__":
    main()