import cv2
import numpy

# Open the webcam (0 is the default camera ID; adjust if needed)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Webcam açılamadı!")
    exit()

while True:
    ret, goruntu = cap.read()
    if not ret:
        print("Görüntü alınamadı!")
        break
    
    # Convert to grayscale
    goruntu_gray = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian Blur
    bulanik = cv2.GaussianBlur(goruntu_gray, (5, 5), 0)
    
    # Detect edges using Canny
    kenar = cv2.Canny(bulanik, 40, 150)
    
    # Detect circles using HoughCircles
    daireler = cv2.HoughCircles(kenar, cv2.HOUGH_GRADIENT, dp=1, minDist=5, maxRadius=250)
    
    if daireler is not None:
        daireler = numpy.round(daireler[0]).astype(int)
        for (x, y, r) in daireler:
            # Draw detected circles
            cv2.circle(goruntu, (x, y), r, (0, 255, 0), 5)
            cv2.circle(goruntu, (x, y), 2, (0, 0, 255), 10)
    
    # Display the result
    cv2.imshow("Sonuc", goruntu)
    
    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()