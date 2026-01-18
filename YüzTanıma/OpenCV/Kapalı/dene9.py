import cv2

resim=cv2.imread("Nesneler/Kopek1.jpg",0)
###Kenar Tespiti###
kenar=cv2.Canny(resim,100,500)
cv2.imshow("Kenarlı",kenar)
cv2.waitKey(0)