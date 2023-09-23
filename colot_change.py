import cv2 as cv

path = "img/1b.jpg"

a = cv.imread(path)
a = cv.cvtColor(a, cv.COLOR_BGR2GRAY)

cv.imshow("aa0", a)
cv.waitKey(0)
cv.destroyAllWindows()
