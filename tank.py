import pygame
from typing import Tuple
from math import sin, cos, atan2, pi


class Tank:
    def __init__(self, x: int, y: int, radius: int, color: Tuple[int, int, int], tank_body_model: str, tank_turret_model: str) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = 3
        self.turn_speed = 0.05
        self.tank_body_model = tank_body_model
        self.tank_turret_model = tank_turret_model
        self.body_rotation = 0
        self.turret_rotation = 0

    def draw(self, window: pygame.display) -> None:
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
        pygame.draw.line(window, self.color, (self.x, self.y), (self.x+15*cos(self.turret_rotation), self.y+15*sin(self.turret_rotation)), 3)

    def move(self, keys) -> None:
        if keys[pygame.K_w]:
            self.x += self.speed * cos(self.body_rotation)
            self.y -= self.speed * sin(self.body_rotation)

        if keys[pygame.K_d]:
            self.body_rotation -= self.turn_speed
            if self.body_rotation < 0:
                self.body_rotation = self.body_rotation + 2 * pi
            self.body_rotation = self.body_rotation % (2 * pi)

        if keys[pygame.K_a]:
            self.body_rotation += self.turn_speed
            if self.body_rotation < 0:
                self.body_rotation = self.body_rotation + 2 * pi
            self.body_rotation = self.body_rotation % (2 * pi)

    def update_tank_body(self, x: str) -> None:
        self.tank_body_model = x

    def update_turret_rotation(self, mouse_pos: Tuple[int, int]) -> None:
        self.turret_rotation = -atan2(mouse_pos[1], mouse_pos[0])

