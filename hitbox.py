from typing import Tuple


class Hitbox:
    def __init__(self):
        self.vertex1 = (0, 0)
        self.vertex2 = (0, 0)
        self.vertex3 = (0, 0)
        self.vertex4 = (0, 0)

    def update_location(self, vertex1, vertex2, vertex3, vertex4):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3
        self.vertex4 = vertex4

    def detect_hit_bullet(self, point: Tuple[float, float]) -> bool:
        point_x = int(point[0])
        point_y = int(point[1])
        return is_angle_convex(self.vertex1[0] - point_x, self.vertex1[1] - point_y,
                               self.vertex2[0] - point_x, self.vertex2[1] - point_y) and \
            is_angle_convex(self.vertex2[0] - point_x, self.vertex2[1] - point_y,
                            self.vertex3[0] - point_x, self.vertex3[1] - point_y) and \
            is_angle_convex(self.vertex3[0] - point_x, self.vertex3[1] - point_y,
                            self.vertex4[0] - point_x, self.vertex4[1] - point_y) and \
            is_angle_convex(self.vertex4[0] - point_x, self.vertex4[1] - point_y,
                            self.vertex1[0] - point_x, self.vertex1[1] - point_y)


def is_angle_convex(x1: int, y1: int, x2: int, y2: int) -> bool:
    return x2*y1 - x1*y2 > 0
