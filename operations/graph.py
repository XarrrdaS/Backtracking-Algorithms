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

    def is_connected(self):
        start = next((i for i in range(self.n) if self.adj_list[i]), None)
        if start is None:
            return True
        
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
