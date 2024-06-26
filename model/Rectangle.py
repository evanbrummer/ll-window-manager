class Rectangle:
    def __init__(self, x0, y0, x1, y1):
        self.rid: int = None
        self.x0: int = x0
        self.y0: int = y0
        self.x1: int = x1
        self.y1: int = y1

    def intersects(self, x, y):
        return self.x0 <= x <= self.x1 and self.y0 <= y <= self.y1
