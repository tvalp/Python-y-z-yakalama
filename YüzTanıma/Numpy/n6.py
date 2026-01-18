###Şimdi Biraz Kodları Kısaltalım###
import cv2
import numpy as np
###görüntüler###
res=cv2.imread("OpenCV/Nesneler/Kopek1.jpg",0)
res1=cv2.imread("OpenCV/Nesneler/Kopek1.jpg",0)
###Açma-Kapama-Tophat-Blackhat İşlemleri###
acma_islemi = cv2.morphologyEx(res,cv2.MORPH_OPEN,np.ones((9,9),np.uint8),iterations=1)
kapama_islemi=cv2.morphologyEx(res1,cv2.MORPH_CLOSE,np.ones((9,9),np.uint8),iterations=1)
top_hat=cv2.morphologyEx(res,cv2.MORPH_TOPHAT,np.ones((5,5),np.uint8),iterations=1)
black_hat=cv2.morphologyEx(res1,cv2.MORPH_BLACKHAT,np.ones((9,9),np.uint8),iterations=1)
###Sonuçları Göster###
cv2.imshow("Açma",acma_islemi)
cv2.imshow("Kapama",kapama_islemi)
cv2.imshow("Tophat",top_hat)
cv2.imshow("Blackhat",black_hat)
cv2.waitKey(0)