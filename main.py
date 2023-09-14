import cv2 as c

path = "img/A.jpeg"
img = c.imread(path)
print(img, "\n")
c.imshow("Image", img)
c.waitKey(0)
c.destroyAllWindows()
print("done")
