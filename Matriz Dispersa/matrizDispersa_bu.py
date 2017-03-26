import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('./')
#Importo la Clase
from nodos import Claseuno
from nodos import Clasedos
from nodos import Clasetres
from nodos import Clasecuatro
from lista import ClaseListaDoble

class ClassMatriz(Clasetres):
    """docstring for ClassName"""
    def __init__(self):
        #super(ClassName, self).__init__()
        #self.arg = arg
        self.primerNodo = Clasetres("Nodo Inicial",None,None,None,None)

##########################   Cabecera Letras  #################################################        
    def insertarCabeceraLetras(self,letra):
        if self.primerNodo.nodoInferior == None:
             self.primerNodo.nodoInferior = Clasetres(letra,None,None,self.primerNodo,None)
             return "Primer nodo creado con " + letra
        if not self.elementExistInCabeceraLetras(letra):
             actual = self.primerNodo.nodoInferior
             temp = self.primerNodo.nodoInferior
             val = ord(letra)
             if val < ord(actual.datos):
                 nuevo = Clasetres(letra,None,None,self.primerNodo,actual)
                 self.primerNodo.nodoInferior = nuevo
                 actual.nodoSuperior = nuevo
                 return "Nodo Creado " + letra
             else:
                  while (actual != None):
                      if val < ord(actual.datos):
                          nuevo = Clasetres(letra,None,None,actual.nodoSuperior,actual)
                          actual.nodoSuperior.nodoInferior = nuevo
                          actual.nodoSuperior = nuevo
                          return "Nodo Creado " + letra
                      if not actual.nodoInferior == None:
                            temp = actual.nodoInferior
                      actual = actual.nodoInferior
                  nuevo = Clasetres(letra,None,None,temp,None)
                  temp.nodoInferior = nuevo 
                  return "Nodo Creado " + letra
    def elementExistInCabeceraLetras(self,letra):
         actual = self.primerNodo.nodoInferior
         while (actual != None):
               if actual.datos == letra:
                        print "Ya existe nodo"
                        return True
               actual = actual.nodoInferior
         print "No existe nodo"
         return False

    def mostrarCabeceraLetras(self):
         actual = self.primerNodo.nodoInferior
         while (actual != None):
               print "Nodo " + actual.datos
               actual = actual.nodoInferior
         print "Fin"
#########################################################################################

############################   Cabecera De Dominios    ##################################

    def insertarCabeceraDominios(self,dominio):
         if self.primerNodo.nodoSiguiente == None:
             self.primerNodo.nodoSiguiente = Clasetres(dominio,None,self.primerNodo,None,None)
             return "Primer dominio creado " + dominio
         if not self.elementExistInCabeceraDominios(dominio):
             actual = self.primerNodo.nodoSiguiente
             temp = self.primerNodo.nodoSiguiente
             val = ord(dominio[0])
             if val < ord(actual.datos[0]):
                 nuevo = Clasetres(dominio,actual,self.primerNodo,None,None)
                 self.primerNodo.nodoSiguiente = nuevo
                 actual.nodoAnterior = nuevo
                 return "Nodo Creado " + dominio
             else:
                  while (actual != None):
                      if val < ord(actual.datos[0]):
                          nuevo = Clasetres(dominio,actual,actual.nodoAnterior,None,None)
                          actual.nodoAnterior.nodoSiguiente = nuevo
                          actual.nodoAnterior = nuevo
                          return "Nodo Creado ant " + dominio
                      if val == ord(actual.datos[0]):
                          print "Nodo igual " + dominio
                          tam = 0
                          if len(dominio) > len(actual.datos):
                              tam = len(actual.datos) - 1
                          else: 
                              tam = len(dominio) - 1 
                          nuevo = None
                          for x in xrange(0,tam):
                            if dominio[x] > actual.datos[x]:
                                print dominio[x] + ">" + actual.datos[x]
                                nuevo = Clasetres(dominio,actual.nodoSiguiente,actual,None,None)
                                actual.nodoSiguiente.nodoAnterior = nuevo
                                actual.nodoSiguiente = nuevo
                                return "Nodo Creado 6" + dominio
                            if dominio[x] < actual.datos[x]:
                                print dominio[x] + "<" + actual.datos[x]
                                nuevo = Clasetres(dominio,actual,actual.nodoAnterior,None,None)
                                actual.nodoAnterior.nodoSiguiente = nuevo
                                actual.nodoAnterior = nuevo
                                return "Nodo Creado 7" + dominio
                          if nuevo==None:
                              if tam==len(actual.datos):
                                nuevo = Clasetres(dominio,actual.nodoSiguiente,actual,None,None)
                                actual.nodoSiguiente.nodoAnterior = nuevo
                                actual.nodoSiguiente = nuevo
                                return "Nodo Creado 8" + dominio
                              else:
                                nuevo = Clasetres(dominio,actual,actual.nodoAnterior,None,None)
                                actual.nodoAnterior.nodoSiguiente = nuevo
                                actual.nodoAnterior = nuevo
                                return "Nodo Creado 9" + dominio  
                      if not actual.nodoSiguiente == None:
                            temp = actual.nodoSiguiente
                      actual = actual.nodoSiguiente
                  nuevo = Clasetres(dominio,None,temp,None,None)
                  temp.nodoSiguiente = nuevo 
                  return "Nodo Creado post" + dominio


    def elementExistInCabeceraDominios(self,dominio):
         actual = self.primerNodo.nodoSiguiente
         while (actual != None):
               if actual.datos == dominio:
                        print "Ya existe nodo"
                        return True
               actual = actual.nodoSiguiente
         print "No existe nodo"
         return False

    def mostrarCabeceraDominios(self):
         actual = self.primerNodo.nodoSiguiente
         while (actual != None):
               print "Nodo " + actual.datos
               actual = actual.nodoSiguiente
         print "Fin"
#############################################################################################


###########################        Insertar correo        ###################################

    def insertarCorreo(self,name,dominio):
         self.insertarCabeceraLetras(name[0])
         self.insertarCabeceraDominios(dominio)
         listaData = ClaseListaDoble()
         NodoLetra = self.nodoL(name[0])
         nodoData = Clasecuatro(name[0],dominio,listaData)
         if NodoLetra == None:
             return "null"
         if NodoLetra.nodoSiguiente == None:
             nuevo = Clasetres(nodoData,None,NodoLetra,None,None)
             NodoLetra.nodoSiguiente = nuevo
             return "Nodo Creado " + name[0] + "-"+ dominio
         if not self.elementExistInMatriz(NodoLetra,dominio):
             actual = NodoLetra.nodoSiguiente
             temp = NodoLetra.nodoSiguiente
             val = ord(dominio[0])
             if val < ord(actual.datos.correo[0]):
                 nuevo = Clasetres(nodoData,actual,NodoLetra,None,None)
                 NodoLetra.nodoSiguiente = nuevo
                 actual.nodoAnterior = nuevo
                 return "Nodo Creado " + name[0] + "-"+ dominio
             else:
                  while (actual != None):
                      if val < ord(actual.datos.correo[0]):
                          nuevo = Clasetres(nodoData,actual,actual.nodoAnterior,None,None)
                          actual.nodoAnterior.nodoSiguiente = nuevo
                          actual.nodoAnterior = nuevo
                          return "Nodo Creado " + name[0] + "-"+ dominio
                      if val == ord(actual.datos.correo[0]):
                          print "Nodo igual " + dominio
                          tam = 0
                          if len(dominio) > len(actual.datos.correo):
                              tam = len(actual.datos.correo) - 1
                          else: 
                              tam = len(dominio) - 1 
                          nuevo = None
                          for x in xrange(0,tam):
                            if dominio[x] > actual.datos.correo[x]:
                                print dominio[x] + ">" + actual.datos.correo[x]
                                nuevo = Clasetres(nodoData,actual.nodoSiguiente,actual,None,None)
                                actual.nodoSiguiente.nodoAnterior = nuevo
                                actual.nodoSiguiente = nuevo
                                return "Nodo Creado " + name[0] + "-"+ dominio
                            if dominio[x] < actual.datos.correo[x]:
                                print dominio[x] + "<" + actual.datos.correo[x]
                                nuevo = Clasetres(nodoData,actual,actual.nodoAnterior,None,None)
                                actual.nodoAnterior.nodoSiguiente = nuevo
                                actual.nodoAnterior = nuevo
                                return "Nodo Creado " + name[0] + "-"+ dominio
                          if nuevo==None:
                              if tam==len(actual.datos.correo):
                                nuevo = Clasetres(nodoData,actual.nodoSiguiente,actual,None,None)
                                actual.nodoSiguiente.nodoAnterior = nuevo
                                actual.nodoSiguiente = nuevo
                                return "Nodo Creado " + name[0] + "-"+ dominio
                              else:
                                nuevo = Clasetres(nodoData,actual,actual.nodoAnterior,None,None)
                                actual.nodoAnterior.nodoSiguiente = nuevo
                                actual.nodoAnterior = nuevo
                                return "Nodo Creado " + name[0] + "-"+ dominio
                      if not actual.nodoSiguiente == None:
                            temp = actual.nodoSiguiente
                      actual = actual.nodoSiguiente
                  nuevo = Clasetres(nodoData,None,temp,None,None)
                  temp.nodoSiguiente = nuevo 
                  return "Nodo Creado " + name[0] + "-"+ dominio

             


    def nodoL(self,letra):
         actual = self.primerNodo.nodoInferior
         while (actual != None):
               if actual.datos == letra:
                   return actual
               actual = actual.nodoInferior
         return None

    def elementExistInMatriz(self,NodoLetra, correo):
         actual = NodoLetra.nodoSiguiente
         while (actual != None):
               if actual.datos.correo == correo:
                   return True
               actual = actual.nodoSiguiente
         return False

    def insertarDatos(self,name,dominio):
         NodoLetra = self.nodoL(name[0])
         if NodoLetra.nodoSiguiente == None:
             return "no hay siguiente"
         NodoDominio = self.nodoD(dominio)
         nodoMagico = self.nodoM(NodoLetra,dominio)
         if NodoDominio == None:
             return "null dominio"
         if nodoMagico == None:
             return "null magico"
         nodoMagico.lista.insertarAlFinal(name + "@" + dominio)
         if NodoDominio.nodoInferior == None:
             NodoDominio.nodoInferior = Clasetres(nodoMagico,None,None,NodoDominio,None)
             return "Primer nodo creado con " + nodoMagico.letra
         if not self.elementExistInCabeceraLetrasM(nodoMagico.letra,NodoDominio):
             actual = NodoDominio.nodoInferior
             temp = NodoDominio.nodoInferior
             val = ord(nodoMagico.letra)
             if val < ord(actual.datos.letra):
                 nuevo = Clasetres(nodoMagico,None,None,self.primerNodo,actual)
                 NodoDominio.nodoInferior = nuevo
                 actual.nodoSuperior = nuevo
                 return "Nodo Creado " + nodoMagico.letra
             else:
                  while (actual != None):
                      if val < ord(actual.datos.letra):
                          nuevo = Clasetres(nodoMagico,None,None,actual.nodoSuperior,actual)
                          actual.nodoSuperior.nodoInferior = nuevo
                          actual.nodoSuperior = nuevo
                          return "Nodo Creado " + nodoMagico.letra
                      if not actual.nodoInferior == None:
                            temp = actual.nodoInferior
                      actual = actual.nodoInferior
                  nuevo = Clasetres(nodoMagico,None,None,temp,None)
                  temp.nodoInferior = nuevo 
                  return "Nodo Creado " + nodoMagico.letra


    def nodoD(self,dominio):
         actual = self.primerNodo.nodoSiguiente
         while (actual != None):
               if actual.datos == dominio:
                        return actual
               actual = actual.nodoSiguiente
         return None

    def nodoM(self,NodoLetra, correo):
         actual = NodoLetra.nodoSiguiente
         while (actual != None):
               if actual.datos.correo == correo:
                   return actual.datos
               actual = actual.nodoSiguiente
         return None
    def elementExistInCabeceraLetrasM(self,letra,nd):
         actual = nd.nodoInferior
         while (actual != None):
               if actual.datos.letra == letra:
                        print "Ya existe nodo"
                        return True
               actual = actual.nodoInferior
         print "No existe nodo"
         return False

    def findbyl(self,letra):
         NodoLetra = self.nodoL(letra[0])
         if NodoLetra == None:
           return "Letra no existe"
         actual = NodoLetra.nodoSiguiente
         text = ""
         while (actual != None):
               text =text + actual.datos.lista.mostrarc()
               actual = actual.nodoSiguiente
         return text

    def findbyd(self,dominio):
         NodoLetra = self.nodoD(dominio)
         if NodoLetra == None:
           return "Dominio no existe"
         actual = NodoLetra.nodoInferior
         text = ""
         while (actual != None):
               text = text + actual.datos.lista.mostrarc()
               #return text
               actual = actual.nodoInferior
         return text
    def borrarDatos(self,name,dominio):
       NodoLetra = self.nodoL(name[0])
       if NodoLetra.nodoSiguiente == None:
        return "no hay siguiente"
       NodoDominio = self.nodoD(dominio)
       nodoMagico = self.nodoM(NodoLetra,dominio)
       if NodoDominio == None:
        return "null dominio"
       if nodoMagico == None:
        return "null magico"
       return nodoMagico.lista.delbyvalue(name + "@" + dominio)