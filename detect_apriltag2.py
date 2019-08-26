#!/usr/bin/env python3
# coding: utf-8

# 这个 apriltag 是第二版，项目来自https://pypi.org/project/apriltag/
# 源码在这里，https://github.com/swatbotics/apriltag，并不是 Michagen 大学
# AprilRobotics 做的，是一个私人的 仓库
import apriltag
import cv2

def start():
    #img = cv2.imread('tag-standard-41h12.png', cv2.IMREAD_GRAYSCALE)
    img_dir = input('input image dir: ')
    img_name = input('input the image name: ')
    img = cv2.imread(img_dir + '/' + img_name, cv2.IMREAD_GRAYSCALE)
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
    if len(results) > 0:
        print(results[0].tag_family)
        print(results[0].center)
    print('number of detections: ', len(results))

if '__main__' == __name__:
    start()
