import cv2

image = cv2.imread('shark.jpeg')

image = cv2.resize(image, (5000,5000))

grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grey_bgr = cv2.cvtColor(grey_image, cv2.COLOR_GRAY2BGR)

HSV_image = cv2.cvtColor(grey_bgr, cv2.COLOR_BGR2HSV)



cv2.imshow('Grayscale', grey_image)
cv2.imshow('HSV', HSV_image)

cv2.waitKey(0)
cv2.destroyAllWindows()