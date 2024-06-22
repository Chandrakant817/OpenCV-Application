import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier(r"C:\Users\Chandrakant\Desktop\OpenCV Application\Haarcascades\haarcascade_frontalface_default.xml")

cap= cv2.VideoCapture(0)
cap.set(3,640) #Width
cap.set(4,480) #Height

while True:
    ret, frame = cap.read()

    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(img_gray,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow("Face Detect",frame)
        cv2.waitKey(0)
        
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break
    
cv2.destroyAllWindows()