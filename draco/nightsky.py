import cv2
import sys
import os
from math import sqrt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray

import matplotlib.pyplot as plt

from draco.constellation import Constellation
from draco.star import Star
from draco.trianglegraph import TriangleGraph

cv2.setUseOptimized(True)
import numpy as np

from matplotlib import pyplot as plt


class NightSky:
    def __init__(self, img_path):
        if not os.path.exists(img_path):
            print("File Error: File could not be found at '%s'" % img_path, file=sys.stderr)
            return
        self.img = cv2.imread(img_path)
        self.filter = self._filter_image(self.img)
        self.threshold = self._threshold_Image(self.filter)
        self.stars = self._detect_stars(self.threshold)
        self.stars = self._filter_stars(self.stars)
        self.graph = self._generate_graph(self.stars)

    # Anisotropic filtering - Removes background noises
    def _filter_image(self, image):
        filter = cv2.ximgproc.anisotropicDiffusion(image, 0.2, 0.1, 50)
        return cv2.cvtColor(filter, cv2.COLOR_BGR2GRAY)

    # Adaptive thresholding - Binarizes image into stars
    def _threshold_Image(self, image):
        _, threshold = cv2.threshold(image, 115, 255, cv2.THRESH_BINARY)
        return cv2.adaptiveThreshold(threshold, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 0)

    # Blob detection - Detects stars on image
    def _detect_stars(self, image):
        points = blob_log(image, max_sigma=30, num_sigma=10, threshold=.2)
        points[:, 2] = points[:, 2] * sqrt(2)

        stars = []
        for point in points:
            x, y, r = point
            star = Star(x, y, 0)
            stars.append(star)
        return stars

    def _filter_stars(self, stars):
        sorted_stars = sorted(stars, key=lambda x: x.r, reverse=True)
        del sorted_stars[100:]
        return sorted_stars

    def _generate_graph(self, stars):
        return TriangleGraph(stars)

    def contains_constellation(self, constellation):
        return self.graph.contains(constellation.graph)

    def _show_image(self, img):
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


nightsky = NightSky('../data/aries.png')

x, y = [], []
for i in range(len(nightsky.stars)):
    star = nightsky.stars[i]
    x.append(star.x)
    y.append(star.y)

plt.plot(x, y)
plt.show()

const = Constellation('../data/constellations/orion.png')

print(nightsky.contains_constellation(const))
