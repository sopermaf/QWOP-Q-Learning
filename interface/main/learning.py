import random

def generateKeyCombo():
    down = [get_rand_bool(),get_rand_bool(),get_rand_bool(),get_rand_bool()]
    key_combo = ""
    
    #generate the string combo
    if down[0]: key_combo += "q"
    if down[1]: key_combo += "w"
    if down[2]: key_combo += "o"
    if down[3]: key_combo += "p"
    
    return key_combo

def get_rand_bool():
    return bool(random.getrandbits(1))
    
for x in range (0,10):   
    move = generateKeyCombo()
    if "q" in move:
        print("CONTAINS A Q", move)
    else: 
        print(move)