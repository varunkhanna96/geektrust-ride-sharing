import math


def calculate_distance(x1: int, y1: int, x2: int, y2: int) -> float:
    point_1 = [x1, y1]
    point_2 = [x2, y2]
    return round(math.dist(point_1, point_2), 2)
