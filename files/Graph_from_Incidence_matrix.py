import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def build_and_visualize_graph(incidence_matrix):
    """
    Функція, яка будує граф із заданої матриці інцидентності та візуалізує його.


    Параметри:
    - incidence_matrix: numpy.ndarray, матриця інцидентності графа.


    Повертає:
    - None
    """
    # Створення графа
    graph = nx.Graph()
    num_nodes, num_edges = incidence_matrix.shape


    # Додавання вершин до графа
    graph.add_nodes_from(range(num_nodes))


    # Додавання ребер та їх ваг
    for edge_index in range(num_edges):
        edge_nodes = np.where(incidence_matrix[:, edge_index] != 0)[0]
        if len(edge_nodes) == 2:
            graph.add_edge(edge_nodes[0], edge_nodes[1], weight=edge_index + 1)


    # Визначення позицій вершин для візуалізації
    pos = nx.spring_layout(graph)


    # Визуалізація графа
    nx.draw(graph, pos, with_labels=True, font_size=10, node_size=700, font_color='black', edge_color='gray')


    # Додавання ваг ребер
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_color='red')


    plt.title("Graph from Incidence Matrix")
    plt.show()


# Приклад використання функції з попередньо заданою матрицею інцидентності
example_incidence_matrix = np.array([
    [1, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1]
])


build_and_visualize_graph(example_incidence_matrix)