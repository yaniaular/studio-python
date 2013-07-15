# -*- encoding: utf-8 -*-

for line in open("archivo.txt"):
    print line

#El problema con este código es que deja el archivo abierto por 
#una cantidad indeterminada de tiempo después de que el código 
#ha terminado de ejecutarse. Esto no es un problema en secuencias 
#de comandos simples, pero puede ser un problema para aplicaciones 
#más grandes. La declaración permite con objetos como archivos que 
#se utilizan de una manera que asegura que siempre se limpian 
#rápidamente y correctamente.

with open('archivo.txt', 'r') as f:
    for line in f:
        print line


