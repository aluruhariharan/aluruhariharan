import cv2 as cv
''''
#read images
img =cv.imread('c:\\users\\harry\\pictures\\sds.jpg')
cv.imshow('me',img)
'''
#rescale_fun

def scaled(frame, scale=0.75):
	width= int(frame.shape[1] * scale)
	height=int(frame.shape[0] * scale)
	dimensions= (width,height)
	return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

#read videos
capture = cv.VideoCapture('C:\\Users\\harry\\Pictures\\passwordbypass.mkv')
	
while True:
	isTrue, frame = capture.read()
	frame_scaled = scaled(frame)
	cv.imshow('Video',frame)
	cv.imshow('scaled',frame_scaled)
capture.release()
cv.DestroyallWindows()
#cv.waitKey()