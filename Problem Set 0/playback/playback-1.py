def main():
    phrase = input("Say something: ")
    print(modify(phrase))

def modify(phrase):
    phrase = phrase.split()
    return "...".join(phrase)

main()
