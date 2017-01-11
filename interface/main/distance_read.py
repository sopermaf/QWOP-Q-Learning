from PIL import ImageGrab
import numpy as np
import cv2
from os import listdir
from os.path import isfile, join

#CHANGE THE FOLLOWING TO SUIT YOUR SYSTEM
mypath='/Users/tadhgriordan/Documents/interface/images/' # 
x = 535
y = 239
w = 618
h = 265 #bbox specifies specific region (bbox= x,y,width,height)

def load_digits():
    
    onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
    images = np.empty(len(onlyfiles), dtype=object)
    for n in range(0, len(onlyfiles)):
      images[n] = cv2.imread( join(mypath,onlyfiles[n]) )
    return images

def replace(output):
    #get index of first value after "-" (if present) and last value before dot (if present) - delete everything in between.
    fst = 1 if "-" in output else 0
    lst = len(output)-1 if not("." in output) else output.index(".")-1   
    if(fst==lst): return output
    else: return output[0:fst+1] + output[lst:]

def format_output(total_coords, last_output):    
    total_coords.sort(key=lambda x: x[0]) #sort coordinates by x value
    output = ""
    for coord in total_coords:
        if(coord[1]==10): 
            if("." not in output): output += "."   #if coord is '.' and not in output, append   
        elif(coord[1]==11): 
            if("-" not in output): output += "-" #if coord is '-' and not in output, append   
        elif(("." not in output) or ("." in output and output.index(".") is len(output)-1)): output += str(coord[1])
    
    output = replace(fst, lst, output) 
    if((last_output == "3.9" or last_output == "4" or last_output == "4.1") and output == "44"): output = "4" #special case.    
    return output
    
images = load_digits()
last_output = ""
output = ""

while(True):
    img = ImageGrab.grab(bbox=(x,y,w,h)) #bbox specifies specific region (bbox= x,y,width,height)
    img_np = np.array(img)

    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    threshold = 0.884
    total_coords = []
    for count, image in enumerate(images):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(frame,image,cv2.TM_CCOEFF_NORMED)       
        match_indices = np.arange(result.size)[(result>threshold).flatten()]      
        coords = np.unravel_index(match_indices,result.shape) #coordinate of match(s)

        if len(coords[1])>0: #only coords[1] matters. its of size 2, 0 has y value and 1 has x i think. if match(s) found:
            for np_coord in coords[1]:
                total_coords.append([np_coord, count]) # add coordinate and digit to total coordinates
    
    output = format_output(total_coords, last_output)  
    print("output: " + output)
    last_output = output
             
    #cv2.imshow("PyQwopper", frame)
    #cv2.waitKey(1)
cv2.destroyAllWindows()

#co-ordinates for full box: (317,253,960,650)
#co-ordinates for distance only: (535,239,608,265)



