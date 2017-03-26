import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('./')
#Importo la Clase
from nodos import Claseuno
from nodos import Clasedos
class ClaseLista(Claseuno):
	 def __init__(self):
	 	 self.primerNodo = None
	 	 self.ultimoNodo = None

	 def estaVacia(self):
	 	if self.primerNodo == None:
	 		print "si esta vacia"
	 		return True
	 	return False
	 def insertarAlFrente(self,datos):
	 	if self.estaVacia():
	 		 #print "insertar primer elemento en la lista"
	 		 self.ultimoNodo = Claseuno(datos,None)
	 		 self.primerNodo = self.ultimoNodo
	  	else:
	  		 #print "existen elementos en la lista"
	  	     self.primerNodo = Claseuno(datos,self.primerNodo)
	 def insertarAlFinal(self,datos):
	 	if self.estaVacia():
	 		 #print "insertar primer elemento en la lista x2" 
	 		 self.ultimoNodo = Claseuno(datos,None)
	 		 self.primerNodo = self.ultimoNodo
	  	else:
	  		 #print "existen elementos en la lista x2"
	  		 self.ultimoNodo.nodo = Claseuno(datos,None)
	  	     	 self.ultimoNodo = self.ultimoNodo.nodo
	  	#print("guau") 
	 def eliminarDelFrente(self):
	 	if self.estaVacia():
	 		return "Esta vacia"
	 	else:
	 		data = self.primerNodo.datos
	 		self.primerNodo = self.primerNodo.nodo
	 		return data
	 def mostrar(self):
	 	 actual = self.primerNodo
	 	 while (actual != None):
	 	 	print "Dato: " + actual.datos
	 	 	actual = actual.nodo
	 	 print "Fin"
class ClaseListaDoble(Clasedos):
	 def __init__(self):
	 	 self.primerNodo = None
	 	 self.ultimoNodo = None

	 def estaVacia(self):
	 	if self.primerNodo == None:
	 		print "si esta vacia"
	 		return True
	 	return False
	 def insertarAlFrente(self,datos):
	 	if self.estaVacia():
	 		 #print "insertar primer elemento en la lista"
	 		 self.ultimoNodo = Clasedos(datos,None,None)
	 		 self.primerNodo = self.ultimoNodo
	  	else:
	  		 #print "existen elementos en la lista"
	  		 nuevo = Clasedos(datos,self.primerNodo,None)
	  		 self.primerNodo.nodoAnterior = nuevo
	  	         self.primerNodo = nuevo
	 def insertarAlFinal(self,datos):
	 	if self.estaVacia():
	 		 #print "insertar primer elemento en la lista x2" 
	 		 self.ultimoNodo = Clasedos(datos,None,None)
	 		 self.primerNodo = self.ultimoNodo
	  	else:
	  		 #print "existen elementos en la lista x2"
	  		 self.ultimoNodo.nodoSiguiente = Clasedos(datos,None,self.ultimoNodo)
	  	     	 self.ultimoNodo = self.ultimoNodo.nodoSiguiente
	  	#print("guau") 
	 def eliminarDelFrente(self):
	 	if self.estaVacia():
	 		return "Esta vacia"
	 	else:
	 		data = self.primerNodo.datos
	 		self.primerNodo.nodoAnterior = None
	 		self.primerNodo = self.primerNodo.nodoSiguiente
	 		#self.primerNodo.nodoAnterior = None
	 		return data
	 def mostrar(self):
	 	 actual = self.primerNodo
	 	 while (actual != None):
	 	 	print "Dato: " + actual.datos
	 	 	actual = actual.nodoSiguiente
	 	 print "Fin"
	 def size(self):
	 	 size = 0
	 	 actual = self.primerNodo
	 	 while (actual != None):
	 	 	size = size + 1
	 	 	#print "Dato: " + actual.datos
	 	 	actual = actual.nodoSiguiente
	 	 #print "Fin"
	 	 return size
	 def delbypos(self,pos):
	 	 if not self.estaVacia():
	 	 	actual = self.primerNodo
	 	 if int(pos) == 0:
	 	 	 return self.eliminarDelFrente()
	 	 if (int(pos) + 1) == self.size():
	 	 	    actual = self.ultimoNodo
	 	 	    data = actual.datos
	 	 	    actual.nodoAnterior.nodoSiguiente = actual.nodoSiguiente
	 	 	 	#actual.nodoSiguiente.nodoAnterior = actual.nodoAnterior
	 	 	    return data
	 	 else:
	 	 	for x in xrange(1,self.size()):
	 	 	 actual = actual.nodoSiguiente
	 	 	 if x==int(pos):
	 	 	 	data = actual.datos
	 	 	 	actual.nodoAnterior.nodoSiguiente = actual.nodoSiguiente
	 	 	 	actual.nodoSiguiente.nodoAnterior = actual.nodoAnterior
	 	 	 	return data
	 	 return "null"
	 def delbyvalue(self,value):
	 	 actual = self.primerNodo
	 	 for x in xrange(0,self.size()):
	 	 	 #return value + "=" + actual.datos
	 	 	 if str(value) == str(actual.datos):
	 	 	 	print "Se encontro en la posicion: " + str(x)
	 	 	 	return self.delbypos(x)
	 	 	 actual = actual.nodoSiguiente
	 def byvalue(self,value):
	 	 actual = self.primerNodo
	 	 for x in xrange(0,self.size()):
	 	 	 if str(value) == str(actual.datos):
	 	 	 	return x
	 	 	 	#return self.delbypos(x)
	 	 	 actual = actual.nodoSiguiente
	 	 return "null"
	 def mostrarc(self):
	 	 actual = self.primerNodo
	 	 text = ""
	 	 while (actual != None):
	 	 	text= actual.datos.usuario + "," +text
	 	 	actual = actual.nodoSiguiente
	 	 return text

	 	
	  		     
	 	