graph {
	graph [bgcolor="#333333" fontcolor=white fontsize=16 label="Practica 2" nodesep=.05 rankdir=BT splines=line]
	node [color=white fillcolor="#006699" fontcolor=white fontname=Helvetica nodesep=.05 shape=doublecircle style=filled]
	edge [arrowhead=open color=white fontcolor=white fontname=Courier fontsize=12 style=dashed]
		0 [label="tecla@gmail.com"]
}