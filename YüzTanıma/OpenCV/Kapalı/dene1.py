###Modülü Tanımla###
import cv2
###Görüntüyü Oku###
goruntu = cv2.imread("Nesneler/Kopek2.jpg")
###Fonksiyon Parametlerini tanımla###
p1=(150,200)
p2=(300,400)
renk=(255,0,0)
kalinlik=10
gor = cv2.resize(goruntu, (600, 380))
###Line Fonksiyonunu Çagıralım###
cv2.line(gor,p1,p2,renk,kalinlik)
###Çıktıyı Alalım###
cv2.imshow("Goruntu",gor)
###Başladıktan sonra kapanmasın diye Bekletek###
cv2.waitKey(0)