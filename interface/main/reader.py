from dependancies import *

class Reader(object):
      distance_last_output = 0
      
      def __init__(self):
        print("Reader started")
        
      def format_distance_output(self, total_coords):    
        total_coords.sort(key=lambda x: x[0]) #sort coordinates by x value
        output = ""
        for coord in total_coords:
            if(coord[1]==10): 
                if("." not in output): output += "."   #if coord is '.' and not in output, append   
            elif(coord[1]==11): 
                if("-" not in output): output += "-" #if coord is '-' and not in output, append   
            elif(("." not in output) or ("." in output and output.index(".") is len(output)-1)): output += str(coord[1])
        
        #get index of first value after "-" (if present) and last value before dot (if present) - delete everything in between.
        fst = 1 if "-" in output else 0
        lst = len(output)-1 if not("." in output) else output.index(".")-1   
        if(not(fst==lst)): output[0:fst+1] + output[lst:] 
        
        if((self.distance_last_output == "3.9" or self.distance_last_output == "4" or self.distance_last_output == "4.1") and output == "44"): output = "4" #special case.    
        return output
      
      def get_distance(self):
        while(True):
            img = ImageGrab.grab(bbox=(distance_x,distance_y,distance_w,distance_h)) #bbox specifies specific region (bbox= x,y,width,height)
            img_np = np.array(img)
            frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
            threshold = 0.884
            total_coords = []
            for count, image in enumerate(digits):
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                result = cv2.matchTemplate(frame,image,cv2.TM_CCOEFF_NORMED)       
                match_indices = np.arange(result.size)[(result>threshold).flatten()]      
                coords = np.unravel_index(match_indices,result.shape) #coordinate of match(s)
                if len(coords[1])>0: #only coords[1] matters. its of size 2, 0 has y value and 1 has x i think. if match(s) found:
                    for np_coord in coords[1]:
                        total_coords.append([np_coord, count]) # add coordinate and digit to total coordinates
    
            output = self.format_distance_output(total_coords)  
            self.distance_last_output = output
            print(output)
            #return output
      
      def get_player(self):
        img = ImageGrab.grab(bbox=(player_x,player_y,player_w,player_h)) #bbox specifies specific region (bbox= x,y,width,height)
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        return frame


