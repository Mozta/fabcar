#import libraries of python opencv
import cv2
import numpy as np

#img = cv2.imread('car1.png')
img = cv2.imread('2.jpeg')
#use trained cars XML classifiers
car_cascade = cv2.CascadeClassifier('cars.xml')

#to get width & height
height, width, channels = img.shape
print("Alto: " + str(height))
print("Ancho: " + str(width))
area = img.size / 3
print("Size: " + str(area))

#convert video into gray scale of each frames
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect cars in the video
cars = car_cascade.detectMultiScale(gray, 1.1, 3)

#to draw arectangle in each cars 
for (x,y,w,h) in cars:
    pos_x = max(x - 10, 0)
    pos_y = max(y - 10, 0)
    
    height2 = (y+h)-y
    width2 = (x+w)-x
    print("Alto2: " + str(height2))
    print("Ancho2: " + str(width2))
    area2 = height2 * width2
    print("Area2: " + str(area2))
    porcentaje = (area2 * 100) / area
    print (porcentaje)
    if(porcentaje > 10):
        if(x < (width/2)):
            cajon = 1
        else:
            cajon = 2
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(img, "Carrito en cajon " + str(cajon)+ str(" : %2.2f" % porcentaje) + "%", (pos_x,pos_y), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,0),4,cv2.LINE_AA)
    
#display the resulting frame
small = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
cv2.imshow('image', small)
cv2.waitKey(0)
cv2.destroyAllWindows()#display the resulting frame

