import math
from .function_fitness import FunctionFitness
class RealFunction(FunctionFitness):
    
    def calc_fitness(self, chromossome):
        #length_info = len(chromossome)/2
        #x = chromossome[:int(length_info)]
        #x_string = '0b'
        #for i in x:
            #x_string = x_string + str(i)
        #x = int(x_string, 2)
        
        #x = x*200/(math.pow(2, length_info) - 1)
        
        #x = x - 100
            
        #y = chromossome[int(length_info):]
        #y_string = '0b'
        #for i in y:
            #y_string = y_string + str(i)
        #y = int(y_string, 2)
        
        #y = y*200/(math.pow(2, length_info) - 1)
        
        #y = y - 100
        
        #result_function = self.__function(x,y) 
        #return result_function, (x, y)
        
        #result_function = self.__function(chromossome[0], chromossome[1]) 
        #return result_function, (chromossome[0], chromossome[1])
        
        result_functions = self.__function(chromossome[0],chromossome[1]) + self.__function(chromossome[1],chromossome[2]) + self.__function(chromossome[2],chromossome[3]) + self.__function(chromossome[3],chromossome[4]) + self.__function(chromossome[4],chromossome[0]) 
        return result_functions, chromossome[:5]
        
        
        
    
    
    def __function(self, x, y):
        return 0.5 - ((math.pow(math.sin(math.sqrt((math.pow(x,2) + math.pow(y,2)))),2) - 0.5)/math.pow(1 + 0.001*(math.pow(x,2) + math.pow(y,2)),2))