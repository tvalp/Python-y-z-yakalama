###Resmi Griye Çevirme###
import cv2
goruntu = cv2.imread("Nesneler/Kopek3.jpg")

gor = cv2.resize(goruntu, (640,380))

gri=cv2.cvtColor(gor,cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(gor,cv2.COLOR_BGR2RGB)
cv2.imshow("Orjinal",gor)
cv2.imshow("Gri",gri)
cv2.imshow("Rgb",rgb)
cv2.waitKey(0)