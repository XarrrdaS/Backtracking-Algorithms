def find_hamilton_cycle(graph):
    path = []

    def backtrack(vertex, visited):
        if len(path) == graph.n:
            if path[0] in graph.adj_list[vertex]:
                path.append(path[0])
                return True
            return False

        for neighbor in graph.adj_list[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                path.append(neighbor)

                if backtrack(neighbor, visited):
                    return True

                visited[neighbor] = False
                path.pop()

        return False

    visited = [False] * graph.n
    path.append(0)
    visited[0] = True

    if backtrack(0, visited):
        return path
    else:
        print("Graph is not Hamiltonian")
        return None
