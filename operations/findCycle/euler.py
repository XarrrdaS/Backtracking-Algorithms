def find_euler_cycle(graph):
    if not graph.is_connected():
        print("Graph is not Eulerian")
        return None
    
    if not all(len(neighbors) % 2 == 0 for neighbors in graph.adj_list.values()):
        print("Graph is not Eulerian")
        return None
    
    current_path = [0]
    cycle = []
    
    while current_path:
        current_vertex = current_path[-1]
        
        if graph.adj_list[current_vertex]:
            next_vertex = graph.adj_list[current_vertex].pop()
            graph.adj_list[next_vertex].remove(current_vertex)
            current_path.append(next_vertex)
        else:
            cycle.append(current_path.pop())
    
    return cycle
