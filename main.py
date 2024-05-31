from operations.generateGraph.hamiltonianGraph import generate_hamiltonian_graph
from operations.generateGraph.non_hamiltonianGraph import generate_non_hamiltonian_graph
from operations.findCycle.euler import find_euler_cycle
from operations.findCycle.hamilton import find_hamilton_cycle
from operations.exportTikz.exportToTikz import export_to_tikz

def main():
    while True:
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

        options_menu = """\nAvailable actions:\n
        -d, --display
               Display graph in the adjacency list
        -t, --tikz
               Export graph to TikZ
        -e, --euler
               Check if there is Eulerian cycle
        -h, --hamilton
               Check if there is Hamiltonian cycle
        -H, --help
               Display help
        -b, --back
               Generate graph again
        -x, --exit
               Exit the program"""
        
        print(options_menu)
        while True:
            action = input(">>> ")

            if action in ('--display', '-d'):
                print("\nGenerated graph in the adjacency list:")
                graph.display()
            elif action in ('--tikz', '-t'):
                export_to_tikz(graph)
            elif action in ('--euler', '-e'):
                print("\nEulerian Cycle:")
                euler_cycle = find_euler_cycle(graph.copy())
                if euler_cycle:
                    print(euler_cycle)
            elif action in ('--hamilton', '-h'):
                print("\nHamiltonian Cycle:")
                hamilton_cycle = find_hamilton_cycle(graph.copy())
                if hamilton_cycle:
                    print(hamilton_cycle)
                else:
                    print("Graph is not Hamiltonian")
            elif action in ('--help', '-H'):
                print(options_menu)
            elif action in ('--back', '-b'):
                break
            elif action in ('--exit', '-x'):
                return

if __name__ == "__main__":
    main()
