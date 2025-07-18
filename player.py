from circleshape import CircleShape
from shot import Shot
from constants import (PLAYER_RADIUS,
                       PLAYER_LINE_WIDTH, 
                       PLAYER_TURN_SPEED,
                       PLAYER_SPEED,
                       PLAYER_SHOOT_SPEED,
                       PLAYER_SHOOT_COOLDOWN)

import pygame


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0


    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = (pygame.Vector2(0, 1).rotate(self.rotation + 90) 
                 * self.radius / 1.5)
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    

    def move(self, delta_time):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta_time


    def rotate(self, delta_time):
        self.rotation += PLAYER_TURN_SPEED * delta_time
    

    def shoot(self):
        shot = Shot(*self.position)
        shot.velocity = (pygame.Vector2(0, 1).rotate(self.rotation) 
                         * PLAYER_SHOOT_SPEED)
    
    
    # Overrides CircleShape.draw method
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 
                            width=PLAYER_LINE_WIDTH)


    # Overrides CircleShape.update method
    def update(self, delta_time):
        self.shoot_timer -= delta_time

        keys = pygame.key.get_pressed()


        if keys[pygame.K_w]:
            self.move(delta_time)

        if keys[pygame.K_s]:
            self.move(-delta_time)

        if keys[pygame.K_a]:
            self.rotate(-delta_time)
        
        if keys[pygame.K_d]:
            self.rotate(delta_time)

        if keys[pygame.K_SPACE]:
            if self.shoot_timer > 0:
                return
            
            self.shoot()
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN