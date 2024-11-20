while True:
    try:
        fuel = input("Fraction: ")
        fraction = fuel.split("/")

        # Ensure both parts of the fraction are numeric
        if fraction[0].isnumeric() and fraction[1].isnumeric():
            numerator = int(fraction[0])
            denominator = int(fraction[1])

            # Ensure denominator is not zero and valid fraction
            if denominator != 0 and numerator <= denominator:
                percentage = round(numerator / denominator * 100)

                if 75 < percentage <= 100:
                    print("F")
                elif 0 <= percentage < 25:
                    print("E")
                else:
                    print(f"{percentage}%")
                break
    except (ValueError, ZeroDivisionError):
        pass
