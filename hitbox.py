

class Hitbox:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0

        self.x2 = 0
        self.y2 = 0

        self.x3 = 0
        self.y3 = 0

        self.x4 = 0
        self.y4 = 0

    def update_location(self, vertex_1, vertex_2, vertex_3, vertex_4):
        self.x1 = vertex_1[0]
        self.y1 = vertex_1[1]

        self.x2 = vertex_2[0]
        self.y2 = vertex_2[1]

        self.x3 = vertex_3[0]
        self.y3 = vertex_3[1]

        self.x4 = vertex_4[0]
        self.y4 = vertex_4[1]

    def detect_hit_bullet(self, point_1) -> bool:
        hit = True
        if (self.x4 - self.x1)*(point_1[1]-self.x1) - (point_1[0]-self.x1)*(self.y4-self.y1) < 0:
            hit = False
        if (self.x3 - self.x4)*(point_1[1]-self.x4) - (point_1[0]-self.x4)*(self.y3-self.y4) < 0:
            hit = False
        if (self.x2 - self.x3)*(point_1[1]-self.x3) - (point_1[0]-self.x3)*(self.y2-self.y3) < 0:
            hit = False
        if (self.x1 - self.x2)*(point_1[1]-self.x2) - (point_1[0]-self.x2)*(self.y1-self.y2) < 0:
            hit = False
        return hit
