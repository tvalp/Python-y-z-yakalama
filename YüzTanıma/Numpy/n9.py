import cv2
goruntu=cv2.imread("OpenCV/Nesneler/Kopek1.jpg",0)
###Kenar Algılama###
kenar=cv2.Canny(goruntu,30,150)
###Kontur Bulma###
contours,hiyerachy =cv2.findContours(kenar,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
###Görüntü Üzerinde Konturları Çizme###
cv2.drawContours(goruntu,contours,-1,(0,255,0),2)
cv2.imshow("Konturlar",kenar)
cv2.waitKey(0)
