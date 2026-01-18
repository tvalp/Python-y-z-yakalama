###Diktörtken içine alma###
import cv2
goruntu = cv2.imread("Nesneler/Kopek3.jpg")

gor = cv2.resize(goruntu, (640,380))

p1=(150,200)
p2=(300,400)
renk=(0,255,0)
kalinlik=5

cv2.rectangle(gor,p1,p2,renk,kalinlik)

cv2.imshow("Dene4", gor)
cv2.waitKey(0)