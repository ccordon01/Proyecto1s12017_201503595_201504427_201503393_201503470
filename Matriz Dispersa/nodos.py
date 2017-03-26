from ArbolAVL import Arbol
#Clase De Nodo Base De Una Lista
class Claseuno(object):

#Constructor
     def __init__(self,datos,nodo):
     	 self.datos = datos
     	 self.nodo = nodo
class Clasedos(object):
	
#Constructor
     def __init__(self,datos,nodoSiguiente,nodoAnterior):
     	 self.datos = datos
     	 self.nodoSiguiente = nodoSiguiente
     	 self.nodoAnterior = nodoAnterior
class Clasetres(object):
	
#Constructor
     def __init__(self,datos,nodoSiguiente,nodoAnterior,nodoSuperior,nodoInferior):
     	 self.datos = datos
     	 self.nodoSiguiente = nodoSiguiente
     	 self.nodoAnterior = nodoAnterior
     	 self.nodoInferior = nodoInferior
     	 self.nodoSuperior = nodoSuperior

class Clasecuatro(object):
	
#Constructor
     def __init__(self,letra,correo,lista):
     	 self.lista = lista
     	 self.letra = letra
     	 self.correo = correo

class Clasecinco(object):
     
#Constructor
     def __init__(self,usuario,passw):
          self.usuario = usuario;
          self.passw = passw;
          self.nodoAVL =  Arbol()
