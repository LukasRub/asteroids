from circleshape import CircleShape
from constants import ASTEROID_LINE_WIDTH

import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Overrides CircleShape.draw method
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 
                           width=ASTEROID_LINE_WIDTH)

    # Overrides CircleShape.update method
    def update(self, delta_time):
        self.position += self.velocity * delta_time