def main():
    answer = input("What is the the Answer to the Great Question of Life, the Universe, and Everything? ")
    question(answer)


def question(q):
    q = q.lower().strip()
    match q :
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

main()
