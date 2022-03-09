import cv2 as cv
import numpy as np

img = cv.imread('c:\\users\\harry\\pictures\\sds.jpg')
cv.imshow('my',img)

#one way of doing it or

'''
res = cv.resize(img,None,fx=0.25,fy=0.25, interpolation = cv.INTER_LINEAR)

cv.imshow('scaled',res)
'''
#other way of doing it:
def resizeFrame(frame, scale = 0.35):
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)
	
	dimensions = (width,height)
    
	res = cv.resize(frame,dimensions,interpolation=cv.INTER_CUBIC)
	return cv.imshow('scaled',res)

resizeFrame(img)

if cv.waitKey(0) & 0xFF == ord('q') :
	cv.destroyAllWindows()