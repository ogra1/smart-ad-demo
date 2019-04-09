#!/usr/bin/env python2.7

import cv2
import os

snap = os.environ["SNAP"]

face_cascade = cv2.CascadeClassifier(snap + '/usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier(snap + '/usr/share/OpenCV/haarcascades/haarcascade_eye.xml')

def detect(gray, frame):
  """ Input = greyscale image or frame from video stream
      Output = Image with rectangle box in the face
  """
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)

  for (x,y,w,h) in faces:
    cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]

    eyes = eyes_cascade.detectMultiScale(roi_gray, 1.1, 3)

    for (ex, ey, ew, eh) in eyes:
      cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 2)

  return frame

video_capture = cv2.VideoCapture(0)
while True:
  ret, frame = video_capture.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  canvas = detect(gray, frame)
  cv2.imshow("Video", canvas)
  # cv2.imshow("Video", gray)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

video_capture.release()
cv2.destroyAllWindows()
