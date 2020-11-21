from math import acos, pow, sqrt, degrees, isclose
from itertools import combinations

from star import Star


class Triangle:
    def __init__(self, a: Star, b: Star, c: Star):
        self.stars = [a, b, c]
        self.sides = self._calculate_sides(self.stars)
        self.sorted_sides = sorted(self.sides)
        self.angles = self._calculate_angles(self.sides)
        self.sorted_angles = sorted(self.angles)
        self.normalized_sides = self._normalize_sides(self.sides)
        self.sorted_normalized_sides = sorted(self.normalized_sides)

    @staticmethod
    def _calculate_sides(points):
        sides = []
        edges = combinations(points, 2)
        for edge in edges:
            sides.append(sqrt(pow(edge[1].x - edge[0].x, 2) + pow(edge[1].y - edge[0].y, 2)))
        return sides

    @staticmethod
    def _calculate_angles(sides):
        angles = []
        n = len(sides)
        for i in range(n):
            a = sides[i % n]
            b = sides[(i + 2) % n]
            c = sides[(i + 1) % n]
            numerator = pow(b, 2) + pow(c, 2) - pow(a, 2)
            denominator = 2 * b * c
            if isclose(denominator, 0):
                angles.append(0)
            else:
                angles.append(degrees(acos(max(-1.0, min(1.0, numerator / denominator)))))
        return angles

    @staticmethod
    def _normalize_sides(sides):
        minimum = min(sides)
        if isclose(minimum, 0):
            return sides
        else:
            return [side / minimum for side in sides]

    def __eq__(self, other):
        if isinstance(other, Triangle):
            return self.stars[0] == other.stars[0] and self.stars[1] == other.stars[1] and self.stars[2] == other.stars[
                2]
        return False

    def connected(self, other):
        if isinstance(other, Triangle):
            for star in self.stars:
                if star in other.stars:
                    return True
        return False

    # region Comparison

    def similar(self, other, method: int, side_tol: float = 0.1, ang_tol: float = 5.0):
        if isinstance(other, Triangle):
            if method == 0:
                return self._similar_aaa(other, ang_tol)
            elif method == 1:
                return self._similar_sas(other, side_tol, ang_tol)
            elif method == 2:
                return self._similar_sss(other, side_tol)
            else:
                print("Invalid argument: Invalid comparison method", method)
        return False

    def _similar_aaa(self, other, tol):
        for i in range(3):
            if not isclose(self.sorted_angles[i], other.sorted_angles[i], abs_tol=tol):
                return False
        return True

    def _similar_sas(self, other, side_tol, agl_tol):
        if isclose(self.sorted_sides[0] / other.sorted_sides[0], self.sorted_sides[1] / other.sorted_sides[1],
                   abs_tol=side_tol):
            if isclose(self.sorted_angles[2], other.sorted_angles[2], abs_tol=agl_tol):
                return True

        if isclose(self.sorted_sides[1] / other.sorted_sides[1], self.sorted_sides[2] / other.sorted_sides[2],
                   abs_tol=side_tol):
            if isclose(self.sorted_angles[0], other.sorted_angles[0], abs_tol=agl_tol):
                return True

        if isclose(self.sorted_sides[2] / other.sorted_sides[2], self.sorted_sides[0] / other.sorted_sides[0],
                   abs_tol=side_tol):
            if isclose(self.sorted_angles[1], other.sorted_angles[1], abs_tol=agl_tol):
                return True

        return False

    def _similar_sss(self, other, tol):
        for i in range(3):
            if not isclose(self.sorted_normalized_sides[i], other.sorted_normalized_sides[i], abs_tol=tol):
                return False
        return True

    # endregion
