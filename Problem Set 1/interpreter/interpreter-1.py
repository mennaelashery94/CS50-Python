def main():
    eq = input("Expression: ")
    calc(eq)

def calc(exp):
    exp = exp.strip()
    x,y,z = exp.split()
    x = float(x)
    z = float(z)
    match y:
        case "+":
            print(x + z)
        case "-":
            print(x - z)
        case "*":
            print(x * z)

        case "/" if z == 0:
            print("undefined")

        case "/":
            print(x / z)

        case _:
            print("Enter valid Expression")

    return
main()

