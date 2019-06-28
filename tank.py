import pygame
from typing import Tuple
from math import sin, cos, atan2, pi
from hitbox import Hitbox
from sprites import SpritesContainer


class Tank:
    def __init__(self, x: int, y: int, radius: int, color: Tuple[int, int, int], tank_body_model: str, tank_turret_model: str, width: int, height: int) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.img_width = width
        self.img_height = height
        self.color = color
        self.speed = 3
        self.turn_speed = 0.05
        self.tank_body_model = tank_body_model
        self.tank_turret_model = tank_turret_model
        self.body_rotation = 0
        self.turret_rotation = 0
        self.hitbox = Hitbox()
        self.update_hitbox()

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

        self.update_hitbox()

    def update_hitbox(self):
        x1 = -1*self.img_width/2
        y1 = self.img_height/2

        x1 = x1 * cos(self.body_rotation) - y1 * sin(self.body_rotation) + self.x
        y1 = y1 * cos(self.body_rotation) + x1 * sin(self.body_rotation) + self.y

        x2 = self.img_width/2
        y2 = self.img_height/2

        x2 = x2 * cos(self.body_rotation) - y2 * sin(self.body_rotation) + self.x
        y2 = y2 * cos(self.body_rotation) + x2 * sin(self.body_rotation) + self.y

        x3 = self.img_width / 2
        y3 = -1*self.img_height / 2

        x3 = x3 * cos(self.body_rotation) - y3 * sin(self.body_rotation) + self.x
        y3 = y3 * cos(self.body_rotation) + x3 * sin(self.body_rotation) + self.y

        x4 = -1*self.img_width / 2
        y4 = -1*self.img_height / 2

        x4 = x4 * cos(self.body_rotation) - y4 * sin(self.body_rotation) + self.x
        y4 = y4 * cos(self.body_rotation) + x4 * sin(self.body_rotation) + self.y

        self.hitbox.update_location( (x1,y1), (x2,y2), (x3,y3), (x4,y4) )

    def detect_hit(self, point_1) -> bool:
        return self.hitbox.detect_hit_bullet(point_1)

    def update_tank_body(self, x: str) -> None:
        self.tank_body_model = x

    def update_turret_rotation(self, mouse_pos: Tuple[int, int]) -> None:
        self.turret_rotation = -atan2(mouse_pos[1], mouse_pos[0])

