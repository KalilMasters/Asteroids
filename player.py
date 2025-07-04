import pygame
from circleshape import CircleShape
from constants import *
from Shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = PLAYER_SHOT_COOLDOWN
    
    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt, dir):
        self.rotation += PLAYER_TURN_SPEED * dt *  dir

    def move(self, dt, dir):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * dir
    
    def shoot(self):
        if self.shot_cooldown < PLAYER_SHOT_COOLDOWN:
            return
        shot = Shot(self.position.x, self.position.y, self.rotation)
        self.shot_cooldown = 0

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt, -1)
        if keys[pygame.K_d]:
            self.rotate(dt, 1)
        if keys[pygame.K_w]:
            self.move(dt, 1)
        if keys[pygame.K_s]:
            self.move(dt, -1)

        if keys[pygame.K_SPACE]:
            self.shoot()
        self.shot_cooldown += dt
