import networkx as nx 
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class GraphVisualizationApp:
    def __init__(self):
        self.graph = nx.Graph()
        self.root = tk.Tk()
        self.root.title("Algoritmo de búsqueda en Anchura y Profundidad")
        self.source_vertex = None
        
        self.setup_gui()
        
    def setup_gui(self):
        self.vertex_entry = tk.Entry(self.root)
        self.vertex_entry.pack()

        self.add_vertex_button = tk.Button(self.root, text="Agregar vértice", command=self.add_vertex)
        self.add_vertex_button.pack()

        self.edge_entry_1 = tk.Entry(self.root)
        self.edge_entry_1.pack()
        self.edge_entry_2 = tk.Entry(self.root)
        self.edge_entry_2.pack()

        self.add_edge_button = tk.Button(self.root, text="Agregar arista", command=self.add_edge)
        self.add_edge_button.pack()

        self.print_info_button = tk.Button(self.root, text="Info de datos agregados (consola)", command=self.print_info)
        self.print_info_button.pack()

        self.figure = Figure(figsize=(5, 5))
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, self.root)
        self.canvas.get_tk_widget().pack()

        self.draw_button = tk.Button(self.root, text="Dibujar grafo", command=self.draw_graph)
        self.draw_button.pack()

        self.bfs_button = tk.Button(self.root, text="Búsqueda en anchura", command=self.show_bfs)
        self.bfs_button.pack()

        self.dfs_button = tk.Button(self.root, text="Búsqueda en profundidad", command=self.show_dfs)
        self.dfs_button.pack()
        
    def add_vertex(self):
        vertex = self.vertex_entry.get()
        if vertex:
            self.graph.add_node(vertex)
            self.vertex_entry.delete(0, tk.END)
            self.source_vertex = vertex
        else:
            print("Introduce un nombre de vértice válido.")
        
    def add_edge(self):
        source = self.edge_entry_1.get()
        target = self.edge_entry_2.get()
        if source and target:
            self.graph.add_edge(source, target)
            self.edge_entry_1.delete(0, tk.END)
            self.edge_entry_2.delete(0, tk.END)
            self.source_vertex = source
        else:
            print("Introduce nodos válidos.")
        
    def print_info(self):
        print("Número de nodos:", self.graph.number_of_nodes())
        print("Número de bordes:", self.graph.number_of_edges())
        
    def draw_graph(self):
        self.ax.clear()
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos=pos, ax=self.ax, with_labels=True)
        self.canvas.draw()
        
    def show_bfs(self):
        if self.source_vertex:
            bfs_edges = list(nx.bfs_edges(self.graph, source=self.source_vertex))
            self.draw_graph_with_edges(bfs_edges, 'bfs')
        else:
            print("No se ha seleccionado un nodo fuente.")
        
    def show_dfs(self):
        if self.source_vertex:
            dfs_edges = list(nx.dfs_edges(self.graph, source=self.source_vertex))
            self.draw_graph_with_edges(dfs_edges, 'dfs')
        else:
            print("No se ha seleccionado un nodo fuente.")
        
    def draw_graph_with_edges(self, edges, search_type):
        self.ax.clear()
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos=pos, ax=self.ax, with_labels=True)
        if edges:
            edge_color = 'r' if search_type == 'bfs' else 'g'
            nx.draw_networkx_edges(self.graph, pos=pos, edgelist=edges, edge_color=edge_color, ax=self.ax)
            nx.draw_networkx_nodes(self.graph, pos=pos, nodelist=[self.source_vertex] + [v for u, v in edges], node_color=edge_color, ax=self.ax)
        self.canvas.draw()
        
    def run(self):
        self.root.mainloop()

app = GraphVisualizationApp()
app.run()
