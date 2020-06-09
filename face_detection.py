import cv2

# reading the haarcascade (xml telling features of a face)
# you can use this to search for face
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

test_Image = cv2.imread("news.jpg")
# this gets the gray image of the image
gray_Test_Image = cv2.cvtColor(test_Image, cv2.COLOR_BGR2GRAY)

# this detects the face. first paramenter is the image input, the higher the second parmeter, the higher tthe chance of missing the image
# for the third parmeter, the higher the number, the higher the chance of not detecting a face, an the lower the number, the higher the chance
# false positive
faces = face_cascade.detectMultiScale(test_Image, scaleFactor= 1.01, minNeighbors= 10)

# this is drawing triangles around the face
for x, y, w , h in faces:
    # first para = image, second para = op left corner, third para = bottom right corner, fourth para = width of a pixel
    img= cv2.rectangle(test_Image, (x,y), (x+w, y+h), (0, 255, 0), 3)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()