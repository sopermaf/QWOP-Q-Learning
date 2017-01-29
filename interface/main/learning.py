import random
import time

from datetime import datetime
random.seed(datetime.now())

#genetic alphabet
MIN_NUM_GENES = 8
MAX_NUM_GENES = 16

NUM_TYPES_GENES = 16

def get_rand_bool():
    return bool(random.getrandbits(1))

def create_runner():
    new_runner = []
    end_creation = False
    genetic_length = random.randint(MIN_NUM_GENES,MAX_NUM_GENES)
    
    for i in range(0, genetic_length):
        new_gene = random.randint(0,15)
        new_runner.append(new_gene)
        
    return new_runner

#changes 1 gene in the genetic sequence
def mutation(genetic_sequence):
    size = len(genetic_sequence)
    gene_num = random.randint(0,size-1)
    new_mutation = random.randint(0,NUM_TYPES_GENES-1)
    #print (gene_num, new_mutation)
    
    #ensure the mutation cannnot be the same as before
    while new_mutation == genetic_sequence[gene_num]:
       new_mutation = random.randint(0,NUM_TYPES_GENES-1)
    
    new_gen = list(genetic_sequence)
    new_gen[gene_num] = new_mutation
    
    return new_gen

