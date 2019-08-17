import cv2
import numpy as np

original = cv2.imread("1.png")
file = open("molecule_names","r")
for line in file:
    image_to_compare = cv2.imread(line[:-1]+".jpg")

    if original.shape == image_to_compare.shape:
        print("The images have same size and channels")
        difference = cv2.subtract(original, image_to_compare)
        b, g, r = cv2.split(difference)

        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("The images are completely Equal")
        else:
            print("The images are NOT equal")

    sift = cv2.xfeatures2d.SIFT_create()
    kp_1, desc_1 = sift.detectAndCompute(original, None)
    kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)

    index_params = dict(algorithm=0, trees=5)
    search_params = dict()
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(desc_1, desc_2, k=2)

    good_points = []
    for m, n in matches:
        if m.distance < 0.6*n.distance:
            good_points.append(m)

    number_keypoints = 0
    if len(kp_1) <= len(kp_2):
        number_keypoints = len(kp_1)
    else:
        number_keypoints = len(kp_2)
    
    if(len(good_points)>300):
        print("File Name:"+line)
        print("GOOD Matches:", len(good_points))
        print("How good it's the match: ", len(good_points) / number_keypoints * 100)

    result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)


    cv2.destroyAllWindows()
