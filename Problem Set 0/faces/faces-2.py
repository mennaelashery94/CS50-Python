def main():
    sentence = input("Say something: ")
    print(convert(sentence))


def convert(emoji):
    
    return emoji.replace(":)", "🙂").replace(":(", "🙁")

main()  