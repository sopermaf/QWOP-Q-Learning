from PIL import ImageGrab
from PIL import ImageOps
import numpy as np
import os
from os import listdir
from os.path import isfile, join
import time
from time import sleep
import pyautogui
import cv2
import random

#----------------------------------------------GLOBALS---------------------------------------------------------------#
print("loading globals..")
path='/Users/tadhgriordan/Documents/interface/'  
path_main = path+'main/'
path_images_digits = path+'images/digits/'
path_images_control = path+'images/control/'


def load_images(path):    
    onlyfiles = [ f for f in listdir(path) if isfile(join(path,f)) ]
    images = np.empty(len(onlyfiles), dtype=object)
    for n in range(0, len(onlyfiles)):
      images[n] = cv2.imread( join(path,onlyfiles[n]) )
    return images
    
digits = load_images(path_images_digits)
controls = load_images(path_images_control)

#Distance screen at game start.
distance_coords = pyautogui.locateOnScreen(path_images_control+'start_distance.png') 
distance_x = distance_coords[0]
distance_y = distance_coords[1]
distance_w = distance_x+70
distance_h = distance_y+40

#restart screen at game end.
restart_image = cv2.cvtColor(controls[3], cv2.COLOR_BGR2GRAY) #for some reason 'images' is indexed starting from 1. '0' is a null image or something
start_coords = pyautogui.locateOnScreen(path_images_control+'click_to_begin.png')
restart_x = start_coords[0]+75
restart_y = start_coords[1]+125
restart_w = restart_x+240
restart_h = restart_x+60

#player coordinates during game running.
player_coords = pyautogui.locateOnScreen(path_images_control+'start_screen.png')
player_x = player_coords[0]
player_y = player_coords[1]+85  
player_w = player_x+600
player_h = player_y+315
print("Globals loaded.")
#----------------------------------------------GLOBALS---------------------------------------------------------------#