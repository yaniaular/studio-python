#numeros impares con raices cuadradas exactas
import math                                                             
def exacta(x):                                                          
    y = math.sqrt(x)                                                    
    if y.is_integer():                                                  
        z = True                                                        
    else:                                                               
        z = False                                                       
    return z                                                            
def f(x):                                                               
    if x % 2 is 0:                                                      
        y = True                                                        
    else:                                                               
        y = False                                                       
    return y                                                                                                                               
                                                                        
print [x for x in xrange(1, 20) if not f(x) and exacta(x)] 
