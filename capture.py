import cv2
import time
# # if you use video from webcam, you put 0.
# # if you capture video from a video clip, you put the name of the clip
# video = cv2.VideoCapture(0)
#
# # this is taking a video
# check, frame = video.read()
# print(check)
# # this prints the 3d array of the RGB values
# print(frame)
#
# # putting the script to sleep so it can take the video of 4 seconds
# time.sleep(4)
#
# #
# cv2.imshow("capturing",frame)
#
# cv2.waitKey(0)
# # this is like the dispose method
# video.release()
# cv2.destroyAllWindows()

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    print(check)
    print(frame)
    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()