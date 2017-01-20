from dependancies import *
    
def get_rand_bool():
    return bool(random.getrandbits(1))

class Controller(object):
    def __init__(self):
        print("Controller started")

    def check_for_end(self):
        img = ImageGrab.grab(bbox=(restart_x, restart_y, restart_w, restart_h)) 
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)       
        result = cv2.matchTemplate(frame,restart_image,cv2.TM_CCOEFF_NORMED)
        threshold = 0.71
        match_indices = np.arange(result.size)[(result>threshold).flatten()]      
        coords = np.unravel_index(match_indices,result.shape) #coordinate of match(s)
        if(len(coords[1])>0):
            self.keypress(" ", "end")
            
    def keypress(self, char, action):
        if(action is "down"): pyautogui.keyDown(char)
        if(action is "up"): pyautogui.keyUp(char)
        if(action is "end"): pyautogui.press(char)
        
    def running(self):  
        while(True): 
            downs = [get_rand_bool(),get_rand_bool(),get_rand_bool(),get_rand_bool()]
            ups = [get_rand_bool(),get_rand_bool(),get_rand_bool(),get_rand_bool()]
            if(downs[0]): self.keypress("q","down")
            if(downs[1]): self.keypress("w","down")
            if(downs[2]): self.keypress("o","down")
            if(downs[3]): self.keypress("p","down")
            if(ups[0]): self.keypress("q","up")
            if(ups[1]): self.keypress("w","up")
            if(ups[2]): self.keypress("o","up")
            if(ups[3]): self.keypress("p","up")
            sleep(random.uniform(0,0.05))       
            self.check_for_end()
    
    def start(self):
        start_game = pyautogui.locateCenterOnScreen(path_images_control+'click_to_begin.png')
        pyautogui.click(start_game)
        pyautogui.click(start_game)
        self.running()


