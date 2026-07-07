def main():
    question = input("What time is it? ")
    time, format = convert(question)
    print(check(time, format))

def convert(time):

    if time.endswith(("a.m", "p.m")):
        t, format = time.split()
        hours, mins = t.split(":")
        return int(hours) + (int(mins) / 60), format

    else:
        hours, mins = time.split(":")
        return int(hours) + (int(mins) / 60), None




def check(t, f):

    match f:
        case "a.m":
            if 7 <= t <= 8:
                return f"breakfast time"
            else:
                return

        case "p.m":
            t = t - 12
            if 0 <= t <= 1:
                return f"lunch time"
            elif 6 <= t <= 7:
                return f"dinner time"
        case None:
             if 7 <= t <= 8:
                 return f"breakfast time"

             elif 12 <= t <= 13:
                return f"lunch time"

             elif 18 <= t <= 19:
                return f"dinner time"

        case _:
            return f"Enter correct time"


if __name__ == "__main__":
    main()
