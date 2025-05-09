import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # sets screen

    

    #groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) # generates player


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
        
        updateable.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
        

if __name__ == "__main__":
    main()