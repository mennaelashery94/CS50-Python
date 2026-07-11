def main():
    sentence = input("Say something: ")
    print(slow(sentence))


def slow(phrase):

    return phrase.replace(" ", "...")

main()

