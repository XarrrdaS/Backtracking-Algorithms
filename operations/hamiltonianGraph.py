from .graph import Graph
import random

def generate_hamiltonian_graph(n, saturation):
    if n <= 10:
        raise ValueError("Number of vertices must be greater than 10")

    graph = Graph(n)
    
    # Hamiltonian cycle generation
    vertices = list(range(n))
    random.shuffle(vertices)
    for i in range(n):
        graph.add_edge(vertices[i], vertices[(i + 1) % n])
    
    # Adding additional edges according to saturation
    edges_needed = int(n * (n - 1) / 2 * (saturation / 100)) - n
    while edges_needed > 0:
        u, v = random.sample(range(n), 2)
        if v not in graph.adj_list[u]:
            graph.add_edge(u, v)
            edges_needed -= 1

    # Makes sure that each vertex has an even degree
    for node in range(n):
        if len(graph.adj_list[node]) % 2 != 0:
            for neighbor in range(n):
                if neighbor != node and neighbor not in graph.adj_list[node]:
                    graph.add_edge(node, neighbor)
                    break

    return graph
