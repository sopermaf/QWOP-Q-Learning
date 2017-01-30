from dependancies import *
import controller
import random
from operator import itemgetter

#initial_file_write = open("initial.txt", 'w')
initial_file_read = open("initial.txt", 'r')
final_file_write = open("final.text", "w")

row_length = 5
col_length = 6
total_length = row_length * col_length

torus = [[['NNMJBACDOHIPIMKDIC', 2.4], ['KMNHMMEAOH', 2.8], ['LIDNJBDDHGAEN', 2.4], ['PGJHDLCIGNAMMJ', 2.2], ['HMAKOHAEGDGPDOMC', 2.4]], 
         [['NNMJBACDOHIPIMKDIC', 2.4], ['KMNHMMEAOH', 2.8], ['LIDNJBDDHGAEN', 2.4], ['PGJHDLCIGNAMMJ', 2.2], ['HMAKOHAEGDGPDOMC', 2.4]], 
         [['NNMJBACDOHIPIMKDIC', 2.4], ['KMNHMMEAOH', 2.8], ['LIDNJBDDHGAEN', 2.4], ['PGJHDLCIGNAMMJ', 2.2], ['HMAKOHAEGDGPDOMC', 2.4]], 
         [['NNMJBACDOHIPIMKDIC', 2.4], ['KMNHMMEAOH', 2.8], ['LIDNJBDDHGAEN', 2.4], ['PGJHDLCIGNAMMJ', 2.2], ['HMAKOHAEGDGPDOMC', 2.4]], 
         [['NNMJBACDOHIPIMKDIC', 2.4], ['KMNHMMEAOH', 2.8], ['LIDNJBDDHGAEN', 2.4], ['PGJHDLCIGNAMMJ', 2.2], ['HMAKOHAEGDGPDOMC', 2.4]], 
         [['NNMJBACDOHIPIMKDIC', 2.4], ['KMNHMMEAOH', 2.8], ['LIDNJBDDHGAEN', 2.4], ['PGJHDLCIGNAMMJ', 2.2], ['HMAKOHAEGDGPDOMC', 2.4]]]                           

def split_list(list):
    result = []
    start = 0
    end = row_length
    while(end<=len(list)):
        row = list[start:end]
        result.append(row)
        start+=row_length
        end+=row_length
    return result
       
def int_to_alphabet(runner):
    string = ""
    for int in runner:
        string += alphabet_string[int]
    return string

def create_runner():
    new_runner = []
    end_creation = False
    genetic_length = random.randint(MIN_NUM_GENES,MAX_NUM_GENES)  
    for i in range(0, genetic_length):
        new_gene = random.randint(0,15)
        new_runner.append(new_gene)
        
    return new_runner           

def get_best_neighbour(torus, x, y):
    neighbour_list = []  
    index_list = [] 
    #gets neighbour torus positions 
    for neighbour_x in range(-1,2):
        for neighbour_y in range(-1,2):
            if(not(neighbour_x==0 and neighbour_y==0)):
                x_pos = ((x+neighbour_x)+col_length)%col_length
                y_pos = ((y+neighbour_y)+row_length)%row_length
                neighbour_list.append(torus[x_pos][y_pos])
                index_list.append([x_pos,y_pos])

    #creates a list of fitness values for sorting
    fitness_list = []
    for i in range(0,len(neighbour_list)):
        fitness_list.append(neighbour_list[i][1])
    
    
    #if multiple best neighbours, chose one at random.
    indexes_of_best_neighbour = [i for i, j in enumerate(fitness_list) if j==max(fitness_list)]     
    if(len(indexes_of_best_neighbour)==1): best_neighbour = indexes_of_best_neighbour[0]
    else: best_neighbour = indexes_of_best_neighbour[random.randint(0,len(indexes_of_best_neighbour)-1)]
    #finally, convert best neighbour to index relative to x and y.
    return index_list[best_neighbour]
      
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
    
    return str(new_gen)

#returns an list of lists, with x[0] = A_splice, x[1] = B_splice
def single_splice(genetic_A, genetic_B):
    size = len(genetic_A)
    if(len(genetic_B) > size):
        size = len(genetic_B)
    
    cut = random.randint(1, size-2) #splice cuts everything above this
    
    #make the cuts
    new1 = genetic_A[:cut]
    new1.extend(genetic_B[cut:])
    new2 = genetic_B[:cut]
    new2.extend(genetic_A[cut:])
 
    #return as a list of the new spliced lists
    cl = []
    cl.append(new1)
    cl.append(new2)
    cl[0] = str(cl[0])
    cl[1] = str(cl[1])
    return cl

def convert_string_to_int_alphabet(string):
    int = []
    string = list(string)
    for letter in string:    
        int.append(alphabet_string.index(letter))    
    return int
    
'''  To train first set of runners.
def initial():
    c = controller.Controller()
    c.start()
    num_runners = 0
    while(num_runners<MAX_INITIAL_RUNNERS):
        runner = create_runner()
        fitness_result = c.runner_fitness_test(runner)
        runner_str = int_to_alphabet(runner)
        initial_file_write.write(runner_str + " " + str(fitness_result) + "\n")
        c.check_for_end()
        num_runners+=1
'''

def post_process(): #take best 30 from runners 
    with initial_file_read as f:
        content = f.readlines()
        content = [x.strip() for x in content] 
    for i,line in enumerate(content):
        content[i] = content[i].split(" ")
        try: content[i][1] = float(content[i][1]) #divide into numbers only
        except ValueError: content[i][1] = 0
    best_content = sorted(content, key=itemgetter(1))
    return best_content[len(best_content)-30:]

def list_to_string(list):
    string = ""
    
    for element in list:
        if element in alphabet_string:
            string += str(element)
    
    return string
    
def final_process(): 
    c = controller.Controller()
    c.start()
    iterations = 0
    while(True):
        #update the fitness metrics
        for i in range(0,col_length):
            for j in range(0,row_length):
                #perform run
                genetic = convert_string_to_int_alphabet(str(torus[i][j][0]))
                new_fitness = c.runner_fitness_test(genetic)
                torus[i][j][1] = new_fitness
                
                #restart game
                c.check_for_end()
                
        #splicing stage
        for i in range(0,col_length):
            for j in range(0,row_length):
                #get best neighbour
                best_neighbour = get_best_neighbour(torus,i,j)
                do_splice = single_splice(list(torus[i][j][0]),list(torus[best_neighbour[0]][best_neighbour[1]][0]))
                
                torus[i][j][0] = list_to_string(do_splice[0]) #********DATA CORRUPTION WAS HAPPENING HERE FROM LIST -> STRING
                torus[best_neighbour[0]][best_neighbour[1]][0] = list_to_string(do_splice[1]) #********DATA CORRUPTION WAS HAPPENING HERE FROM LIST -> STRING
                #print(torus[i][j][0]) #******PRINTING HERE SHOWED THE CORRUPTION AS IT HAPPENED********

        #mutation stage   
        for i in range(0,col_length):
            for j in range(0,row_length):
                torus[i][j][0] = mutation(list(torus[i][j][0]))
        
        #write all to file every torus completion
        #*******NEED TO CLOSE THE FILE OR CHANGE FILE NAME EACH TIME BECAUSE IT BECOMES HUGE*************
        final_file_write.write("Iteration: " + str(iterations) + "\n")
        for i in range(0,col_length):
            for j in range(0,row_length):
                final_file_write.write(torus[i][j][0] + " " + torus[i][j][1]  + "\n")
        final_file_write.write("\n")
                    
if __name__ == "__main__": 
    final_process()
      
