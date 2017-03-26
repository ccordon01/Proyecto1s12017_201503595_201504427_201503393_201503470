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
import graphviz as gv
import pygraphviz as pgv
styles = {
    'graph': {
        'label': 'Practica 2',
        'fontsize': '16',
        'fontcolor': 'white',
        'bgcolor': '#333333',
        'nodesep' : '.05',
        'rankdir': 'BT',
        'splines' : 'line'
    },
    'nodes': {
        'fontname': 'Helvetica',
        'shape': 'doublecircle',
        'fontcolor': 'white',
        'color': 'white',
        'style': 'filled',
        'fillcolor': '#006699',
        'nodesep' : '.05',
    },
    'edges': {
        'style': 'dashed',
        'color': 'white',
        'arrowhead': 'open',
        'fontname': 'Courier',
        'fontsize': '12',
        'fontcolor': 'white',
    }
}
class ClassDD(object):
	"""docstring for ClassName"""
	def __init__(self, datos,nodo):
     	 self.datos = datos
     	 self.nodo = nodo
def pos(correo):
	#actual = nsM.nodoSiguiente
         actual = listaPos.primerNodo
         while (actual != None):
	 	 	if actual.datos.datos == correo:
	 	 		return actual.datos.nodo
	 	 	actual = actual.nodo
def apply_styles(graph, styles):
    graph.graph_attr.update(
        ('graph' in styles and styles['graph']) or {}
    )
    graph.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {}
    )
    graph.edge_attr.update(
        ('edges' in styles and styles['edges']) or {}
    )
    return graph
def graficarLista(l,name):
    g1 = gv.Graph(format='png')
    actual = l.primerNodo
    contador = 0
    aux = 0
    while (actual != None):
            g1.node(str(contador),actual.datos)
              #print "Dato: " + actual.datos
            contador = contador + 1
            aux = aux + 1
            actual = actual.nodoSiguiente
    print "Fin Crear Nodos " + str(contador)
    contador = 0
    actual = l.primerNodo
    while (actual != None):
    	    tmp = contador + 1
    	    if not tmp==aux:
    	      g1.edge(str(aux-contador-1),str(aux-tmp-1))
              #print "Dato: " + actual.datos
            contador = contador + 1
            actual = actual.nodoSiguiente
    print "Fin Crear Enlaces " + str(contador)
    #g1.edge('A', 'A')
    print(g1.source)
    g1 = apply_styles(g1, styles)
    filename = g1.render(filename='img/'+name)
    print filename
def graficarListaE(l,name):
    g1 = gv.Graph(format='png')
    actual = l.primerNodo
    contador = 0
    aux = 0
    while (actual != None):
            g1.node(str(contador),actual.datos)
              #print "Dato: " + actual.datos
            contador = contador + 1
            aux = aux + 1
            actual = actual.nodo
    print "Fin Crear Nodos " + str(contador)
    contador = 0
    actual = l.primerNodo
    while (actual != None):
    	    tmp = contador + 1
    	    if not tmp==aux:
    	      g1.edge(str(aux-contador-1),str(aux-tmp-1))
              #print "Dato: " + actual.datos
            contador = contador + 1
            actual = actual.nodo
    print "Fin Crear Enlaces " + str(contador)
    #g1.edge('A', 'A')
    print(g1.source)
    g1 = apply_styles(g1, styles)
    filename = g1.render(filename='img/'+name)
    print filename
def graficarMatriz(l,name):
    A=pgv.AGraph(directed=True,strict=True,rankdir='LR',splines='ortho',shape = 'record')
# add some edges
    A.node_attr['shape']='box'
    A.add_node(0,label = "")
    B=A.add_subgraph([0],name='s1',rank='same')
    B.graph_attr['rank']='same'
    actual = l.primerNodo.nodoInferior
    contador = 1
    aux = 1
    tmpstring ="<n> prueba"
    while (actual != None):
            A.add_node(str(contador),label = actual.datos)
            #tmpstring = tmpstring +' | '+ actual.datos 
              #print "Dato: " + actual.datos
            contador = contador + 1
            aux = aux + 1
            actual = actual.nodoInferior
    print "Fin Crear Nodos " + str(contador)
    contador = 1
    #aux = aux + 1
    actual = l.primerNodo.nodoInferior
    while (actual != None):
            tmp = contador + 1
            if not tmp==(aux):
              A.add_edge(contador,tmp)
              B=A.add_subgraph([str(contador)],name='s1',rank='same')
              B.graph_attr['rank']='same'
              print "Dato: " + actual.datos
            contador = contador + 1
            actual = actual.nodoInferior
    print "Fin Crear Enlaces " + str(contador)
    A.add_edge(0,1)
    A.add_edge(0,contador)
    B=A.add_subgraph([str(contador - 1)],name='s1',rank='same')
    B.graph_attr['rank']='same'
    actual = l.primerNodo.nodoSiguiente
    contadorAux = contador
    #aux = 1
    tmpstring ="<n> prueba"
    while (actual != None):
            A.add_node(str(contador),label = actual.datos)
            #tmpstring = tmpstring +' | '+ actual.datos 
              #print "Dato: " + actual.datos
            contador = contador + 1
            aux = aux + 1
            actual = actual.nodoSiguiente
    print "Fin Crear Nodos Dominios" + str(contador)
    print contadorAux
    contador = contadorAux
    #aux = aux + 1
    actual = l.primerNodo.nodoSiguiente
    while (actual != None):
            tmp = contador + 1
            if not tmp==(aux):
              A.add_edge(contador,tmp)
              B=A.add_subgraph([str(contador)],name='sm',rankdir='LR')
              B.graph_attr['rankdir']='LR'
              print "Dato: " + actual.datos
            contador = contador + 1
            actual = actual.nodoSiguiente
    print "Fin Crear Enlaces " + str(contador)
    B=A.add_subgraph([str(contador-1)],name='sm',rankdir='LR')
    B.graph_attr['rankdir']='LR'
    contadorN = contador
    contador = contadorAux
    actual = l.primerNodo.nodoSiguiente
    n=1
    """while (actual != None):
            tmp = contador 
            print str(tmp) + "=" + str(aux)
            if not tmp==(aux):
              print "entro"
              A.add_edge(contador,contadorN)
              n = n+1
              B=A.add_subgraph([str(contador)],name='s'+str(n),rank='same')
              B.graph_attr['rank']='same'
              actuala = actual.nodoInferior
              if actuala == None:
                print "pise"
              text = ""
              repetir=0
              contadorNAux =contadorN
              while (actuala != None):
                    print "Creando: " + actuala.datos.letra+"-"+actuala.datos.correo
                    datoPos = ClassDD(actuala.datos.letra+"-"+actuala.datos.correo,contadorN)
                    listaPos.insertarAlFinal(datoPos)
                    graficarLista(actuala.datos.lista,actuala.datos.letra+"-"+actuala.datos.correo)
                    A.add_node(str(contadorN),label = actuala.datos.letra+"-"+actuala.datos.correo)
               #return text
                    repetir = 1 + repetir
                    contadorN = contadorN + 1
                    actuala = actuala.nodoInferior
              #return text                           
              #print "Dato: " + actual.datos
              for x in xrange(1,repetir):
                 A.add_edge(contadorNAux,contadorNAux + 1)
                 B=A.add_subgraph([str(contadorNAux)],name='s'+str(n),rank='same')
                 B.graph_attr['rank']='same'
                 contadorNAux = contadorNAux + 1
            tmp = contador + 1
            B=A.add_subgraph([str(contadorNAux)],name='s'+str(n),rank='same')
            B.graph_attr['rank']='same'
            contador = contador + 1
            actual = actual.nodoSiguiente
    print "Fin Crear Enlaces Valor Nodo " + str(contador)
    contador = 1
    #aux = aux + 1
    actual = l.primerNodo.nodoInferior
    while (actual != None):
                 actualm = actual.nodoSiguiente
                 anterior = contador
                 while (actualm != None):
                         print "se esta haciendo " + actualm.datos.letra+"-"+actualm.datos.correo
                         valPos = pos(actualm.datos.letra+"-"+actualm.datos.correo)
                         #if not actualm.nodoSiguiente== None:
                            #print "entro"
                         A.add_edge(anterior,valPos)
                         anterior = valPos
                         actualm = actualm.nodoSiguiente
                 contador = contador + 1
                 actual = actual.nodoInferior
    """
    #g1.edge('A', 'A')
    #print(g1.source)
    #g1 = apply_styles(g1, styles)
    #filename = g1.render(filename='img/'+name)
    print A.string() # print dot file to standard output
    A.draw('img/'+name+'.png', prog='dot')

print "--Inicio Matriz Dispersa--"
matrizD = ClassMatriz()
print matrizD.insertarCorreo("Seguros","EmpresaA")
print matrizD.insertarCorreo("Ventas","EmpresaB")
print matrizD.insertarCorreo("Atencion","EmpresaB")
print matrizD.insertarCorreo("Atencion","EmpresaC")

graficarMatriz(matrizD,'MatrizD')
print "--Insertar Usuarios--"
print matrizD.insertarDatos("Seguros","EmpresaA","carlos",12345)
print "------------------------"
print matrizD.insertarDatos("Ventas","EmpresaB","chino",12345)
print "------------------------"
print matrizD.insertarDatos("Atencion","EmpresaC","claus",12345)
print "------------------------"
print matrizD.insertarDatos("Seguros","EmpresaA","juanpa",12345)
print "------------------------"
print matrizD.insertarDatos("Atencion","EmpresaB","panqueque",12345)
print "------------------------"
"""
print matrizD.insertarDatos("carlos","hotmail")
print matrizD.insertarDatos("diego","hotmail")
print matrizD.insertarCorreo("cech","hotmail")
print matrizD.insertarDatos("cech","hotmail")
print matrizD.insertarCorreo("fech","fotmail")
print matrizD.insertarDatos("fech","fotmail")
print matrizD.insertarCorreo("fech","hotmail")
print matrizD.insertarDatos("fech","hotmail")
print matrizD.insertarCorreo("rech","rotmail")
print matrizD.insertarDatos("rech","rotmail")
print matrizD.insertarCorreo("cech","rotmail")
print matrizD.insertarDatos("cech","rotmail")
print matrizD.insertarCorreo("yech","yotmail")
print matrizD.insertarDatos("yech","yotmail")
print matrizD.insertarCorreo("rech","fotmail")
print matrizD.insertarDatos("rech","fotmail")
print matrizD.insertarCorreo("rech","gmail")
print matrizD.insertarDatos("rech","gmail")
print matrizD.insertarCorreo("rech","hotmail")
print matrizD.insertarDatos("rech","hotmail")
"""
print "--Inicio Cabecera Letras--"
matrizD.mostrarCabeceraLetras()
print "--Inicio Cabecera Dominios--"
matrizD.mostrarCabeceraDominios()
print "--Inicio Cabecera Dominios Busqueda--"
print matrizD.findbyd("EmpresaB")
print "--Inicio Cabecera Letras Busqueda--"
print matrizD.findbyl("Atencion")
print "--Inicio Login--"
print matrizD.login("Seguros","EmpresaA","carlos",12345)
print matrizD.login("Atencion","EmpresaB","panqueque",12345)

"""
graficarMatriz(matrizD,'MatrizD')
print "--Inicio Cabecera Dominios--"
matrizD.mostrarCabeceraDominios()
print "--Inicio Cabecera Letras--"
print matrizD.findbyl("c")
print "--Inicio Cabecera Dominios--"
print matrizD.findbyd("hotmail")
print matrizD.borrarDatos("carlos","hotmail")
print "--Inicio Cabecera Letras--"
print matrizD.findbyl("c")
print "--Inicio Cabecera Dominios--"
print matrizD.findbyd("hotmail")
"""
#print "Hola Mundo"
#hi= "hi"
#print hi[1]
#print len(hi)
#print len(".")
#Claseuno();
#Clasedos();
