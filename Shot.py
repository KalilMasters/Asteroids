from circleshape import CircleShape, pygame
from constants import *
class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_SIZE)
        velocity = pygame.Vector2(0,1).rotate(rotation)
        self.velocity = velocity * SHOT_SPEED

    def move(self, dt):
        self.position += self.velocity * dt
    
    def update(self, dt):
        self.move(dt)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, SHOT_SIZE, 2)