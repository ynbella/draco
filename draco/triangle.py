from math import acos, pow, sqrt, degrees, isclose
from itertools import combinations

from draco.star import Star


class Triangle:
    def __init__(self, a: Star, b: Star, c: Star):
        self.stars = [a, b, c]

        self.sides = self._calculate_sides(self.stars)
        self.sorted_sides = sorted(self.sides)
        self.angles = self._calculate_angles(self.sides)
        self.sorted_angles = sorted(self.angles)
        self.normalized_sides = self._normalize_sides(self.sides)
        self.sorted_normalized_sides = sorted(self.normalized_sides)

    def _calculate_edges(self, points):
        return combinations(points, 2)

    def _calculate_sides(self, points):
        sides = []
        edges = combinations(points, 2)
        for edge in edges:
            print(edge)
            sides.append(sqrt(pow(edge[1].x - edge[0].x, 2) + pow(edge[1].y - edge[0].y, 2)))
        return sides

    def _calculate_angles(self, sides):
        angles = []
        n = len(sides)
        for i in range(n):
            a = sides[i % n]
            b = sides[(i + 2) % n]
            c = sides[(i + 1) % n]
            angles.append(degrees(acos((pow(b, 2) + pow(c, 2) - pow(a, 2)) / (2 * b * c))))
        return angles

    def _normalize_sides(self, sides):
        minimum = min(sides)
        normalized_sides = [side / minimum for side in sides]
        return normalized_sides

    def __eq__(self, other):
        # Overrides the default implementation
        if isinstance(other, Triangle):
            return self.stars == other.stars
        return False

    def is_equal_to(self, other):
        return self == other

    def is_connected_to(self, other):
        if isinstance(other, Triangle):
            for star in self.stars:
                if star in other.stars:
                    return True
        return False

    def is_similar_to(self, other):
        # AAA similarity
        if isinstance(other, Triangle):
            for i in range(3):
                if not isclose(self.sorted_angles[i], other.sorted_angles[i], abs_tol=5.0):
                    return False
            return True
        return False
