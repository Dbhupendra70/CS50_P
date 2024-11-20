def main():
    fuel = input("Fraction: ")
    percentage = convert(fuel)
    print(gauge(percentage))

def convert(fraction):
    parts = fraction.split("/")
    if parts[0].isnumeric() and parts[1].isnumeric():
        numerator = int(parts[0])
        denominator = int(parts[1])
        if denominator == 0:
            raise ZeroDivisionError
        elif numerator > denominator:
            raise ValueError

        return round(numerator / denominator * 100)
    raise ValueError

def gauge(percentage):
    if 75 <= percentage <= 100:
        return "F"
    elif 0 <= percentage <= 25:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
