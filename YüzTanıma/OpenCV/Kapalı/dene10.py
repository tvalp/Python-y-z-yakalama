
###Kütüphaneyi Ekliyoruz###
import cv2
###Resmi Dahil et###
resim =cv2.imread("Nesneler/Kopek1.jpg")
###Filtreler##
bulanik=cv2.GaussianBlur(resim,(11,11),2)
medyan=cv2.medianBlur(resim,7)
bilateral=cv2.bilateralFilter(resim,15,93,93)
###Kaydetme Fonksiyonu###
def Kaydet(goruntu_matrisi):
    goruntu_matrisi=cv2.cvtColor(goruntu_matrisi,cv2.COLOR_BGR2GRAY)
    goruntu_matrisi=cv2.resize(goruntu_matrisi,(200,200))
    goruntu_matrisi=cv2.Canny(goruntu_matrisi,50,150)
    dosya=input("Dosya Adını Gir: ")
    dosya=dosya+".jpg"
    return cv2.imwrite(dosya,goruntu_matrisi)



cv2.imshow("Bulanık",bulanik)
cv2.imshow("MedianBlur",medyan)
cv2.imshow("Bilateral Bulanık azaltıcı",bilateral)
cv2.waitKey(0)
Kaydet(resim)