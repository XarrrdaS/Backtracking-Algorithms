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
