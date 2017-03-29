__author__ = "Carlangas"

#Si mientras trabajan en Python alguna vez les arroja un "IndentationError" es porque en alguna linea, los tabs al inicio de la sentencia estan erroneos, por ejemplo:
#Esto es valido:
#class Usuario():
#    def __init__(self, nombre):
#        self.nombre = nombre
#        self.password = password
#Esto NO es valido y arroja un "IndentationError":
#class Usuario():
#    def __init__(self, nombre):
#        self.nombre = nombre
#       self.password = password
#       ^
#       Esto no deberia de estar ahi, sino que tiene que estar igual de indentado que las demas sentencias.
#
#
#Recomiendo Sublime Text como IDE
#


import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('./')
#Importo la Clase
#from nodos import Claseuno
from flask import Flask, request, Response
from nodos import Claseuno
from nodos import Clasedos
from lista import ClaseLista
from lista import ClaseListaDoble
from listaPila import ClaseListaPila
from listaCola import ClaseListaCola
from matrizDispersa import ClassMatriz
app = Flask("Practica 2")
lista = ClaseListaDoble()
pila = ClaseListaPila()
cola = ClaseListaCola()
matriz = ClassMatriz()
import graphviz as gv
import pygraphviz as pgv
test = ClaseLista()
listaPos = ClaseLista()
test2 = ClaseListaDoble()
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
    filename = g1.render(filename='imgen/'+name)
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
    filename = g1.render(filename='imgen/'+name)
    print filename
def graficarMatriz(l,name):
    A=pgv.AGraph(directed=True,strict=True,rankdir='LR',splines='ortho',shape = 'record')
# add some edges
    A.node_attr['shape']='box'
    A.add_node(0,label = "M. D.")
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
    while (actual != None):
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
    #g1.edge('A', 'A')
    #print(g1.source)
    #g1 = apply_styles(g1, styles)
    #filename = g1.render(filename='img/'+name)
    print A.string() # print dot file to standard output
    A.draw('imgen/'+name+'.png', prog='dot')
@app.route('/prueba',methods=['POST']) 
def h1i():
    #return "hola"
    parametro = str(request.form['dato'])
    ##self.lista.insertarAlFinal(parametro);
    return "Se inicio correctamente " + str(parametro) + "!"
@app.route('/insertarLista',methods=['POST']) 
def h1():
    parametro = str(request.form['dato'])
    lista.insertarAlFinal(str(parametro))
    graficarLista(lista,'Lista')
    return "Se inserto correctamente " + str(parametro) + "!"
@app.route('/borrarLista',methods=['POST']) 
def h11():
    parametro = str(request.form['dato'])
    print "borrar "+parametro
    lista.mostrar()
    valor = lista.delbypos(parametro)
    graficarLista(lista,'Lista')
    if valor is "null":
        return "No se encontro dato"
    return "Se elimino correctamente " + str(valor) + "!"
@app.route('/buscarLista',methods=['POST']) 
def h111():
    parametro = str(request.form['dato'])
    valor = lista.byvalue(parametro)
    if valor == "null":
        return "No se encontro dato"
    return "Se encontro correctamente en pos: " + str(valor) + "!"
@app.route('/insertarMatriz',methods=['POST']) 
def h14():
    parametro = str(request.form['dato'])
    dato = str(request.form['dato2'])
    print matriz.insertarCorreo(parametro,dato)
    print matriz.insertarDatos(parametro,dato)
    print "--Inicio Cabecera Letras--"
    matriz.mostrarCabeceraLetras()
    print "--Inicio Cabecera Dominios--"
    matriz.mostrarCabeceraDominios()
    graficarMatriz(matriz,'MatrizD')
    return "Se inserto correctamente " + str(parametro) +"@"+ str(dato)+ "!"
@app.route('/borrarMatriz',methods=['POST']) 
def h114():
    parametro = str(request.form['dato'])
    print "borrar "+parametro
    parametro = str(request.form['dato'])
    dato = str(request.form['dato2'])
    valor = matriz.borrarDatos(parametro,dato)
    graficarMatriz(matriz,'MatrizD')
    if valor is "null":
        return "No se encontro dato"
    return "Se elimino correctamente " + str(valor) + "!"
@app.route('/buscarMatrizL',methods=['POST']) 
def h1114():
    parametro = str(request.form['dato'])
    valor = matriz.findbyl(str(parametro))
    if valor == "null":
        return "No se encontro dato"
    return str(valor)
@app.route('/buscarMatrizD',methods=['POST']) 
def h11145():
    parametro = str(request.form['dato'])
    valor = matriz.findbyd(str(parametro))
    if valor == "null":
        return "No se encontro dato"
    return str(valor)
@app.route('/insertarPila',methods=['POST']) 
def h12():
    parametro = str(request.form['dato'])
    pila.push(parametro);
    graficarListaE(pila,'Pila')
    return "Se inserto correctamente " + str(parametro) + "!"
@app.route('/borrarPila',methods=['POST']) 
def h112():
    #parametro = str(request.form['dato'])
    valor = pila.pop()
    graficarListaE(pila,'Pila')
    return "Se elimino correctamente " + str(valor) + "!"
@app.route('/insertarCola',methods=['POST']) 
def h13():
    parametro = str(request.form['dato'])
    cola.enqueue(parametro);
    graficarListaE(cola,'Cola')
    return "Se inserto correctamente " + str(parametro) + "!"
@app.route('/borrarCola',methods=['POST']) 
def h113():
    #parametro = str(request.form['dato'])
    valor = cola.dequeue()
    graficarListaE(cola,'Cola')
    return "Se elimino correctamente " + str(valor) + "!"
@app.route('/metodoWeb',methods=['POST']) 
def hello():
    parametro = str(request.form['dato'])
    dato2 = str(request.form['dato2'])
    return "Hola " + str(parametro) + "!"
@app.route('/metodoWeb1',methods=['POST']) 
def helloq():
    return "Hola mundo !"

@app.route("/e")
def hellof():
    return "Hello World2!"
def function():
    pass
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')

#################################/
#                               #/
#   Carlos Eduardo Cordon Hdez  #/
#                               #/
#          201504427            #/
#                               #/
#################################/