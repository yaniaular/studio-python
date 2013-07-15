class Autenticar(object):
    def __init__(self, f):
        self.f = f
    def __call__(self, user, paswd):
        print "Estoy en Autenticar"
        if user == 'yani' and paswd == '123':
            self.f(user, paswd)
        else:
            print 'Error en los datos'
    
@Autenticar
def Login(u, p):
    print "Estoy en Login"
    print 'Bienvenido'

@Autenticar
def ver_correo(u, p):
    print "Estoy en ver_correo"
    print 'Hola mundo'
    
user = raw_input('Introduzca su usuario:')
paswd = raw_input('Introduzca password:')
Login(user, paswd)
ver_correo(user, paswd)
