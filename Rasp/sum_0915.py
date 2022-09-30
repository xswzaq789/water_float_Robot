import tensorflow
import serial
import string
import RPi.GPIO as GPIO
from time import sleep, time
import model as md
import servo_motor
import led_control as led
import server2 as db
import cv2
import numpy as np





#pixel difference settings
threshold = 50
max_diff = 100

# frames settings
a, b, c= None, None, None

# model settings
model = md.import_model()
state = 1

metal = 0
trash = 0
plastic = 0
unknown = 0

# starting point
while (1):
	#camera settings
	cap= cv2.VideoCapture(0)
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

	ret, a = cap.read()
	ret , b = cap.read()

	if ret ==0:
		print("camera_problem")
		break
	ret, c = cap.read()

	a_gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
	b_gray = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
	c_gray  = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY)

	# Arduino wave settings




	diff1 = cv2.absdiff(a_gray, b_gray)
	diff2 = cv2.absdiff(b_gray, c_gray)

	ret, diff1_t = cv2.threshold(diff1, threshold, 255, cv2.THRESH_BINARY)
	ret, diff2_t = cv2.threshold(diff2, threshold, 255, cv2.THRESH_BINARY)

	diff = cv2.bitwise_and(diff1_t, diff2_t)


	k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
	diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN,k )

	#led all release
	led.all_off()

	diff_cnt = cv2.countNonZero(diff)

	if diff_cnt > max_diff:
		nzero = np.nonzero(diff)
		low_1 = min(nzero[1])
		low_2 = max(nzero[1])
		high_1 = min(nzero[0])
		high_2  = max(nzero[0])
		draw2 = cv2.cvtColor(diff.cv2COLOR_GRAY2BGR)
		img = None

		if(low_1<low_2) & (high_1 < high_2):
			img = draw2[high_1:high_2, low_1:low_2]
			classes = md.predict_model(img,model)
			# metal, plastic, trash, unknown
			servo_motor.pork_up()
			

			if(classes == 0): #metal

				led.red_on()
				servo_motor.servo_decision(0,state) #90 degree
				state = 0
				time.sleep(5)
				metal = metal +1
				db.add_data(metal,plastic,trash, unknown)

					
			elif classes ==1:
				led.blue_on()
				servo_motor.servo_decision(1,state)
				state = 1
				time.sleep(5)
				plastic = plastic +1
				db.add_data(metal,plastic, trash, unknown)


			elif classes ==2:
				led.green_on()
				servo_motor.servo_decision(2,state)
				state = 2
				time.sleep(5)
				trash = trash +1
				db.add_data(metal,plastic,trash,unknown)
					
			else:
				led.white_on()
				servo_motor.servo_decision(3,state)
				state = 3
				time.sleep(5)
				unknown = unknown + 1
				db.add_data(metal,plastic,trash,unknown)

			servo_motor.pork_down()

	a = b
	b = c
