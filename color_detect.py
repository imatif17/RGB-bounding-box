import numpy as np
import cv2

lower_green = np.array([30, 80, 30])
upper_green = np.array([90, 255,255])
lower_blue = np.array([90,50,100])
upper_blue = np.array([120,255,255])
lower_red = np.array([170,87,111])
upper_red = np.array([180, 255, 255])

colors = np.array([[lower_red,upper_red],[lower_green,upper_green],[lower_blue,upper_blue]])
color_name = ['red','green','blue']

while (True):
	print("Choose the color :\n\t1 - Red\n\t2 - Green\n\t3 - Blue")
	c = int(input())
	if c not in [1,2,3]:
		print("Wrong input try again")
		continue
	break

cam = cv2.VideoCapture(0)
while(True):
	ret,frame = cam.read()
	if(ret):
		frame = cv2.flip(frame,1)
		hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		hsv = cv2.dilate(hsv,np.ones((7,7)))
		mask = cv2.inRange(hsv,colors[c-1][0],colors[c-1][1])
		contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		
		largest_contour = max(contours, key = cv2.contourArea)
		

		x,y,w,h = cv2.boundingRect(largest_contour)
		frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),3)
		frame = cv2.drawContours(frame, largest_contour, -1, (255,255,0), 3)

		cv2.imshow(color_name[c-1]+' colour detection',frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break
        
cam.release()
cv2.destroyAllWindows()
