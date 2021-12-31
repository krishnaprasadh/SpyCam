import cv2
import uuid
import os
capture = cv2.VideoCapture(0)
filename = str(uuid.uuid4())
while True:
      ret, frame = capture.read()
      cv2.imwrite(filename+".jpg", frame)
      break
cv2.destroyAllWindows()
