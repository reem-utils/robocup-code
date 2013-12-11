#! /usr/bin/env python
import cv2
import math
#http://www.steinm.com/blog/motion-detection-webcam-python-opencv-differential-images/


def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)

cam = cv2.VideoCapture(0)

winName = "Movement Detector"
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)

# Read three images first:

t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
diff = t_plus

while True:

    gravityCenter = cv2.moments(diff)
    gravityCenterXa = gravityCenter["m10"] / gravityCenter["m00"]
    gravityCenterYa = gravityCenter["m01"] / gravityCenter["m00"]

    key = cv2.waitKey(100)  # Wait 10 Milisseconds

    diff = diffImg(t_minus, t, t_plus)  # Calcule the difference between images
    cv2.imshow(winName, diff)  # Show image - Util to debug

    gravityCenter = cv2.moments(diff)
    gravityCenterXb = gravityCenter["m10"] / gravityCenter["m00"]
    gravityCenterYb = gravityCenter["m01"] / gravityCenter["m00"]

    print "Gravity Center a[%.3d, %.3d]" % (gravityCenterXa, gravityCenterYa)
    print "Gravity Center b[%.3d, %.3d]" % (gravityCenterXb, gravityCenterYb)
    print "Distance %d \n" % math.sqrt((gravityCenterXb - gravityCenterXa) ** 2 + (gravityCenterYb - gravityCenterYa) ** 2)

    # Read next image
    t_minus = t
    t = t_plus
    t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    #t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_GRAY2BGR)

    if key == 27:
        cv2.destroyWindow(winName)
        break

print "Goodbye"
