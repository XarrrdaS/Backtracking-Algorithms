from operations.generateGraph.hamiltonianGraph import generate_hamiltonian_graph
from operations.generateGraph.non_hamiltonianGraph import generate_non_hamiltonian_graph
from operations.findCycle.euler import find_euler_cycle
from operations.findCycle.hamilton import find_hamilton_cycle

def main():
    while True:
        mode = input(">>> ")

        if mode == '--hamilton':
            n = int(input("nodes> "))
            saturation = int(input("saturation> "))
            graph = generate_hamiltonian_graph(n, saturation)
            break
        elif mode == '--non-hamilton':
            n = int(input("nodes> "))
            graph = generate_non_hamiltonian_graph(n)
            break
        else:
            print("Invalid argument. Use --hamilton or --non-hamilton\n")
    
    print("\nGenerated Graph:")
    graph.display()
    print("\nEulerian Cycle:")
    euler_cycle = find_euler_cycle(graph)
    if euler_cycle:
        print(euler_cycle)
    print("\nHamiltonian Cycle:")
    hamilton_cycle = find_hamilton_cycle(graph)
    if hamilton_cycle:
        print(hamilton_cycle)

if __name__ == "__main__":
    main()
