import cv2 as cv

capture = cv.VideoCapture('D:\\school stuff\\SECURED WIRELESS COMMUNICATION FOR INDUSTRIAL AUTOMATION AND CONTROL - YouTube.mp4')

#video rescaling function

def rescaleFrame(frame, scale):
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)
	dimensions = (width,height)
	res = cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
	return cv.imshow('scaled',res)

#video capture

while capture.isOpened():

	ret, frap = capture.read()
	cv.imshow('normal',frap)
	rescaleFrame(frap,0.75)

	if cv.waitKey(25) & 0xFF == ord('q'):
		break

capture.release()
cv.destroyAllWindows()
