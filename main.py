#numpy creates image arrays
import numpy as np

#PIL defines image size also grabs the image
from PIL import ImageGrab

#openCV displays image array from numpy as its own display window
import cv2

import pyautogui as gui
import os
import time

#directkeys just defines the keyboard inputs as direct x inputs so the game can read it
from directkeys import PressKey, ReleaseKey, UP, DOWN, LEFT, RIGHT, Z, X, I, P, LBRACKET

#grey scales given image/numpy array
def proccess_img(original_img):
    proccessed_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    proccessed_img = cv2.Canny(proccessed_img, threshold1=200, threshold2=300)
    return proccessed_img

for i in list(range(4))[::-1]:
    print(i+1)
   # time.sleep(1)

while(True):
    #grabs display withins the pixals given
    #bbox dedines what to display
    screen =  np.array(ImageGrab.grab(bbox=(25,45,605,568)))

    #does the same but puts it to function to grey scale
    new_screen = proccess_img(screen)

    # PressKey(RIGHT)
    # PressKey(X)
    # time.sleep(0.5)
    # ReleaseKey(X)
    # ReleaseKey(RIGHT)

    #imshow displays the window it is capturing
    cv2.imshow('window', cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2RGB))
    #cv2.imshow('test', new_screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break