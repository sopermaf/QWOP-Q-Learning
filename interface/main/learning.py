import random
import time

#genetic alphabet
MIN_NUM_GENES = 8
MAX_NUM_GENES = 16

def get_rand_bool():
    return bool(random.getrandbits(1))

def create_runner():
    new_runner = []
    end_creation = False
    
    while end_creation == False and len(new_runner) < MAX_NUM_GENES:
        new_gene = random.randint(0,15)
        new_runner.append(new_gene)
        
        if len(new_runner) < MIN_NUM_GENES:
            end_creation = False
        else:
            end_creation = get_rand_bool()
        
    return new_runner

start = time.clock()

for x in range(0,500000):
    y = x
    
print(time.clock() - start)