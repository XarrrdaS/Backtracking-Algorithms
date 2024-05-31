from operations.generateGraph.hamiltonianGraph import generate_hamiltonian_graph
from operations.generateGraph.non_hamiltonianGraph import generate_non_hamiltonian_graph
from operations.findCycle.euler import find_euler_cycle
from operations.findCycle.hamilton import find_hamilton_cycle
from operations.exportTikz.exportToTikz import export_to_tikz

def main():
    while True:
        options_menu_before = """\nAvailable actions:\n
            -h, --hamilton
                   Generate Hamiltonian graph
            -n, --non-hamilton
                   Generate non-Hamiltonian graph
            -H, --help
                     Display help
            -x, --exit
                     Exit the program"""
        print(options_menu_before)

        while True:
            mode = input("\n>>> ")

            if mode in ('-h', '--hamilton'):
                while True:
                    try:
                        n = int(input("nodes> "))
                        if n <= 10:
                            print("Number of nodes must be greater than 10\n")
                        else:
                            break
                    except ValueError:
                        print("Please enter a valid integer\n")

                while True:
                    try:
                        saturation = int(input("saturation> "))
                        if saturation < 0 or saturation > 100:
                            print("Saturation must be between 0 and 100\n")
                        else:
                            break
                    except ValueError:
                        print("Please enter a valid integer\n")

                graph = generate_hamiltonian_graph(n, saturation)
                break

            elif mode in ('-n', '--non-hamilton'):
                while True:
                    try:
                        n = int(input("nodes> "))
                        if n <= 10:
                            print("Number of nodes must be greater than 10\n")
                        else:
                            break
                    except ValueError:
                        print("Please enter a valid integer\n")

                graph = generate_non_hamiltonian_graph(n)
                break

            elif mode in ('--help', '-H'):
                print(options_menu_before)

            elif mode in ('--exit', '-x'):
                return

            else:
                print("Invalid argument. For more informations use '-H' or '--help'\n")

        options_menu_after = """\nAvailable actions:\n
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
        
        print(options_menu_after)
        while True:
            action = input(">>> ")

            if action in ('--display', '-d'):
                print("\nGenerated graph in the adjacency list:")
                graph.display()

            elif action in ('--tikz', '-t'):
                print("\nName your TeX file")
                filename = input("filename> ")
                export_to_tikz(graph, f'{filename}.tex')

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

            elif action in ('--help', '-H'):
                print(options_menu_after)

            elif action in ('--back', '-b'):
                break

            elif action in ('--exit', '-x'):
                return

if __name__ == "__main__":
    main()
