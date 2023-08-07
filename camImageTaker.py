#captures images from the Webcam

import cv2

imgcapture= cv2.VideoCapture(0) #0 is cam id
result = True

while(result):
    ret, frame= imgcapture.read()
    cv2.imwrite("test.jpg", frame)
    result= False
    print("Image clicked!")

imgcapture.release()