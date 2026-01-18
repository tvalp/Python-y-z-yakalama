###Kütüphaneleri dahil et###
import numpy as np
import cv2
###Yayma için matris###
cekirdek = np.ones((9,9),np.uint8)
###Görüntüyü Okuyup Gri yapalım###
resim=cv2.imread("OpenCV/Nesneler/Kopek1.jpg",0)
###Yayma işlemini Yapak###
son_hal=cv2.dilate(resim,cekirdek,iterations=3)
###Çıktımızı Alalım###
cv2.imshow("Yayma",son_hal)
cv2.waitKey(0)