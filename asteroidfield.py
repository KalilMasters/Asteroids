import pygame, random
from asteroid import Asteroid
from constants import *

class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        a = Asteroid(position.x, position.y, radius)
        a.velocity = velocity
    
    def split_asteroid(self, asteroid):
        if asteroid.radius < ASTEROID_MIN_RADIUS:
            return
        
        self.spawn(asteroid.radius - ASTEROID_MIN_RADIUS, asteroid.position, asteroid.velocity.rotate(random.uniform(20,50)) * 1.2)
        self.spawn(asteroid.radius - ASTEROID_MIN_RADIUS, asteroid.position, asteroid.velocity.rotate(-random.uniform(20,50)) * 1.2)

    
    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            #Grab random edge to spawn at
            edge = random.choice(self.edges)

            #Random speed between 40 and 100
            speed = random.randint(40, 100)
            #Multiply speed by given vector from edge
            velocity = edge[0] * speed
            #Add a little bit of randomness to the direction
            velocity = velocity.rotate(random.randint(-30, 30))
            #Shift the position on the edge randomly
            position = edge[1](random.uniform(0,1))
            #Determine size
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MAX_RADIUS * kind, position, velocity)