def convert(time):
    time_list = tuple(time.split(":"))
    hour, minutes = time_list
    new_hour = float(hour)
    new_minutes = float(minutes) / 60
    result = new_hour + new_minutes
    return result


def main():
    time = convert(input("What time is it: "))
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")
    else:
        print("Not time")


if __name__ == "__main__":
    main()
