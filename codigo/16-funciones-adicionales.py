

lista = [1,2,3,4,5,6,7]

for i in lista:
    if i is 5 or i is 6:
        pass
    else:
        print i

for i in lista:
    print i
    if i == 4:
        print "Entro al condicional y se rompera el ciclo"
        break
    
for i in lista:
    if i == 5:
        print "Entre en el condicional, continuare con la iteracion"
        continue
    print "Voy por", i ,"llego al final de la iteracion"


x = 1
print eval("x+1")
y = eval("x + 5")
print y

try:
    x = int(raw_input("Por favor introduzca un numero:"))
except ValueError:
    print "El valor que introdujo no es valido"
    print ValueError
