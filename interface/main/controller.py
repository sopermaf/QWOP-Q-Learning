from dependancies import *
    
def get_rand_bool():
    return bool(random.getrandbits(1))

class Controller(object):
    def __init__(self):
        print("Controller started")

    def check_for_end(self): 
        if(check_for_restart_image()):
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
        start_game = [player_x+100,player_y+100]
        pyautogui.click(start_game)
        pyautogui.click(start_game)
        self.running()

'''
if __name__ == "__main__":
    c = Controller()
    c.start()
'''
