import csv
import sys

def after(before, after_file):
    try:
        # Open the input file in read mode
        with open(before, 'r') as file:
            reader = csv.DictReader(file)

            # Open the output file in write mode
            with open(after_file, 'w', newline="") as af:
                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(af, fieldnames=fieldnames)

                # Write the header
                writer.writeheader()

                # Write rows to the new CSV
                for row in reader:
                    # Split the 'name' field into 'last' and 'first'
                    last, first = row['name'].split(',')
                    # Write the new row to the output file
                    writer.writerow({'first': first.strip(), 'last': last.strip(), 'house': row['house']})

    except FileNotFoundError:
        sys.exit(f"Could not read {before}")

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    # Call the after function with the input and output filenames
    after(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
