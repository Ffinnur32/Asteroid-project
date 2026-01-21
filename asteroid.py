import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius,):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")

        new_angle = random.uniform(20, 50)

        angle_a = self.velocity.rotate(new_angle)
        angle_b = self.velocity.rotate(-new_angle)

        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_a = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid_a.velocity = angle_a * 1.2
        asteroid_b = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid_b.velocity = angle_b * 1.2