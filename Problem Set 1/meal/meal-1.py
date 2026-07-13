def main():
    ask = input("What time is it? ")
    time =  convert(ask)
    if 8 >= time >=7:
        print("breakfast time")
    elif 13 >= time >= 12:
        print("lunch time")
    elif 19 >= time >= 18:
        print("dinner time")
    return


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes  = int(minutes) / 60
    clock = round(float(hours + minutes), 2)

    return clock


if __name__ == "__main__":
    main()
