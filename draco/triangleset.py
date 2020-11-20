from collections import deque
import networkx

class TriangleSet:
    def __init__(self, triangles):
        self.triangles = triangles

    def _breadth_first_search(self, triangles):
        queue = deque([triangles[0]])

        edges =

        graph = networkx.Graph()