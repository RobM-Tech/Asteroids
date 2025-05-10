import pygame, circleshape, random
from constants import *


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.add(*self.containers)


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        ran_angle = random.uniform(20, 50)
        
        A1 = self.velocity.rotate(ran_angle)
        A2 = self.velocity.rotate(-ran_angle)
        velocity_1 = A1 * 1.2
        velocity_2 = A2 * 1.2

        old_radius = self.radius
        new_radius = old_radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        new_asteroid1.velocity = velocity_1
        new_asteroid2.velocity = velocity_2

        new_asteroid1.add(*new_asteroid1.containers)
        new_asteroid2.add(*new_asteroid2.containers)




    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), tuple(map(int, self.position)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt