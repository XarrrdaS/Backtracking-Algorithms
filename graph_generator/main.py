from hamilton import generate_hamiltonian_graph

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
            break
        else:
            print("Invalid argument. Use --hamilton or --non-hamilton\n")
    
    print("\nGenerated Graph:")
    graph.display()
    print("\nEuler Cycle:")
    graph.find_euler_cycle()
    print("\nHamiltonian Cycle:")
    graph.find_hamilton_cycle()

if __name__ == "__main__":
    main()
