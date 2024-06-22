import cv2
import numpy as np

full_body = cv2.CascadeClassifier(r"C:\Users\Chandrakant\Desktop\OpenCV Application\Haarcascades\haarcascade_fullbody.xml")

cap = cv2.VideoCapture(r"C:\Users\Chandrakant\Desktop\OpenCV Application\image_examples\walking.avi")

while cap.isOpened():
    ret,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    bodies = full_body.detectMultiScale(gray,1.2,3)

    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow("Full Body",frame)
    
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break

cap.release()
cv2.destroyAllWindows()