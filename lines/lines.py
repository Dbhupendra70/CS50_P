import sys

def count_LOC(filename):
    try:
        with open(filename, 'r') as file:
            lines_of_code = 0
            for line in file:
                stripped_line = line.lstrip()
                if stripped_line and not stripped_line.startswith('#'):
                    lines_of_code += 1
        return lines_of_code
    except FileNotFoundError:
        sys.exit(f"File does not exist")

def main():
    if len(sys.argv)> 2 :
            sys.exit("Too many command-line arguments")
    elif len(sys.argv)< 2:
            sys.exit("Too few command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith('.py'):
        sys.exit("Not a python file")

    loc = count_LOC(filename)
    print(loc)

if __name__ == "__main__":
    main()
