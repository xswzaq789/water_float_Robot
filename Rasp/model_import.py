import tensorflow as tf
from time import time
import cv2
import numpy as np

def model_processing():
	model  = tf.keras.models.load_model("garabge_500.h5")
	return model

def predict_processing(model, frame):
	frame = cv2.resize(frame, (100,100))
	frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
	X= []
	ret = 0 
	X.append(frame)
	X = np.array(X)
	X = X/255.0
	list_a = model.predict(X)
	list_a  = list_a[0]
	p = max(list_a)
	if(p<0.2):
		ret = 0
		return 'nothing'
	list_a = list(list_a)
	p = list_a.index(p)
	list_b = ['cardboard', 'glass','metal','paper','plastic','trash','nothing']
	ret = 1
	return ret, list_b[p]

