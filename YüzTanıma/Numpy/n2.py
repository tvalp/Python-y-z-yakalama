###Kütüphaneyi dahil et###
import numpy as np
import cv2
###Aşındırma###
cekirdek = np.ones((5,5),np.uint8)
###Resmi Ekleyelim###
resim=cv2.imread("OpenCV/Nesneler/Kopek1.jpg")
###Aşındırmayı Gerçekleştirelim###
asindirma=cv2.erode(resim,cekirdek,iterations=1)
cv2.imshow("Aşındırılmış",asindirma)
cv2.waitKey(0)