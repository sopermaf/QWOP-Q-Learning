from dependancies import *
    
def get_rand_bool():
    return bool(random.getrandbits(1))

class Controller(object):
    def __init__(self):
        self.key_history = ""  #will store the key strokes for each game
        print("Controller started")

    def check_for_end(self): 
        if(check_for_restart_image()):
            #store key press somewhere??
            self.keypress(" ", "end")
            
    def keypress(self, char, action):
        if(action is "down"): pyautogui.keyDown(char)
        if(action is "up"): pyautogui.keyUp(char)
        if(action is "end"): pyautogui.press(char)
    
    def keyInterpret(self, char, keyCombo):
        if char in keyCombo:
            pyautogui.keyDown("q")
        else:
            pyautogui.keyUp("q")
    
    def generateKeyCombo(self):
        down = [get_rand_bool(),get_rand_bool(),get_rand_bool(),get_rand_bool()]
        key_combo = ""
        
        #generate the string combo
        if down[0]: key_combo += "q"
        if down[1]: key_combo += "w"
        if down[2]: key_combo += "o"
        if down[3]: key_combo += "p"
        
        return key_combo
    
    #function sending keypress
    def running(self):  
        while(True): 
            #(1) capture the string of keypresses
            #(2) store the keypresses when the game has finished for evaluation
            
            #generate the random move
            move = self.generateKeyCombo()
            
            #execute the move
            self.keyInterpret("q", keyCombo)
            self.keyInterpret("w", keyCombo)
            self.keyInterpret("o", keyCombo)
            self.keyInterpret("p", keyCombo)
            
            #add to history
            self.key_history += " + " move
            
            #check for end
            sleep(random.uniform(0,0.05))       
            self.check_for_end()    #STORE THE STRING IN THIS FUNCTION TO FILE?
            
            #if check_end == true: store AND genetic evaluation
            
            
            
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
