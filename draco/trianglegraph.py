import networkx

from draco.triangle import Triangle
from graph_tools import Graph


class TriangleGraph:
    def __init__(self, stars):
        self.stars = stars
        self.triangles = self._permute_triangles(stars)
        #self.graph = self._generate_graph(self.triangles)

    def _permute_triangles(self, stars):
        triangles = []
        n = len(stars)
        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    triangles.append(Triangle(stars[i], stars[j], stars[k]))
        return triangles

    def contains(self, other):
        matches = 0
        misses = 0
        for dest_triangle in other.triangles:
            for src_triangle in self.triangles:
                if src_triangle.is_similar_to(dest_triangle):
                    matches += 1
                    continue
            misses += 1
        return matches, misses

