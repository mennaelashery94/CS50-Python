def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    question(answer)

def question(q):
    q = q.lower().strip()
    if q == "42" or q == "forty two" or q == "forty-two":
        print("Yes")
    else:
        print("No")
    return

main()
