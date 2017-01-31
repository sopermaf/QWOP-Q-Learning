from dependancies import *

class Reader(object):
      distance_last_output = 0.2
      
      def __init__(self):
        pass
              
      def format_output(self, total_coords):
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
        if(not(fst==lst)): 
            output = output[0:fst+1] + output[lst:]  

        #special case. some values repeat, this removes them.
        if(self.distance_last_output < 10 and not(output == "10")): 
            fst = 1 if "-" in output else 0
            if(("." in output and (output.index(".")==fst+2)) or (len(output)==fst+2)):
                output = output.replace(output[fst],"",1)        
        return float(output)
       
      def get_distance(self):
        try:
            #parameters for screen: ManyCam 768p, half size frame. frame not shown. full screen chrome
            _, frame = cap.read()   
            frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) 
            frame = frame[int(distance_y):int(distance_y+distance_h), int(distance_x):int(distance_x+distance_w)] #[y: y + h, x: x + w]   
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            threshold = 0.86

            total_coords = []
            for count, image in enumerate(digits):
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                result = cv2.matchTemplate(frame,image,cv2.TM_CCOEFF_NORMED)       
                match_indices = np.arange(result.size)[(result>threshold).flatten()]      
                coords = np.unravel_index(match_indices,result.shape) #coordinate of match(s)
                if len(coords[1])>0: #only coords[1] matters. its of size 2, 0 has y value and 1 has x i think. if match(s) found:
                    for np_coord in coords[1]:
                        total_coords.append([np_coord, count]) # add coordinate and digit to total coordinates              

            output = self.format_output(total_coords)
            if(self.distance_last_output!=output):
                self.distance_last_output = output
                return output
        except ValueError:
            return 0.2
      