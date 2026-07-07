def main():
    greet = input("Greeting: ")
    print(reply(greet))

def reply(r):
    r = r.lower().strip()
    if r.startswith('h'):
        return f"$20"
    elif r.startswith('hello'):
        return f"$0"
    else:
        return f"$100"

main()

