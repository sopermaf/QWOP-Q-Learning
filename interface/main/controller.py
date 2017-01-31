from dependancies import *
import learning
import reader
r = reader.Reader()

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
    
    def runner_fitness_test(self, genetic):
        distance = 0
        index = 0
        stop_time = 60 + time.clock()        
        #loop executes the run until crashed state or time is finished
        while check_for_restart_image() == False and time.clock() <= stop_time:
            self.makeMove(genetic[index])   #make an individual key combination
            index += 1            
            
            if index >= len(genetic):   #repeat the genetic sequence when the end is reached
                index = 0
            
            distance = r.get_distance()
            sleep(0.150)
        
        #check that the runner didn't crash, if so return the distance. DECIDED TO USE DISTANCE INSTEAD. WERENT GETTING FAR.
        r.distance_last_output = 0.2
        return distance
    '''
    def running(self):  
        while(True): 
            gen_sequence = learning.create_runner()
            self.runner_fitness_test(gen_sequence)
            sleep(0.150)    #150ms sleep between steps like in the paper on genetic
            #read distance
            self.check_for_end()    #STORE THE STRING IN THIS FUNCTION TO FILE?          
    ''' 
    
    def refresh(self):
        pyautogui.moveTo(player_x+200, player_y)  
        pyautogui.click()
        pyautogui.hotkey('command', 'r') 
        time.sleep(3)   
        
    def start(self):
        start_game = [player_x+200,player_y+200]
        pyautogui.click(start_game)
        pyautogui.click(start_game)
        #self.running()

'''
if __name__ == "__main__": 
    start()
'''
