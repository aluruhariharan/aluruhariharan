import cv2 as cv

capture = cv.VideoCapture('D:\\school stuff\\SECURED WIRELESS COMMUNICATION FOR INDUSTRIAL AUTOMATION AND CONTROL - YouTube.mp4')

#video rescaling function
'''
def rescaleFrame(frame, scale=1):
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)
	dimensions = (width,height)
	res = cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
	return cv.imshow('scaled',res)
'''
#video capture

while capture.isOpened():
	frap = capture.read()
	scale = 0.95
	width = int(frap.shape[1] * scale)
	height = int(frap.shape[0] * scale)
	dimensions = (width,height)
	res = cv.resize(frap,None, dimensions, interpolation = cv.INTER_AREA)
	
	cv.imshow('scaled',res)	

	if cv.waitKey(20) & 0xFF == ord('q'):
		break

capture.release()
cv.destroyAllWindows()

	#rescaleFrame(frap)


#one way of doing it or
