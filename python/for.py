print "\nfor con (1,2,3,4)"
for valor in (1, 2, 3, 4):
	print "Numero ", valor

print "\nfor con range(10)"
for variable in range(10):
	print "Numero ", variable

print "\nfor con range(5,10)"
for variable in range(5, 10):
	print "Numero ", variable

print "\nfor con range(1,50,5)"
for variable in range(1, 50, 5):
	print "Numero ", variable
	
















print "\nQue tabla quieres saber?"
numero = int (input())
print "Esta es la tabla del numero ", numero
for variable in range(0, 11):
	print numero, " x ", variable , " = ", numero * variable 





















	
print "\n======= LISTA =======\n"
lista_personajes = ["Homer", "Bart", "Lisa", "Ned Flanders", "Maggie"]

print lista_personajes
print lista_personajes[0]
print lista_personajes[1:3]
print lista_personajes[-1]

print "\n======= RECORRER LISTA CON FOR ======\n"
for personaje in lista_personajes:
	print personaje, "aparece en la serie Los Simpson"

print "\n======= ANIADIR Y QUITAR UN ELEMENTO DE UNA LISTA =========\n"
lista_personajes.append("Calamardo")
print "He aniadido Calamardo a mi lista "
print lista_personajes

lista_personajes.remove("Ned Flanders")
print "He borrado a Ned Flanders de mi lista "
print lista_personajes

#Funciones

def mayor_de_edad(anios):
    """ Calcula si eres mayor de edad."""
    if anios >= 18:
        print "Eres mayor de Edad"
    else:
        print "Renacuajo !!!"

def pesetas_a_euros(cantidad_en_pesetas):
    """Conversion de pesetas a euros"""
    return cantidad_en_pesetas / 166.386

def suma_dos_numeros(numero1, numero2):
    """Suma dos cantidades"""
    return numero1 + numero2
	

	
print "\n -==[ Funciones ]==- \n"
print "\n Escribe cuantos anios tienes"
anios = int (input())
mayor_de_edad(anios)
	

print "5000 pesetas son %0.2f euros" % (pesetas_a_euros(5000))
print "200 + 300 = ", suma_dos_numeros(200, 300)


