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
import threading
from operator import itemgetter

#----------------------------------------------GLOBALS---------------------------------------------------------------#
print("loading globals..")  
dir = os.path.dirname(__file__)
path_images_digits = dir+'/images/digits/'
path_images_control = dir+'/images/control/'
alphabet = ["", "p", "o", "op", "w", "wp", "wo", "wop", "q", "qp", "qo", "qop", "qw", "qwp", "qwo", "qwop"]
alphabet_string = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]
MAX_INITIAL_RUNNERS = 5000
MIN_NUM_GENES = 8
MAX_NUM_GENES = 24
NUM_TYPES_GENES = 16

cap = cv2.VideoCapture(3)

def get_rand_bool():
    return bool(random.getrandbits(1))
    
lock = threading.Lock()
last_frame = ''
def get_frame():
    lock.acquire()
    ret, frame = cap.read()
    lock.release()
    return frame
    
def get_coords(image,threshold):   
    ret, frame = cap.read()     
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) 
    result = cv2.matchTemplate(frame,image,cv2.TM_CCOEFF_NORMED)
    match_indices = np.arange(result.size)[(result>threshold).flatten()]      
    coords = np.unravel_index(match_indices,result.shape) #coordinate of match(s)
    if(len(coords[1])>0):        
        return [coords[1][0],coords[0][0]]
    else: return None
       
def load_images(path):    
    onlyfiles = [ f for f in listdir(path) if isfile(join(path,f)) ]
    images = np.empty(len(onlyfiles), dtype=object)
    for n in range(0, len(onlyfiles)):
      images[n] = cv2.imread( join(path,onlyfiles[n]) )
    return images
    
digits = load_images(path_images_digits)
controls = load_images(path_images_control)
digits = digits[1:]
controls = controls[1:]

#restart screen at game end.
def check_for_restart_image():
    restart_image = controls[2]
    restart_coords = get_coords(restart_image,0.8)
    if(restart_coords==None): return False
    else: return True

#Distance screen at game start.
start_distance_image = controls[3]
distance_height, distance_width, distance_channels = start_distance_image.shape 
distance_coords = get_coords(start_distance_image,0.9) 
distance_x = distance_coords[0]-5
distance_y = distance_coords[1]
distance_w = distance_width+(distance_width/5)
distance_h = distance_height+(distance_height/5)
print("distance: " + str(distance_x) + " " + str(distance_y) + " " + str(distance_w) + " " + str(distance_h))


#player coordinates during game running.
start_screen_image = controls[4]
start_height, start_width, start_channels = start_screen_image.shape 
start_screen_coords = get_coords(start_screen_image, 0.9)
player_x = start_screen_coords[0]
player_y = start_screen_coords[1]+45
player_w = start_width
player_h = start_height-45
print("Globals loaded.")

#----------------------------------------------GLOBALS---------------------------------------------------------------#