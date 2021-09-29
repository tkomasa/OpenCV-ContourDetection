import numpy as np
import cv2

cap = cv2.VideoCapture('video_test\\205_78.247_Tr_cookies_-_Cookie_Clicker_2021-09-27_23-40-16.mp4')

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_color = np.array([110, 60, 62])
    upper_color = np.array([121, 37, 38])

    mask = cv2.inRange(hsv, lower_color, upper_color)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()