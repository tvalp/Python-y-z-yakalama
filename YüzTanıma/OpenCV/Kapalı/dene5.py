###Resmin üstüne yazı Ekleme###
import cv2
resim =cv2.imread("Nesneler/Kopek3.jpg")
renk =(255,0,0)
gor = cv2.resize(resim,(640,380))
cv2.putText(gor,"Kopek",(50,100),cv2.FONT_ITALIC,3,renk,5)
cv2.imshow("Köpek",gor)
kopya = gor.copy()
cv2.imshow("Kopya",kopya)
cv2.waitKey(0)