from matplotlib import pyplot as plt
from tqdm import tqdm
from scipy.spatial import Delaunay
from triangle import Triangle
from random import randrange
from tqdm import trange


class StarMap:
    def __init__(self, stars, tri_method, tri_limit, tri_tolerance):
        self.stars = stars
        self.triangles = self._triangularize(self.stars, tri_method, tri_limit, tri_tolerance)

    # region Triangularization

    def _triangularize(self, stars, method: int, limit: int, tolerance: float):
        if method == 0 or method is None:
            return self._triangularize_nested(stars)
        elif method == 1:
            return self._triangularize_clustered(stars, tolerance)
        elif method == 2:
            return self._triangularize_random(stars, limit)
        elif method == 3:
            return self._triangularize_delaunay(stars)
        else:
            print("Invalid argument: Invalid triangularization method", method)

    @staticmethod
    def _triangularize_nested(stars):
        n = len(stars)
        triangles = []
        for i in trange(0, n - 2, desc="Triangularization (nested) first loop", leave=False):
            for j in trange(i + 1, n - 1, desc="Triangularization (nested) second loop", leave=False):
                for k in trange(j + 1, n, desc="Triangularization (nested) third loop", leave=False):
                    triangle = Triangle(stars[i], stars[j], stars[k])
                    triangles.append(triangle)
        return triangles

    @staticmethod
    def _triangularize_clustered(stars, tolerance):
        n = len(stars)
        triangles = []
        for i in trange(0, n - 2, desc="Triangularization (clustered) first loop", leave=False):
            for j in trange(i + 1, n - 1, desc="Triangularization (clustered) second loop", leave=False):
                if not stars[i].near(stars[j], tolerance):
                    continue
                for k in trange(j + 1, n, desc="Triangularization (clustered) third loop", leave=False):
                    if not stars[i].near(stars[k], tolerance):
                        continue
                    triangle = Triangle(stars[i], stars[j], stars[k])
                    triangles.append(triangle)
        return triangles

    @staticmethod
    def _triangularize_random(stars, limit):
        triangles = []
        for x in trange(0, limit, desc="Triangularization (random)", leave=False):
            i = j = k = randrange(0, len(stars))
            while j == i:
                j = randrange(0, len(stars))
            while k == i or k == j:
                k = randrange(0, len(stars))
            triangle = Triangle(stars[i], stars[j], stars[k])
            triangles.append(triangle)
        return triangles

    @staticmethod
    def _triangularize_delaunay(stars):
        points = []
        triangles = []
        for star in stars:
            points.append(star.list())
        simplices = Delaunay(points).simplices
        for simplex in tqdm(simplices, desc="Triangularization (delaunay)", leave=False):
            triangle = Triangle(stars[simplex[0]], stars[simplex[1]], stars[simplex[2]])
            triangles.append(triangle)
        return triangles

    # endregion

    def plot(self, ax=None, stars=True, triangles=True):
        if stars:
            map(lambda star: star.plot(ax), self.stars)
        if triangles:
            map(lambda star: star.plot(ax), self.triangles)

    def match(self, other, method: int, side_tol: float, ang_tol: float):
        matches = misses = 0
        if isinstance(other, StarMap):
            triangles = self.triangles.copy()
            for triangle in tqdm(other.triangles, desc="Comparing constellation triangles"):
                for x in tqdm(triangles, desc="Comparing sample triangles"):
                    if triangle.similar(x, method, side_tol, ang_tol):
                        triangles.remove(x)
                        matches += 1
                        continue
                misses += 1
        return matches, misses
