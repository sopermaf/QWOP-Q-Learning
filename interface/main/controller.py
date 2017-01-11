from PIL import ImageGrab
from PIL import ImageOps
from numpy import *
import os
import time
import pyautogui

# Globals
# ------------------

#need: mouseClick, spacebar, Q, W, O, P

def start():
    pyautogui.click()
    pyautogui.click() #clicks out of terminal window onto game
    
    while(True): 
        '''*keypress commands.
        keypress("q","down")
        keypress("w","down")
        keypress("o","down")
        keypress("p","down")
        keypress("q","up")
        keypress("w","up")
        keypress("o","up")
        keypress("p","up")
        sleep(x)
        '''
        
def keypress(char, action):
    if(action is "down"): pyautogui.keyDown(char)
    if(action is "up"): pyautogui.keyUp(char)

def end():
    pyautogui.press(' ')  
    
def main():
    start()
 
if __name__ == '__main__':
    main()

