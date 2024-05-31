def main():
    mode = input(">>> ")

    if mode == '--hamilton':
        n = int(input("nodes> "))
        saturation = int(input("saturation> "))
    elif mode == '--non-hamilton':
        n = int(input("nodes> "))
    else:
        print("Invalid argument. Use --hamilton or --non-hamilton")
        return

if __name__ == "__main__":
    main()
