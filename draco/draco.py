import argparse
import cv2

def main():
    ap = argparse.ArgumentParser(description='Detects and recognizes celestial bodies from images')
    ap.add_argument("-i", "--input", required=True, help="path to input image")

    args = vars(ap.parse_args())

    image = cv2.imread(args["input"])
    

if __name__ == "__main__":
    main()