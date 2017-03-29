__author__ = "cech"

import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('./')
#Importo la Clase
from nodos import Claseuno
from flask import Flask, request, Response,jsonify,json
from nodoAvl import nodoAvl
import names
from matrizDispersa import ClassMatriz
app = Flask("EDD_Grupo7")
matrizD = ClassMatriz()


@app.route('/login',methods=['POST']) 
def helloLogin():
     user = str(request.form['user'])
     passw = str(request.form['pass'])
     depto = str(request.form['depto'])
     emp = str(request.form['emp'])
     return matrizD.login(str(depto),str(emp),str(user),str(passw))

@app.route('/simulacion') 
def helloSimulacion():
     print matrizD.insertarCorreo("Seguros","EmpresaA")
     print matrizD.insertarCorreo("Ventas","EmpresaB")
     print matrizD.insertarCorreo("Atencion","EmpresaB")
     print matrizD.insertarCorreo("Atencion","EmpresaC")
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
     print "----------------------------------------------------------"
     print matrizD.insertarAvl("Atencion","EmpresaB","panqueque","1","bonitos zapatos","A65A19E23Q104A4")
     print matrizD.insertarAvl("Atencion","EmpresaB","panqueque","5","bonitos blusas","I47D83A17J22T27")
     print matrizD.insertarAvl("Seguros","EmpresaA","carlos","1","bonitos zapatos","A65A19E23Q104A4")
     print matrizD.insertarAvl("Seguros","EmpresaA","carlos","5","bonitos blusas","I47D83A17J22T27")
     print "----------------------------------------------------------"
     print matrizD.mostrarAvlG()
     return "Datos Cargados"

@app.route('/json',methods=['POST']) 
def helloJson():
    jsonStr = None
    try:

        # Initialize a employee list
        avlList = []

        # create a instances for filling up employee list
        for i in range(0,5):
            employee = nodoAvl(names.get_first_name(),names.get_last_name(),str(i))
            avlList.append(employee)
        print "hola"
    # convert to json data
        jsonStr = json.dumps([e.toJSON() for e in avlList])
        #return jsonStr
        print jsonStr
    except:
        print "error ", sys.exc_info()[0]

    return jsonStr
    
@app.route('/activos',methods=['POST']) 
def helloActivos():
     return matrizD.mostrarAvlG()

































@app.route('/metodoWeb',methods=['POST']) 
def hello():
     parametro = str(request.form['dato'])
     dato2 = str(request.form['dato2'])
     return "Hola " + str(parametro) + "!"
@app.route('/metodoWeb1',methods=['POST']) 
def helloq():
     return "Hola mundo !"

@app.route('/python') 
def hellop():
     return matrizD.login("Seguros","EmpresaA","carlos",str(12345))

@app.route("/e")
def hellof():
     return "Hello World :)!"
#if __name__ == "__main__":
app.run(debug=True, host='192.168.1.237')
#app.run(debug=True)
#app.run(debug=True, host='192.168.43.99')
#################################/
#                               #/
#   Carlos Eduardo Cordon Hdez  #/
#                               #/
#          201504427            #/
#                               #/
#################################/