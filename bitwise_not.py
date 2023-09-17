import cv2 as cv
path = "img/A.jpeg"
img = cv.imread(path)
img = cv.bitwise_not(img)
img = cv.resize(img, (0, 0), fx=.5, fy=.5)
cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()
