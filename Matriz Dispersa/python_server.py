__author__ = "cech"

import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('./')
#Importo la Clase
from nodos import Claseuno
from flask import Flask, request, Response
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
     print "------------------------"
     return "Datos Cargados"



































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

#################################/
#                               #/
#   Carlos Eduardo Cordon Hdez  #/
#                               #/
#          201504427            #/
#                               #/
#################################/