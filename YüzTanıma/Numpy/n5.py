import numpy as np
import cv2 as cv
###Kapama Yapalım ###
cekirdek_asindirma=np.ones((7,7),np.uint8)
cekirdek_yayma=np.ones((9,9),np.uint8)
###Görüntüyü Okuyup gri formata çevirelim###
resim=cv.imread("OpenCV/Nesneler/Kopek1.jpg",0)
###Yayma Yapalım###
yayma=cv.dilate(resim,cekirdek_yayma,iterations=1)
###Asındırma###
son_hal=cv.erode(yayma,cekirdek_asindirma,iterations=1)
###Çıktı Alalım###
cv.imshow("Yayılmış",yayma)
cv.imshow("s",son_hal)
cv.waitKey(0)