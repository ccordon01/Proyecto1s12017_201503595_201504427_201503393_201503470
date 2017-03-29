from NodoArbolAVL import NodoArbol
from nodoAvl import nodoAvl

a=[]
dra = ""
class Arbol():
     def __init__(self):
          self.raiz = None

     def obtenerRaiz(self):
          return self.raiz

     #BUSCAR
     def buscar(self, d, r):
          if self.raiz == None:
               return None
          elif r.id == d:
               return r
          elif r.id < d:
               return self.buscar(d, r.hderecho)
          elif r == None:
               return     None
          else:
               return self.buscar(d, r.hizquierdo)
                    
     #Modificar
     def Modificar(self, codigo,descrip):
          retornado = self.buscar(codigo,self.raiz)
          if retornado == None:
               print ("No se encontro el nodo")
          else:
               retornado.descripcion = descrip     
               print("Modificacion con Exito")      

     #OBTENER FE
     def ObtenerFE(self, x):
          if x == None:
               return -1
          else:
               return x.fe     
     
     #OBTENER NUMERO MAXIMO
     def Maxi(self, a , b):
          if a>b:
               return a
          elif b>a:
               return b
          else:
               return a


     #ROTACION SIMPLE IZ
     def rotacionDE(self, c):
          aux = c.hizquierdo
          c.hizquierdo = aux.hderecho
          aux.hderecho = c
          c.fe = self.Maxi(self.ObtenerFE(c.hizquierdo), self.ObtenerFE(c.hderecho)) + 1
          aux.fe = self.Maxi(self.ObtenerFE(aux.hizquierdo), self.ObtenerFE(aux.hderecho)) + 1
          return aux

     #ROTACION SIMPLE DE
     def rotacionIZ(self, c):
          aux = c.hderecho
          c.hderecho = aux.hizquierdo
          aux.hizquierdo = c
          c.fe = self.Maxi(self.ObtenerFE(c.hizquierdo), self.ObtenerFE(c.hderecho)) + 1
          aux.fe = self.Maxi(self.ObtenerFE(aux.hizquierdo), self.ObtenerFE(aux.hderecho)) + 1
          return aux

          #ROTACION DOBLE IZ

     #ROTACION DOBLE DE
     def rotacionDDE(self, c):
          c.hizquierdo = self.rotacionDE(c.hizquierdo)
          temp = self.rotacionIZ(c)
          return temp

     #ROTACION DOBLE DI
     def rotacionDIZ(self, c):
          c.hderecho = self.rotacionIZ(c.hderecho)
          temp = self.rotacionDE(c)
          return temp

          #INSERTAR


     #INSERTAR AVL
     def insertarAVL(self, nuevo, subAr):
          nuevoPadre = subAr


          #Agarro por la izquierda
          if nuevo.id < subAr.id:
               #Si en la iquierda no hay nada se inserta a la izquierda
               if subAr.hizquierdo == None:
                    subAr.hizquierdo = nuevo
               #Si a la izquierda si hay algo
               else:
                    #envio el hijo izquierdo como nueva raiz (recursivo)
                    subAr.hizquierdo = self.insertarAVL(nuevo, subAr.hizquierdo)
                    #Comparo si esta desiquilibrado
                    if (self.ObtenerFE(subAr.hizquierdo) - self.ObtenerFE(subAr.hderecho) == 2):
                         if nuevo.id < subAr.hizquierdo.id:
                              nuevoPadre = self.rotacionDE(subAr)
                         else:
                              nuevoPadre      = self.rotacionDDE(subAr)



          #Agarro por la deecha
          elif nuevo.id > subAr.id:
               if subAr.hderecho == None:
                    subAr.hderecho = nuevo
               else:
                    subAr.hderecho = self.insertarAVL(nuevo, subAr.hderecho)
                    if (self.ObtenerFE(subAr.hderecho) - self.ObtenerFE(subAr.hizquierdo) == 2):
                         if nuevo.id > subAr.hderecho.id:
                              nuevoPadre = self.rotacionIZ(subAr)
                         else:
                              nuevoPadre = self.rotacionDIZ(subAr)

          else:
               print("NODO DUPLICADO")

          #ACTUALIZANDO LA ALTURA
          if (subAr.hizquierdo == None) and (subAr.hderecho != None):
               subAr.fe = subAr.hderecho.fe + 1
          elif (subAr.hderecho == None) and (subAr.hizquierdo != None):
               subAr.fe = subAr.hizquierdo.fe + 1
          else:
               subAr.fe = self.Maxi(self.ObtenerFE(subAr.hizquierdo), self.ObtenerFE(subAr.hderecho)) + 1
          return nuevoPadre

     #METODO INSERTAR
     def Insertar(self, n,d,i):
          nuevo = NodoArbol(n,d,i)
          if self.raiz == None:
               self.raiz = nuevo
          else:
               self.raiz = self.insertarAVL(nuevo, self.raiz)

     #RECORRIDOS
     def inOrden(self, r):
          if r != None:
               self.inOrden(r.hizquierdo)
               print("ID: "+r.id +" NOMBRE: "+ r.nombre + " DESCRIPCION: "+ r.descripcion)
               self.inOrden(r.hderecho)

     def preOrden(self, r):
          if r != None:
               employee = nodoAvl(r.nombre,r.descripcion,r.id)
               if r.dias == 0:
                     a.append(employee)
                     print "add"
                     print("ID: "+r.id +" NOMBRE: "+ r.nombre + " DESCRIPCION: "+ r.descripcion)
               self.preOrden(r.hizquierdo)
               self.preOrden(r.hderecho)

     def postOrden(self, r):
          if r != None:
               self.postOrden(r.hizquierdo)
               self.postOrden(r.hderecho)
               print("ID: "+r.id +" NOMBRE: " +r.nombre + " DESCRIPCION: "+ r.descripcion)

     #ELIMINAR
     def Eliminar(self, codigo):
          retornado = self.buscar(codigo)

     def getAll(self):
          del a[:]
          self.preOrden(self.raiz)
          print len(a)
          return a

     def buscaR(self,us,idp,dias, r):
          if r != None:
             if r.id == idp:
                  r.user = us
                  r.dias = dias
                  dra = "Renta Realizada Con Exito"
                  print dra
             else:
                  self.buscaR(us,idp,dias,r.hderecho)
                  self.buscaR(us,idp,dias,r.hizquierdo)


     def devolverR(self,idp,r):
          if r != None:
             if r.id == idp:
                  r.user = ""
                  r.dias = 0
                  print "Devolucion Realizada Con Exito"
                  dra = "Devolucion Realizada Con Exito"
             else:
                     self.devolverR(idp,r.hderecho)
                     self.devolverR(idp,r.hizquierdo)


