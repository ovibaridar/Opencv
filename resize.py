import cv2 as cv

path = "img/A.jpeg"
img = cv.imread(path)

img3 = cv.resize(img, (300, 300))
img2 = cv.resize(img, (0, 0), fx=0.5, fy=0.5)

cv.imshow("Image", img2)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow("Image", img3)
cv.waitKey(0)
cv.destroyAllWindows()
