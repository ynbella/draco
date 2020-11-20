import os
import sys

import cv2
import numpy as np
from math import sqrt
from skimage.feature import blob_dog, blob_log, blob_doh

from draco.star import Star


class Constellation:
    def __init__(self, img_path):
        if not os.path.exists(img_path):
            print("File Error: File could not be found at '%s'" % img_path, file=sys.stderr)
            return
        self.path = img_path
        self.name = os.path.splitext(os.path.basename(img_path))[0]
        self.img = cv2.imread(img_path)
        self.filter = self._filter_image(self.img)
        self.stars = self._detect_stars(self.filter)

    def _filter_image(self, img):
        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        lower = np.array([110.0, 125.0, 70.0])
        upper = np.array([130.0, 230.0, 180.0])
        mask = cv2.inRange(hsv, lower, upper)
        self._show_image(mask)
        return mask

    def _show_image(self, img):
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def _detect_stars(self, img):
        blobs = blob_log(img, max_sigma=30, num_sigma=10, threshold=.2)
        blobs[:, 2] = blobs[:, 2] * sqrt(2)
        stars = []
        for blob in blobs:
            y, x, r = blob
            star = Star(x, y, r)
            self.stars.append(star)
        return stars

    def _generate_graph(self):


path = '../data/constellations/orion.png'
stars = Constellation(path)
