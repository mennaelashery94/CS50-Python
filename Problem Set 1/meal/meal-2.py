def main():
    question = input("What time is it? ")
    time = convert(question)
    print(check(time))

def convert(time):
    hours, mins = time.split(":")
    return int(hours) + (int(mins) / 60)

def check(t):

    if 7<= t <= 8:
        return f"breakfast time"
    elif 12 <= t <= 13:
        return f"lunch time"
    elif 18 <= t <= 19:
        return f"dinner time"
    else:
        return f""



if __name__ == "__main__":
    main()
