g = lambda x: x**2 # En vez de funciones se puede usar lambda
print g(4) # devuelve 4**2

######

def incrementor(n): #Funciones anidadas
	def suma(x):
		return n + x
	return suma
	
x = incrementor(3) #Devuelve una funcion, es decir x pasar a ser la funcion suma con un n = 3
print x(4) # Devuelve la suma (n + x), ya que x es una funcion con el n = 3, y x = 4

print incrementor(20)(30)# Estoy mandando 'n' y 'x' de una vez 

######

def incrementor(n):
	return lambda x: x + n
	
f = incrementor(2) #incrementor retorna un objeto lambda, es decir, f trabajara como una funcion.
g = incrementor(6) #incrementor retorna un objeto lambda, es decir, f trabajara como una funcion.

print f(42), g(42) #Utilizo los lambda 'f' y 'g' como funciones

#####

foo = [2,18,9,22,17,24,8,12,27]
print filter(lambda x: x % 3 == 0, foo)

print map(lambda x: x * 2 + 10, foo)


def f(x):
	return ' '.join([ i.capitalize() if len(i)>2 else i for i in x.strip().replace('php','python').split()])
print f('   este es el curso de php    ')

def flambda(s):
	return map(lambda x: len(x),s.split()) #Cuenta la cantidad de caracteres de cada palabra de la frase s
	
print flambda('Esta ahora lloviendo perros y gatos')


