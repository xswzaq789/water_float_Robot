# 라이브러리 읽어오기 #
import servo_model
import tensorflow as tf
import cv2
import numpy as np
import model_import
import serial

# 시리얼 포트 연결 설정 #
com = serial.Serial(port="/dev/ttyUSB0",
baudrate= 9600,
bytesize = serail.EIGHTBITS,
parity = serial.PARITY_NONE,
timeout= 1)

# 픽셀변화 기준 정하기 #
thresh = 50
max_diff = 40


a,b,c  =None, None, None

cap = cv2.VideoCapture(0,cv2.CAP_V4L)

# cnn 모델 가져오기 #
model = model_import.model_processing()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,320)

if cap.isOpened():
	ret, a = cap.read()
	ret, b =cap.read()

	while ret:
		ret, c = cap.read()
		draw = c.copy()
		if not ret:
			break
			
		a_gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
		b_gray = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
		c_gray = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY)

		# 픽셀차이 찾아내기 #
		
		diff1 = cv2.absdiff(a_gray,b_gray)
		diff2 = cv2.absdiff(b_gray,c_gray)
		
		ret, diff1_t = cv2.threshold(diff1,thresh,255,cv2.THRESH_BINARY)
		ret, diff2_t = cv2.threshold(diff2, thresh, 255, cv2.THRESH_BINARY)

		diff = cv2.bitwise_and(diff1_t,diff2_t)

		k=cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
		diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)
		
		# 픽셀차이 결과값을 통해 사각형 그리기 #
		diff_cnt = cv2.countNonZero(diff)
		
		if diff_cnt > max_diff:
			nzero = np.nonzero(diff)
			cv2.rectangle(draw, (min(nzero[1]), min(nzero[0])),
			(max(nzero[1]), max(nzero[0])), (0,255,0),2)

		
			low = (min(nzero[1]), min(nzero[0]))
			high = (max(nzero[1]),max(nzero[0]))
		
			low_1 = min(nzero[1])
			low_2 = max(nzero[1])
			high_1 = min(nzero[0])
			high_2 = max(nzero[0])
			draw2 = np.hstack((draw,cv2.cvtColor(diff,cv2.COLOR_GRAY2BGR)))
			if(low_1 <low_2) & (high_1<high_2):
				if(high_1 >5):	
					high_1 = high_1 -5
				high_2 =high_2 + 5
				if(low_1 >5):
					low_1 = low_1 -5
				low_2 = low_2 +5
				
				#cnn 모델 돌릴 이미지 정하기
				garbage  = draw2[high_1:high_2, low_1:low_2]


				cv2.imshow("test1",garbage)
				
				# cnn 모델 결과값을 통해 serial 포트로 어떤 정보 보낼지 정하기  쓰레기: 1, 쓰레기 x : 0 #
				ret, print_a = model_import.predict_processing(model,garbage)
				
				# 아두이노에 정보 보내기 serial port를 통해 #
				
				if(ret ==1):
					serial.write(1.encode())
				else:
					serial.write(0.encode())

				cv2.putText(draw,print_a, (high_2,low_1),
				cv2.FONT_HERSHEY_DUPLEX,1.5,(0,0,255))
				mi_1 = (high_1 +high_2) /2
				mi_2 = (low_1 + low_2) / 2
				mi = (mi_1, mi_2)
				print(print_a)


		stacked = np.hstack((draw, cv2.cvtColor(diff,cv2.COLOR_GRAY2BGR)))
		stacked2 = draw
	
		a=b
		b=c

		if cv2.waitKey(32) >0:
			cv2.destroyAllWindows()
			break
