#!/bin/python

import numpy, cv2, time

cap = cv2.VideoCapture(0)

frames = []

#Images to keep in buffer.
#Program reads the oldest item from the buffer and diffs it from the current frame, so modifying this
#adjusts the delay on the ghost effect
for i in range(1,60):
	frames.append(cap.read()[1])

while(True):
	ret, frame = cap.read()

	#Cool thing. Sort of like a poor man's edge detect but not really.
	frames.append(frame)
	mask = cv2.subtract(frame, frames.pop(0))

	mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
	#unexpected behavior when the coefficient is changed to anything below 1.
	mask = mask*1 
	#print(mask)

	cv2.imshow('thiscanbeliterallyanything', mask)
	key = cv2.waitKey(1) & 0xFF
	if key == ord('q'):
		break
	elif key == ord('s'):
		cv2.imwrite("{0}.png".format(time.ctime()).replace(' ','-'), mask)
		print("Image written")

cap.release()
cv2.destroyAllWindows()
