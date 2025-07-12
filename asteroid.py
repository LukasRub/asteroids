from circleshape import CircleShape
from constants import (ASTEROID_LINE_WIDTH,
                       ASTEROID_MIN_RADIUS)

import random

import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            # If the asteroid is too small, it does not split
            return
        
        random_angle = random.uniform(20, 50)

        velocities = [self.velocity.rotate(random_angle), 
                      self.velocity.rotate(-random_angle)]
        radii = [self.radius - ASTEROID_MIN_RADIUS] * 2

        for radius, velocity in zip(radii, velocities):
            asteroid = Asteroid(*self.position, radius)
            asteroid.velocity = velocity * 1.2



    # Overrides CircleShape.draw method
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 
                           width=ASTEROID_LINE_WIDTH)

    # Overrides CircleShape.update method
    def update(self, delta_time):
        self.position += self.velocity * delta_time