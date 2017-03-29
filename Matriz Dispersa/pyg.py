#!/usr/bin/env python
import pygraphviz as pgv
  
A=pgv.AGraph(directed=True,strict=True,rankdir='LR',splines='ortho',shape = 'record')
# add some edges
A.node_attr['shape']='box'
A.add_node(1,label = "hola")
A.add_edge(1,2)
A.add_edge(2,"hola")
A.add_edge(1,4)
A.add_edge(4,5)
A.add_edge(2,6)
A.add_edge(4,6)
#A.add_edge(3,7)
#A.add_edge(6,7)
A.add_edge(3,8)
A.add_edge(5,8)
# make a subgraph with rank='same'
B=A.add_subgraph([1,2,3],name='s1',rank='same')
B.graph_attr['rank']='same'
B=A.add_subgraph([1,4,5],name='sm',rankdir='LR')
B.graph_attr['rankdir']='LR'
B=A.add_subgraph([4,6,7],name='s2',rank='same')
B.graph_attr['rank']='same'
B=A.add_subgraph([5,8],name='s3',rank='same')
B.graph_attr['rank']='same'
print A.string() # print dot file to standard output
A.draw('example.png', prog='dot')