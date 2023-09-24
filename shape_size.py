import cv2 as cv

path = "img/1b.jpg"

print()
img = cv.imread(path)
# height and weight
print("Shape h/w = ", img.shape, "\nSize = ", img.size)

cv.imshow("Img", img)
cv.waitKey(0)
cv.destroyAllWindows()
