from math import isclose, pow, sqrt
from matplotlib import pyplot as plt


class Star:
    def __init__(self, x, y, r, label=None):
        self.x, self.y, self.r, self.label = x, y, r, label

    def __eq__(self, other):
        if isinstance(other, Star):
            return isclose(self.x, other.x) and isclose(self.y, other.y)
        return False

    def __str__(self):
        res = '(' + str(self.x) + ', ' + str(self.y) + ')'
        if self.label:
            res += ': ' + self.label
        return res

    def list(self):
        return [self.x, self.y]

    def plot(self, ax=None):
        if ax is None:
            plt.plot(self.x, self.y, 'o')
        else:
            ax.plot(self.x, self.y, 'o')

    def distance(self, other):
        if isinstance(other, Star):
            return sqrt(pow(other.x - self.x, 2) + pow(other.y - self.y, 2))
        return None

    def near(self, other, tolerance=250):
        if isinstance(other, Star):
            return self.distance(other) < tolerance
        return False
