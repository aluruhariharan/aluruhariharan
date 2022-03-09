import cv2 as cv

capture = cv.VideoCapture(0)
#cv.imshow(capture)

#change res only work for live video

capture.set(3,320)
capture.set(4,240)

#frame capture

while capture.isOpened():
	isTrue,frame = capture.read()
	cv.imshow('Video',frame)
	if cv.waitKey(1) & 0xFF == ord('q') :
		break
capture.release()
cv.destroyAllWindows()
