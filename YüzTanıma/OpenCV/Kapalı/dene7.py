###DERECEYE GÖRE DÖNDÜRME###
import cv2
resim = cv2.imread("Nesneler/Kopek2.jpg")
genislik= 600
yükseklik = 600
merkez_nokta=(genislik//2,yükseklik//2)
d = cv2.getRotationMatrix2D(merkez_nokta,10,1)
dondurme= cv2.warpAffine(resim,d,(genislik,yükseklik))
cv2.imshow("Dondurme",dondurme)
cv2.waitKey(0)
