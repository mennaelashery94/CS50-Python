def main():
    expression = input("Expression: ")
    print(calc(expression))


def calc(eq):
    x, y, z = eq.split()
    x = float(x)
    z = float(z)

    match y:
        case "+":
            return float(x + z)

        case "/":
            if z != 0:
                return float(x / z)

        case "*":
            return float(x * z)

        case "-":
            return float(x - z)

        case _:
            return f"Enter valid Expression"


main()
