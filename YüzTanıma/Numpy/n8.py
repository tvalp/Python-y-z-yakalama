import cv2

resim = cv2.imread("OpenCV/Nesneler/Kopek1.jpg")

def islem(event, x, y, flags, params):
    if event == cv2.EVENT_MOUSEMOVE:
        print("Ekranda Geziyorsun")
        print("Mausenin Konumu x: {} ve y: {}".format(x, y))
    elif flags == cv2.EVENT_FLAG_SHIFTKEY:  # Corrected
        print("Shift Dügmesine Basıyorsun")
    elif event == cv2.EVENT_LBUTTONDOWN:
        print("Sol Tuşa Basıldı")

if resim is not None:
    cv2.imshow("Goruntu", resim)
    cv2.setMouseCallback("Goruntu", islem)  # Corrected
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Resim dosyası bulunamadı! Lütfen dosya yolunu kontrol edin.")