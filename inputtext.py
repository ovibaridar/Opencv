import cv2 as cv

# cv.putText(img,text,coordinate,font,font_size,color,thickness)
path = "img/A.jpeg"
path2 = "img/p1.jpg"

a = cv.imread(path)
b = input("Enter a Text ")

font = cv.FONT_ITALIC
Height = a.shape[0]-200
print("Height", Height)
weight = a.shape[1]-200
print("Weight", weight)
# cv.putText(img,text,coordinate,font,font_size,color,thickness)
a = cv.putText(a,b, (weight, Height), font, 1, (0, 255, 255), 2)

cv.imshow("aa0", a)
cv.waitKey(0)
cv.destroyAllWindows()
