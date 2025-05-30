from circleshape import CircleShape
from constants import *

import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = (pygame.Vector2(0, 1).rotate(self.rotation + 90) 
                 * self.radius / 1.5)
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    

    def draw(self, screen: pygame.Surface):
        points = self.triangle()
        pygame.draw.polygon(screen, "white", points, width=2)

    
    def rotate(self, dt: int):
        self.rotation += PLAYER_TURN_SPEED * dt

    
    def move(self, dt: int):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def update(self, dt: int):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # rotate left
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # rotate right
            self.rotate(dt)
        if keys[pygame.K_w]:
            # move forward
            self.move(dt)
        if keys[pygame.K_s]:
            # move backward
            self.move(-dt)