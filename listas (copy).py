import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('./')
#Importo la Clase
from nodos import Claseuno
from nodos import Clasedos
from lista import ClaseLista
from lista import ClaseListaDoble
from listaPila import ClaseListaPila
from listaCola import ClaseListaCola
from matrizDispersa import ClassMatriz

class listas(object):
	"""docstring for listas"""
	def __init__(self):
		#super(listas, self).__init__()
		#self.arg = arg
		self.lista = ClaseListaDoble()

	def insertarLista(self,parametro):
		self.lista.insertarAlFinal(parametro);

	def borrarLista(self,parametro):
		return self.lista.delbypos(parametro)

	def buscarLista(self,parametro):
		return self.lista.byvalue(parametro)