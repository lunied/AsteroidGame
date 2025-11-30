import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", (self.position[0], self.position[1]), self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            vec1 = 1.2 * self.velocity.rotate(random_angle)
            vec2 = 1.2 * self.velocity.rotate(-random_angle)
            radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position[0], self.position[1], radius)
            asteroid1.velocity = vec1
            asteroid2 = Asteroid(self.position[0], self.position[1], radius)
            asteroid2.velocity = vec2
