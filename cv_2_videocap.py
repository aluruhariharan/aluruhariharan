import cv2 as cv

#cap = cv.VideoCapture('D:\\school stuff\\SECURED WIRELESS COMMUNICATION FOR INDUSTRIAL AUTOMATION AND CONTROL - YouTube.mp4')

cap = cv.VideoCapture(0)

#read frame by frame

while True:
	isTrue, frame = cap.read()
	cv.imshow('frame',frame)
	if cv.waitKey(1) & 0xFF == ord('q') :
		break
cap.release()
cv.destroyAllWindows()