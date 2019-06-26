from math import sin, cos, atan2, pi

bullet_speed = 10

class Bullet:
    def __init__(self, x :int, y:int, turret_angle :int):
        self.x = x
        self.y = y
        self.bullet_angle = turret_angle

        self.bullet_lifetime = 300

        self.x_velocity = bullet_speed * cos(turret_angle)
        self.y_velocity = -(bullet_speed * sin(turret_angle))

    def update(self) -> bool:
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.bullet_lifetime -= 1
        return self.bullet_lifetime == 0




