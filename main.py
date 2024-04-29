import networkx as nx 
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

G = nx.Graph()
root = tk.Tk()
root.title("Algoritmo de búsqueda en Anchura y Profundidad")

source_node = None  # Variable para almacenar el nodo fuente

vertex_entry = tk.Entry(root)
vertex_entry.pack()

def add_vertex():
    global source_node
    vertex = vertex_entry.get()
    if vertex:
        G.add_node(vertex)
        vertex_entry.delete(0, tk.END)
        source_node = vertex  # Actualiza el nodo fuente
    else:
        print("Introduce un nombre de vértice válido.")

add_vertex_button = tk.Button(root, text="Agregar vértice", command=add_vertex)
add_vertex_button.pack()

edge_entry_1 = tk.Entry(root)
edge_entry_1.pack()
edge_entry_2 = tk.Entry(root)
edge_entry_2.pack()

def add_edge():
    global source_node
    source = edge_entry_1.get()
    target = edge_entry_2.get()
    if source and target:
        G.add_edge(source, target)
        edge_entry_1.delete(0, tk.END)
        edge_entry_2.delete(0, tk.END)
        source_node = source  # Actualiza el nodo fuente
    else:
        print("Introduce nodos válidos.")

add_edge_button = tk.Button(root, text="Agregar arista", command=add_edge)
add_edge_button.pack()

print_info_button = tk.Button(root, text="Info de datos agregados (consola)", command=lambda: print("Número de nodos:", G.number_of_nodes(), "\nNúmero de bordes:", G.number_of_edges()))
print_info_button.pack()

figure = Figure(figsize=(5, 5))
ax = figure.add_subplot(111)
canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().pack()

def draw_graph(search_edges=None, search_type='bfs'):
    ax.clear()
    pos = nx.spring_layout(G)
    nx.draw(G, pos=pos, ax=ax, with_labels=True)
    if search_edges:
        edge_color = 'r' if search_type == 'bfs' else 'g'
        nx.draw_networkx_edges(G, pos=pos, edgelist=search_edges, edge_color=edge_color, ax=ax)
        nx.draw_networkx_nodes(G, pos=pos, nodelist=[source_node] + [v for u, v in search_edges], node_color=edge_color, ax=ax)
    canvas.draw()

draw_button = tk.Button(root, text="Dibujar grafo", command=lambda: draw_graph())
draw_button.pack()

def show_bfs():
    bfs_edges = list(nx.bfs_edges(G, source=source_node))
    draw_graph(bfs_edges, 'bfs')

bfs_button = tk.Button(root, text="Búsqueda en anchura", command=show_bfs)
bfs_button.pack()

def show_dfs():
    dfs_edges = list(nx.dfs_edges(G, source=source_node))
    draw_graph(dfs_edges, 'dfs')

dfs_button = tk.Button(root, text="Búsqueda en profundidad", command=show_dfs)
dfs_button.pack()

root.mainloop()
