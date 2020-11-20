import cv2
import sys
import os
from math import sqrt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray

import matplotlib.pyplot as plt

from draco.star import Star

cv2.setUseOptimized(True)
import numpy as np

from matplotlib import pyplot as plt


class NightSky:
    def __init__(self, img_path):
        if not os.path.exists(img_path):
            print("File Error: File could not be found at '%s'" % img_path, file=sys.stderr)
            return
        self.img = cv2.imread(img_path)
        self._show_image(self.img)
        print("Using image found at '%s'" % img_path, "with dimensions", self.img.shape)
        self._filter_image()
        self._threshold_Image()
        self._detect_stars()

    # Anisotropic filtering - Removes background noises
    def _filter_image(self):
        self.filter = cv2.ximgproc.anisotropicDiffusion(self.img, 0.2, 0.1, 50)
        self.filter = cv2.cvtColor(self.filter, cv2.COLOR_BGR2GRAY)
        self._show_image(self.filter)

    # Adaptive thresholding - Binarizes image into stars
    def _threshold_Image(self):
        _, self.threshold = cv2.threshold(self.filter, 115, 255, cv2.THRESH_BINARY)
        self.threshold = cv2.adaptiveThreshold(self.threshold, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,
                                               115, 0)
        self._show_image(self.threshold)

    # Blob detection - Detects stars on image
    def _detect_stars(self):
        image = self.threshold
        blobs = blob_log(image, max_sigma=30, num_sigma=10, threshold=.2)
        blobs[:, 2] = blobs[:, 2] * sqrt(2)
        self.stars = []
        for blob in blobs:
            y, x, r = blob
            star = Star(x, y, r)
            self.stars.append(star)

    def _show_image(self, img):
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def get_star_set(self):
        return self.stars

    def contains_constellation(self, constellation):
        graph = self.graph
        for node in graph.nodes:
            for other in constellation.graph.nodes:
                if not node.is_similar_to(other):
                    continue



path = '../data/orion.jpg'
stars = NightSky(path)
