import cv2
import pandas
from datetime import datetime

# this is the first frame
first_frame = None
# stores the status of the motion
status_list = [None, None]
# stores the time when the state of the status changes
times = []
# creating data frames
df = pandas.DataFrame(columns=["Start", "End"])

# video capture from the webcam
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    # no motion in current frame
    status = 0

    # converts the RGB image to gray image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # reduces noise
    gray = cv2.GaussianBlur(gray, (7,7), 0)

    # gets the first frame of the video
    if first_frame is None:
        first_frame = gray
        continue
    # gets the difference between the two frames
    delta_frame = cv2.absdiff(first_frame, gray)

    # sets the threshold. If the delta value of a pixel is over 30, it's white (255)
    # and if less than 30, it's black.
    threshold_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    # cleans the image
    threshold_frame = cv2.dilate(threshold_frame, None, iterations = 2)

    # ges the contours in form of tuples
    (cnts,_) = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        # if contour area is less than a thousand ignore it
        if cv2.contourArea(contour) < 6000:

            continue
        # motion detected in video
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

    # you add the state of the status of the video to the status list
    status_list.append(status)
    # you record the time of the status change
    if status_list[-1] == 1 and status_list [-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())


    # cv2.imshow("first", first_frame)
    cv2.imshow("delta", delta_frame)
    # cv2.imshow("others", gray)
    cv2.imshow("threshold", threshold_frame)
    cv2.imshow("color frame", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        if status ==1:
            times.append(datetime.now())
        break

print(status_list)
print(times)

for i in range (0, len(times), 2):
    df = df.append({"Start": times[i], "End": times[i+1]},ignore_index = True)
df.to_csv("Times.csv")
video.release()
cv2.destroyAllWindows()