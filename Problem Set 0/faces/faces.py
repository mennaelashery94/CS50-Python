def main():
    phrase = input("say somthing: ")
    text = convert(phrase)
    print(text)



def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

main()
