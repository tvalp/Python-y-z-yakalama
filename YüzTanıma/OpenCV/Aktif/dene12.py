### Modülü içe aktar ###
import cv2

### Webcam tanımla ###
webcam = cv2.VideoCapture(0)  # Eğer 1 çalışmazsa, 0'ı deneyin

### Pencere genişlik yükseklik ayarı ###
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

### Degerleri çıktı alalım ###
print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(webcam.get(cv2.CAP_PROP_FRAME_WIDTH)))
print("CV_CAP_PROP_FRAME_HEIGHT: '{}'".format(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT)))

### Kamerayı Okuyup değişkene atalım ###
while True:
    kontrol, yakala = webcam.read()
    if kontrol:
        ### Görüntüyü göster ###
        cv2.imshow("webcam", yakala)
    else:
        print("Okuma Başarısız")
        break
    
    ### Çıkış için 'q' tuşuna bas ###
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

### Kaynakları serbest bırakma ###
webcam.release()
cv2.destroyAllWindows()