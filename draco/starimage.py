from skimage.feature import blob_log

from cv2 import imshow, waitKey, destroyAllWindows

from star import Star
from starmap import StarMap
from math import sqrt


class StarImage(StarMap):
    def __init__(self, image, star_limit, tri_method, tri_limit, tri_tol):
        self.stars = self._detect_stars(image)
        self.trimmed_stars = self._trim(self.stars, star_limit)
        super().__init__(self.trimmed_stars, tri_method, tri_limit, tri_tol)

    def _detect_stars(self, image):
        blobs = blob_log(image, max_sigma=30, num_sigma=10, threshold=.2)
        blobs[:, 2] = blobs[:, 2] * sqrt(2)
        stars = []
        for blob in blobs:
            x, y, r = blob
            star = Star(x, y, r)
            stars.append(star)
        return stars

    def _trim(self, stars, limit):
        if limit < 0:
            return stars
        else:
            sorted_stars = sorted(stars, key=lambda x: x.r, reverse=True)
            return sorted_stars[:limit]

    def _show_image(self, img):
        imshow('image', img)
        waitKey(0)
        destroyAllWindows()
