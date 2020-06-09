import cv2
# this read the image, the second parameter can be 0 (gray), 1 (color), -1
galaxyImg = cv2.imread("galaxy.jpg", 1)

# resizing the image
resizedImg= cv2.resize(galaxyImg, (500,500))

# this shows the image.
cv2.imshow("galaxy", resizedImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

# writing the image to a file
cv2.imwrite("GalaxyResize.jpg", resizedImg)


print(galaxyImg)