###Kütüphaneyi ekledik###
import cv2
###Resmi Ekledik###
resim = cv2.imread("Nesneler/Kopek1.jpg")
###Resmi Kırpma İşlemi###
kirpma=resim[5:350,20:380]
resim = kirpma
###Resmin Boyutunu Ekledik###
boyut = cv2.resize(resim, (640,480))
###Resmi Gösterdik 1.parametre sekmenin ismi 2.si resim###
cv2.imshow("Kopek", boyut)
###Resmin Yükseklik Genişlik ve Kanal sayısını bulduk###
yukseklik, genislik, kanal_sayisi = resim.shape
###Bu Formatta yazdırdık###
print("Genişlik:{}\nYükseklik:{}\nKanal sayısı:{}".format(genislik, yukseklik, kanal_sayisi))
###OpenCv Kütüphanesinde renk rgb degil bgr olarak alınır###
mavi,yesil,kırmızı = boyut[10,30]
###Renk Yogunlugunu Bulduk###
print("Mavi renk yogunlugu:{}\nYeşil Renk Yogunlugu:{}\nKırmızı renk yogunlugu:{}".format(mavi,yesil,kırmızı))
###Kapanmaması için beklettik###
cv2.waitKey(0)