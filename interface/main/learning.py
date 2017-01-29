import random
from dependancies import *

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

alphabet = ["", "p", "o", "op", "w", "wp", "wo", "wop", "q", "qp", "qo", "qop", "qw", "qwp", "qwo", "qwop"]