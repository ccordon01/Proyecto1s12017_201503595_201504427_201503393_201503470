#First we need to import the graphviz module:

import graphviz as gv

#Now we can create the graph object g1 and add two nodes A and B as well as an edge to connect the two.
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
styles = {
    'graph': {
        'label': 'Lista',
        'fontsize': '16',
        'fontcolor': 'white',
        'bgcolor': '#333333',
        'rankdir': 'BT',
    },
    'nodes': {
        'fontname': 'Helvetica',
        'shape': 'doublecircle',
        'fontcolor': 'white',
        'color': 'white',
        'style': 'filled',
        'fillcolor': '#006699',
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
g1 = gv.Graph(format='png')
g1.node('1','1')
g1.node('2','1')
g1.edge('A', 'A')

#Let's have a look at the the dot code that this will generate behind the scenes:

print(g1.source)

"""graph {
    A
    B
        A -- B
}"""

#That looks about right. Now it's time to save the graph to disk:
g1 = apply_styles(g1, styles)
filename = g1.render(filename='img/lista')
print filename


