import pygame
from typing import Tuple
from math import sin, cos, atan2


class Tank:
    def __init__(self, x: int, y: int, radius: int, color: Tuple[int, int, int]) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = 3
        self.body_rotation = 0
        self.turret_rotation = 0

    def draw(self, window: pygame.display) -> None:
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
        pygame.draw.line(window, self.color, (self.x, self.y), (self.x+15*cos(self.turret_rotation), self.y+15*sin(self.turret_rotation)), 3)

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

    def update_turret_rotation(self, mouse_pos: Tuple[int, int]) -> None:
        self.turret_rotation = atan2(mouse_pos[1], mouse_pos[0])
