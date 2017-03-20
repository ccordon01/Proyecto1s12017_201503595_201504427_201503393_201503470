from ArbolAVL import Arbol

AVL = Arbol()
#----------------------INSERTAR------------------------
""" 
como para comprobar si estaba ingresando bien en el arbol de nombre puse los numero pero de id envio sus cadenas alfanumericas 
que cada una corresponde ordenada mente a cada numero, solo para que cuando me imprimiera yo verificara con la pagina AVL ONLINE si 
se estaba ordenando bien.
		1 A65A19E23Q104A4
        5 I47D83A17J22T27
        6 M37O51P10E35H10
        10 O80Y12E13J14J89
        13 T15R44J98W78R50
        16 T67Y18A94O17H37
        17 Y17O56J40W72U65

"""
#------- ESTRUCTURA DE ENTRADA -> AVL.Insertar(nombre,descripcion,id)--------
AVL.Insertar("1","bonitos zapatos","A65A19E23Q104A4")
AVL.Insertar("5","bonitos blusas","I47D83A17J22T27")
AVL.Insertar("6","bonits blusas","M37O51P10E35H10")
AVL.Insertar("10","bonitos zapatos","O80Y12E13J14J89")
AVL.Insertar("13","bonitos blusas","T15R44J98W78R50")
AVL.Insertar("16","bonits blusas","T67Y18A94O17H37")
AVL.Insertar("17","bonits blusas","Y17O56J40W72U65")


#----------------------BUSCAR Y MODIFICAR DESCRIPCION---------------
AVL.Modificar("M37O51P10E35H10","Esto es una modificios")

#----------------------ELMINIAR----------------------




#-----------------------RECORRIDOS----------------

#print("----------------INORDEN--------------------")
#AVL.inOrden(AVL.obtenerRaiz())
print("----------------PREORDEN---------------------")
AVL.preOrden(AVL.obtenerRaiz())
#print("----------------POSTORDEN--------------------")
#AVL.postOrden(AVL.obtenerRaiz())



