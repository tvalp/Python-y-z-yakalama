import cv2

# Görüntüyü Oku
goruntu = cv2.imread("Nesneler/Kopek3.jpg")

# Görüntüyü Yeniden Boyutlandır
gor = cv2.resize(goruntu, (640, 380))

# Çizim Parametreleri
merkez = (150, 200)  # x, y
renk = (255, 0, 0)  # BGR formatında mavi
kalinlik = 10  # Çizginin kalınlığı
yaricap = 30  # Piksel yarıçapı

# Daire Çizme
cv2.circle(gor, merkez, yaricap, renk, kalinlik)

# Görüntüyü Göster
cv2.imshow("Goruntu", gor)

# Ekranı Beklet
cv2.waitKey(0)