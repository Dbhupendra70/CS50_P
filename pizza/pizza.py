import sys
import csv
from tabulate import tabulate

def count_LOC(filename):
    try:
        with open(filename, 'r') as file:
            f_pointer = csv.reader(file)
            for i in f_pointer:
               headers=i
               break

            item_list=[]
            for j in f_pointer:
                item_list.append(j)

        return tabulate(item_list, headers, tablefmt="grid")
    except FileNotFoundError:
        sys.exit(f"File does not exist")

def main():
    if len(sys.argv)> 2 :
            sys.exit("Too many command-line arguments")
    elif len(sys.argv)< 2:
            sys.exit("Too few command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith('.csv'):
        sys.exit("Not a CSV file")

    loc = count_LOC(filename)
    print(loc)

if __name__ == "__main__":
    main()
