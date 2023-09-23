import cv2 as cv

path = "img/A.jpeg"

a = cv.imread(path)

Height = a.shape[0]
print("Height", Height)
weight = a.shape[1]
print("Weight", weight)
# a = cv.line(a, (weight, Height), (weight, Height), (color), thickness)
a = cv.line(a, (0, 0), (800, 600), (0, 255, 255), 10)
a = cv.line(a, (0, Height), (800, 600), (0, 255, 255), 10)

cv.imshow("aa0", a)
cv.waitKey(0)
cv.destroyAllWindows()
