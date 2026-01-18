import cv2

# Haar-cascade dosyasını yükleyin
yuz_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Kamerayı başlat
webca = cv2.VideoCapture(0)
if not webca.isOpened():
    print("Kamera Algılanmadı")
    exit()

while True:
    # Kameradan görüntü al
    ret, frame = webca.read()
    if not ret:
        print("Görüntü alınamadı")
        break

    # Görüntüyü griye çevir
    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri tespit et
    yuzler = yuz_cascade.detectMultiScale(gri, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Tespit edilen yüzlerin etrafına dikdörtgen çiz ve üzerine 'İnsan' yaz
    for (x, y, w, h) in yuzler:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, 'Insan', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    # Görüntüyü göster
    cv2.imshow('Yuz Tanıma', frame)

    # 'q' tuşuna basarak çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Her şeyi serbest bırak
webca.release()
cv2.destroyAllWindows()