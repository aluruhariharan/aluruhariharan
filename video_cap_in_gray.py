import cv2 as cv

#cap = cv.VideoCapture('D:\\school stuff\\SECURED WIRELESS COMMUNICATION FOR INDUSTRIAL AUTOMATION AND CONTROL - YouTube.mp4')

cap = cv.VideoCapture(0)

#read frame by frame

while True:
	isTrue, frame = cap.read()

	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	cv.imshow('frame',gray)
	
	if cv.waitKey(1) & 0xFF == ord('q') :
		break
cap.release()
cv.destroyAllWindows()