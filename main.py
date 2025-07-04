import pygame
from constants import *
from player import Player, Shot
from asteroidfield import AsteroidField, Asteroid

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    dt = 0
    

    update_group = pygame.sprite.Group()
    draw_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (update_group, draw_group)
    Asteroid.containers = (asteroid_group, update_group, draw_group)
    AsteroidField.containers = (update_group,)
    Shot.containers = (shot_group, update_group, draw_group)
    

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            return
        
        screen.fill("black")
        
        update_group.update(dt)
        for drawable in draw_group:
            drawable.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        del_group = []
        for a in asteroid_group:
            if a.CheckCollision(player):
                return
            for shot in shot_group:
                if(a.CheckCollision(shot)):
                    del_group.append(shot)
                    del_group.append(a)
                    asteroid_field.split_asteroid(a)
        
        for k in del_group:
            k.kill()

        


if __name__ == "__main__":
    main()
    print("Game Over!")
