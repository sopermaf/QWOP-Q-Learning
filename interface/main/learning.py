import numpy as np

#NEEDS TO BE GIVEN ACTUAL FUNCITONALITY
def calc_reward():
    #is_dead? (large neg) game_won (large pos)
    game_state = 0  #some image classification
    
    #movement_direction (- for neg, + for pos)
    moment_direction = 0 #curr_dist - prev_dist check
    
    #time_pass (small neg)
    time_reward = -1 #fixed as time passes
    
    state_reward = game_state + moment_direction + time_reward
    
    return state_reward;

def get_actions():    
    a = []
    for x in range(0, 16):
        q_val = 1
        w_val = 0
        o_val = 0
        p_val = 0
        
        if (x+1)%2 == 0:
            p_val = 1
        
        if (x+1)%4 == 0 or (x+2)%4 == 0:
            o_val = 1 

        if (x+1)%8 == 0 or (x+2)%8 == 0 or (x+3)%8 == 0 or (x+4)%8 == 0:
            w_val = 1

        if x < 8:
            q_val = 0
        
        b = [q_val, w_val, o_val, p_val]
        a.append(b)
    return a

learning_rate = 0.1
total_reward = 0
discount_factor = 0.4

#q table 
NUM_STATES = 16 #4 binary value keys
NUM_ACTIONS = 16 #4 different keys, can be up or down

q_values = np.zeros([NUM_STATES, NUM_ACTIONS])

print (q_values)