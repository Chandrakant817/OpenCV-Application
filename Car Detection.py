import cv2
import numpy as np
import time

#Haarcascade Classifier Path
car_classifier = cv2.CascadeClassifier(r"C:\Users\Chandrakant\Desktop\OpenCV Application\Haarcascades\haarcascade_car.xml")

# Video Path
cap = cv2.VideoCapture(r"C:\Users\Chandrakant\Desktop\OpenCV Application\image_examples\cars.avi")

while cap.isOpened():
    ret,frame = cap.read()
    time.sleep(.05)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    car = car_classifier.detectMultiScale(gray,1.4,2)

    for (x,y,w,h) in car:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow("Car Window",frame)
    
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break

cap.release()
cv2.destroyAllWindows()