import cv2 as cv

path = "img/A.jpeg"
img = cv.imread(path)

#img = cv.rotate(img, cv.ROTATE_180)
#img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
img = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)

cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()
