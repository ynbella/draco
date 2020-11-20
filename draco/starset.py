import networkx

from draco.star import Star
from draco.triangle import Triangle
import matplotlib.pyplot as plt

class StarSet:
    def __init__(self, stars):
        self.stars = stars
        self.triangles = self._permute_triangles(stars)
        self.graph = self._generate_graph(self.triangles)

    def _permute_triangles(self, stars):
        triangles = []
        n = len(stars)
        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    triangles.append(Triangle(stars[i], stars[j], stars[k]))
        return triangles

    def _generate_graph(self, triangles):
        graph = networkx.Graph()

        for i in range(len(triangles)):
            new_triangle = triangles[i]
            graph.add_node(i, triangle=new_triangle)
            for j in range(len(graph.nodes)):
                existing_node = graph.nodes[j]
                existing_triangle = existing_node['triangle']
                if isinstance(existing_triangle, Triangle):
                    if new_triangle.is_connected_to(existing_triangle):
                        graph.add_edge(i, j)

        networkx.write_edgelist(graph, path="grid.edgelist", delimiter=":")
        # read edgelist from grid.edgelist
        H = networkx.read_edgelist(path="grid.edgelist", delimiter=":")

        networkx.draw(H)
        plt.show()
        print(graph)
        return graph



a = Star(1, 2, 3)
b = Star(4, 5, 6)
c = Star(7, 3, 4)
d = Star(9, 1, 2)
e = Star(4, 2, 4)
f = Star(2, 9, 1)

stars = [a, b, c, d, e,f]
set = StarSet(stars)
