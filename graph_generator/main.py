def main():
    while True:
        mode = input(">>> ")

        if mode == '--hamilton':
            n = int(input("nodes> "))
            saturation = int(input("saturation> "))
            return True
        elif mode == '--non-hamilton':
            n = int(input("nodes> "))
            return True
        else:
            print("Invalid argument. Use --hamilton or --non-hamilton\n")
            continue

if __name__ == "__main__":
    main()
