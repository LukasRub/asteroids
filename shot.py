from circleshape import CircleShape
from constants import (SHOT_RADIUS,
                       SHOT_LINE_WIDTH)

import pygame


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    # Overrides CircleShape.draw method
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 
                           width=SHOT_LINE_WIDTH)

    # Overrides CircleShape.update method
    def update(self, delta_time):
        self.position += self.velocity * delta_time
