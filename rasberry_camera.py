import tensorflow as tf
import keras.models 
import cv2
import os
import numpy as np 
from time import time

#이미지 모델받아오기
def model_setting():
    new_models = tf.keras.models.load_model("first.h5") # 0.26초 
    #new_models = tf.keras.models.load_model("second.h5") # 0.52초 
    
    return new_models

#이미지 전처리
def image_processing(img):
    list_a = []
  
    img =  cv2.resize(img, (100,100))
    img = cv2.cvtColor(img ,cv2.COLOR_BGR2RGB)
    list_a.append(img)
    list_a = np.array(list_a)
    list_a = list_a/255.0
    return img, list_a


cap = cv2.VideoCapture(0)

model = model_setting()

while True: 
    ret, frame = cap.read() 
    if ret ==0:
        break;
    img = cv2.imread(frame)
    img, img_list = image_processing(img)
    a = model.predict(img_list)
    if a<= 0.5:
        cv2.rectangle(img, (10,10), (90,90), (0,0,255),5)
        cv2.imshow("image",img)
        
    else:
        cv2.rectangle(img, (10,10), (90,90), (255,0,0),5)    
        cv2.imshow("image",img)
    
    if cv2.waitKey(32)== ord("q"):
        break;
