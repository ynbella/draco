import os
import sys

from cv2 import COLOR_RGB2HSV, cvtColor, imread, inRange
from numpy import array

from starimage import StarImage


class Constellation(StarImage):
    def __init__(self, filepath, tri_method=0, tri_limit=1000, tri_tol=250):
        if not os.path.exists(filepath):
            print("File Error: File could not be found at '%s'" % filepath, file=sys.stderr)
            return
        self.path = filepath
        self.name = os.path.splitext(os.path.basename(self.path))[0]
        self.src = imread(self.path)
        self.filter = self._filter(self.src)
        super().__init__(self.filter, -1, tri_method, tri_limit, tri_tol)

    def _filter(self, image):
        hsv = cvtColor(image, COLOR_RGB2HSV)
        lower = array([110.0, 125.0, 70.0])
        upper = array([130.0, 230.0, 180.0])
        mask = inRange(hsv, lower, upper)
        return mask

    def plot(self, ax=None, src=True, filtered=True, stars=True, triangles=True):
        if src:
            super(Constellation, self)._show_image(self.src)
        if filtered:
            super(Constellation, self)._show_image(self.filter)
        super(Constellation, self).plot(ax, stars, triangles)
