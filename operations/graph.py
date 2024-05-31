class Graph:
    def __init__(self, n):
        self.n = n
        self.adj_list = {i: [] for i in range(n)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def display(self):
        for node, neighbors in self.adj_list.items():
            print(f"{node}: {neighbors}")

    def find_euler_cycle(self):
        # Check if all vertices with non-zero degree are connected
        if not self.is_connected():
            print("Graph is not Eulerian")
            return
        
        # Check if all vertices have even degree
        if not all(len(neighbors) % 2 == 0 for neighbors in self.adj_list.values()):
            print("Graph is not Eulerian")
            return
        
        current_path = [0]  # Start from the first vertex
        cycle = []
        
        while current_path:
            current_vertex = current_path[-1]
            
            if self.adj_list[current_vertex]:
                next_vertex = self.adj_list[current_vertex].pop()
                self.adj_list[next_vertex].remove(current_vertex)
                current_path.append(next_vertex)
            else:
                cycle.append(current_path.pop())
        
        print("Euler cycle:", cycle)

    def find_hamilton_cycle(self):
        path = []
        
        def backtrack(vertex, visited):
            if len(path) == self.n:
                if path[0] in self.adj_list[vertex]:
                    path.append(path[0])
                    return True
                return False
            
            for neighbor in self.adj_list[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    path.append(neighbor)
                    
                    if backtrack(neighbor, visited):
                        return True
                    
                    visited[neighbor] = False
                    path.pop()
            
            return False
        
        visited = [False] * self.n
        path.append(0)
        visited[0] = True
        
        if backtrack(0, visited):
            print("Hamiltonian cycle:", path)
        else:
            print("No Hamiltonian cycle found")

    def is_connected(self):
        # Perform a BFS or DFS to check if all non-zero degree vertices are connected
        start = next((i for i in range(self.n) if self.adj_list[i]), None)
        if start is None:
            return True  # No edges in the graph
        
        visited = [False] * self.n
        stack = [start]
        
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                for neighbor in self.adj_list[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
        
        return all(visited[i] or not self.adj_list[i] for i in range(self.n))
