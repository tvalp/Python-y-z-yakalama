###Kütüphaneleri dahil edelim###
import cv2
import numpy as np
###Yayıp Aşındıralım###
cekkirdek_asindirma=np.ones((7,7),np.uint8)
cekkirdek_yayma=np.ones((3,3),np.uint8)
###Okuyup Griye cevirelim###
resim=cv2.imread("OpenCV/Nesneler/Kopek1.jpg",0)
###Aşındırma###
asindirma=cv2.erode(resim,cekkirdek_asindirma,iterations=1)
son_hal=cv2.dilate(asindirma,cekkirdek_yayma,iterations=1)
cv2.imshow("Acma",son_hal)
cv2.waitKey(0)