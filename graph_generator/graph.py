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
        # Placeholder implementation for finding Euler cycle
        print("Euler cycle not implemented yet")

    def find_hamilton_cycle(self):
        # Placeholder implementation for finding Hamilton cycle
        print("Hamilton cycle not implemented yet")
