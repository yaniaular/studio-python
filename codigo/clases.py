class LibretaTelefonica(): #Funciona sin parentesis o con parentesis
	'Mi primera clase'
	version = 1.0
	def __init__(self, nm, nt): #Siempre debe recibir self, se refiere a this pero en python
		self.nombre = nm	#Constructor __init___
		self.telefono = nt
		
	def actualizarTel(self, nuevo):
		self.telefono = nuevo
		
	def getVersion(self):
		return self.version
	
	def setVersion(self, nuevo):
		self.version = nuevo
		

yani = LibretaTelefonica('Yanina','0412-123234')		


class MiClase:
	version = '1.0.x'
	def __init__(self, pv, sv):
		self.pv = pv
		self.sv = sv
	
	def get_pv(self):
		return self.pv
		
	def set_pv(self, pv_n):
		self.pv = pv_n
	
	def get_sv(self):
		return self.sv
		
	def set_sv(self, sv_n):
		self.sv = sv_n
		
mc = MiClase('primero','segundo')

print mc.pv
print mc.get_pv()
mc.set_pv('Otro')
print mc.get_pv()
		
		
class MiSegundaClase(MiClase): #Hereda MiClase
		def __init__(self, x, pv, sv):
			self.x = x
			MiClase.__init__(self, pv, sv) #Se necesita inicializar los valores de la clase padre si se quieren consultar.
			#Se puede utilizar args para mandar 1 o mas parametros, depende de lo que quiera inicializar
			
		def get_x(self):
			return self.x
			
		def set_x(self, x_n):
			self.x = x_n
			
msc = MiSegundaClase('SegundaClase', 'PV Segunda clase', 'SV Segunda Clase')

#print msc.get_pv()			#Esto da error porque los argumentos de la clase padre no han sido inicializados
			
#'valor < valor2'
#exec		
	
