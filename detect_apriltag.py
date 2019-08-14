#!/usr/bin/env python3
# coding: utf-8

import apriltag
import cv2

#img = cv2.imread('tag-standard-41h12.png', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('tag-standard-41h12.png', cv2.IMREAD_GRAYSCALE)
options = apriltag.DetectorOptions(families='tagstandard41h12',
            border=1,
            nthreads=4,
            quad_decimate=1.0,
            quad_blur=0.0,
            refine_edges=True,
            refine_decode=False,
            refine_pose=False,
            debug=False,
            quad_contours=True)
detector = apriltag.Detector()

results = detector.detect(img)

print(results)
