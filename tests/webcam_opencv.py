import cv2
import time

cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FPS, 24) # Частота кадров
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600) # Ширина кадров в видеопотоке.
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # Высота кадров в видеопотоке.

#cam raw start
for i in range(10):
    cap.read()

#take pic
return_value, image = cap.read()

#write to file
if return_value:
    cv2.imwrite('cam0.png', image)
    cv2.imshow("cam0", image)

    #поприкалываемся?
    cv2.imshow('Color blue', image[:, :, 0])
    cv2.imshow('Color green', image[:, :, 1])
    cv2.imshow('Color red', image[:, :, 2])

    time.sleep(1)
    cv2.waitKey(0)
    cv2.destroyWindow("cam0")
    cv2.destroyWindow("Color blue")
    cv2.destroyWindow("Color green")
    cv2.destroyWindow("Color red")
else:
    print('err')

#off cam
cap.release()