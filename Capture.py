import cv2.cv as cv
import uuid
import os
capture = cv.CaptureFromCAM(0)
filename = str(uuid.uuid4())
while True:
      img = cv.QueryFrame(capture)
      cv.SaveImage(filename+".jpg", img)
      break
cv.DestroyAllWindows()
