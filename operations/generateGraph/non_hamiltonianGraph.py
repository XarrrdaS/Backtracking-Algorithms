from ..graph import Graph
import random

def generate_non_hamiltonian_graph(n):
    if n <= 10:
        raise ValueError("Number of vertices must be greater than 10")

    graph = Graph(n)
    
    # Graph generation with 50% saturation - as in task
    edges_needed = int(n * (n - 1) / 2 * 0.5)
    while edges_needed > 0:
        u, v = random.sample(range(n), 2)
        if v not in graph.adj_list[u]:
            graph.add_edge(u, v)
            edges_needed -= 1

    # Isolating one vertex
    isolated_node = random.choice(range(n))
    graph.adj_list[isolated_node] = []
    for node in range(n):
        if isolated_node in graph.adj_list[node]:
            graph.adj_list[node].remove(isolated_node)

    return graph
