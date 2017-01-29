from dependancies import *
    
def get_rand_bool():
    return bool(random.getrandbits(1))

class Controller(object):
    def __init__(self):
        print("Controller started")

    def check_for_end(self): 
        if(check_for_restart_image()):
            #store key press somewhere??
            self.keypress(" ", "end")
            
    def keypress(self, char, action):
        if(action is "down"): pyautogui.keyDown(char)
        if(action is "up"): pyautogui.keyUp(char)
        if(action is "end"): pyautogui.press(char)
    
    def keyInterpret(self, char, key_combo):
        if char in key_combo:
            pyautogui.keyDown(char)
        else:
            pyautogui.keyUp(char)
    
    #takes genetic encoding number/letter and decodes into keypress
    def makeMove(self, move):
        #turn the number into the string
        move_decoded = alphabet[move]
        
        #execute the relevant key presses for the string
        self.keyInterpret("q", move_decoded)   
        self.keyInterpret("w", move_decoded)
        self.keyInterpret("o", move_decoded)
        self.keyInterpret("p", move_decoded)
    
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
            
            #run game for a given runner genes
            #get fitness
            #store the info
            
            sleep(0.150)    #150ms sleep between steps like in the paper on genetic
            #read distance
            self.check_for_end()    #STORE THE STRING IN THIS FUNCTION TO FILE?          
                        
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
