import cv2
import sys
import os

from cv2 import imread
from starimage import StarImage

cv2.setUseOptimized(True)


class NightSky(StarImage):
    def __init__(self, filepath, star_limit=20, tri_method=0, tri_limit=1000, tri_tol=250):
        if not os.path.exists(filepath):
            print("File Error: File could not be found at '%s'" % filepath, file=sys.stderr)
            return
        self.path = filepath
        self.name = os.path.splitext(os.path.basename(self.path))[0]
        self.src = imread(self.path)
        self.filter = self._filter(self.src)
        self.threshold = self._threshold(self.filter)
        super().__init__(self.filter, star_limit, tri_method, tri_limit, tri_tol)

    def _filter(self, image):
        filter = cv2.ximgproc.anisotropicDiffusion(image, 0.2, 0.1, 50)
        return cv2.cvtColor(filter, cv2.COLOR_BGR2GRAY)

    def _threshold(self, image):
        _, threshold = cv2.threshold(image, 115, 255, cv2.THRESH_BINARY)
        return cv2.adaptiveThreshold(threshold, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 0)

    def plot(self, ax=None, src=True, filtered=True, threshold=True, stars=True, triangles=True):
        if src:
            super(NightSky, self)._show_image(self.src)
        if filtered:
            super(NightSky, self)._show_image(self.filter)
        if threshold:
            super(NightSky, self)._show_image(self.threshold)
        super(NightSky, self).plot(ax, stars, triangles)
