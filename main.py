import pygame, asteroidfield
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # sets screen

    

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) # generates player

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)




    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 return
        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)
        
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                exit()
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
        

if __name__ == "__main__":
    main()