import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier(r"C:\Users\Chandrakant\Desktop\OpenCV Application\Haarcascades\haarcascade_frontalface_default.xml")

img = cv2.imread(r"C:\Users\Chandrakant\Desktop\OpenCV Application\image_examples\Chandrakant_Thakur.jpg")
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale(img_gray,1.3,4)

if faces is ():
    print("No face found")

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("Face Detect",img)
    cv2.waitKey(0)

cv2.destroyAllWindows()