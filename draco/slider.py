import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
image = cv2.imread('../data/constellations/orion.png')
img = image.copy()
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('H1','image',0,255,nothing)
cv2.createTrackbar('S1','image',0,255,nothing)
cv2.createTrackbar('V1','image',0,255,nothing)

cv2.createTrackbar('H2','image',0,255,nothing)
cv2.createTrackbar('S2','image',0,255,nothing)
cv2.createTrackbar('V2','image',0,255,nothing)


while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    h1 = cv2.getTrackbarPos('H1','image')
    s1 = cv2.getTrackbarPos('S1','image')
    v1 = cv2.getTrackbarPos('V1','image')
    h2 = cv2.getTrackbarPos('H2', 'image')
    s2 = cv2.getTrackbarPos('S2', 'image')
    v2 = cv2.getTrackbarPos('V2', 'image')

    img = image.copy()
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    # lower = np.array([11, 90, 44])
    lower = np.array([h1, s1, v1])
    upper = np.array([h2, s2, v2])
    mask = cv2.inRange(hsv, lower, upper)
    img = cv2.bitwise_and(img, img, mask=mask)

cv2.destroyAllWindows()