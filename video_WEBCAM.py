import cv2 as cv

capture = cv.VideoCapture(0)
#cv.imshow(capture)
while True:
	isTrue, frame = capture.read()
	cv.imshow('Video',frame)
	if cv.waitKey(1) & 0xFF == ord('q') :
		break
capture.release()
cv.destroyAllWindows()
