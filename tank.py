import pygame
from typing import Tuple
from random import randint


class Tank:
    def __init__(self, x: int, y: int, radius: int, color: Tuple[int, int, int]) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = 3

    def draw(self, window) -> None:
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def move(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if keys[pygame.K_UP]:
            self.y -= self.speed

        if keys[pygame.K_DOWN]:
            self.y += self.speed