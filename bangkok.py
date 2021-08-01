import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
time.sleep(2)
bg = 0

while(True):
    ret, img = cap.read()
    if not ret:
        break
    img = np.flip(img, axis=1)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break


cap.release()
cv2.destroyAllWindows()