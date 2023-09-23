import cv2 as cv
from cvzone.SelfiSegmentationModule import SelfiSegmentation

# Load the two images you want to compare
path1 = "img/1a .jpg"
path2 = "img/1b.jpg"

img1 = cv.imread(path1)
img2 = cv.imread(path2)

# Initialize SelfiSegmentation to remove the background
seg = SelfiSegmentation()
img1 = seg.removeBG(img1)
img2 = seg.removeBG(img2)

# Resize the images for consistency


cv.imshow("IMG4", img1)
cv.imshow("IMG", img2)
cv.waitKey(0)
cv.destroyAllWindows()
print("done")
