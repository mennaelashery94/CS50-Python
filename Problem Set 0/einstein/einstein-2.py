def main():
    mass = input("m: ")
    print(f"E: {einstein(mass)}")

def einstein(m):
    c = 300000000 
    return int(m) * (c ** 2) 

main()