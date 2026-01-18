###video üzerinden tespit###
import cv2
###Videoyu tanımladıgın yer###
video = cv2.VideoCapture("Video.mp4")
while True:
    ###Videoyu degişkene atıyoruz###
    kontrol, yakala=video.read()
    ###Okunmamasını Kontrol edelim###
    if kontrol==False:
        print("Okuma Başarısız")
        break
    ###Ekranda oynatalım###
    cv2.imshow("Video",yakala)
    ###Kapatma tuşu ayarlayalım ben esc yapacam###
    if cv2.waitKey(20)==27:
        break


    ###Burada Video üzerinde tanıma ya başlayacaz ###