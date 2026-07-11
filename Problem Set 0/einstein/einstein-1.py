def main():
    mass = int(input("m: "))
    print(f"E: {calc(mass)}")

def calc(m):
    return m * pow(300000000, 2)

main()
