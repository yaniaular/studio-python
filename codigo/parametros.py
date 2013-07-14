# -*- encoding: utf-8 -*-
#!/usr/bin/python

def TiendaDeQueso(kind, *arguments, **keywords):                        
    print "-- ¿Tienes ", kind, "?"                                      
    print "-- Lo siento, en este momento no tenemos ", kind             
    for arg in arguments:                                               
        print arg                                                       
    print "-" * 40                                                      
    keys = sorted(keywords.keys())                                      
    for kw in keys:                                                     
        print kw, ":", keywords[kw]                                     
                                                                        
TiendaDeQueso("Quesoburger", "Es derretido, señor",                     
   "El queso es realmente muy derretido, señor",                        
   vendedor='Michael Palin',                                            
   cliente="John Cleese",                                               
   tienda="Cheese Shop Sketch")  
