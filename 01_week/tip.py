def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    new_text = d.replace("$", "")
    dollar_float = float(new_text)
    return dollar_float


def percent_to_float(p):
    new_text = p.replace("%", "")
    percent_float = float(new_text) / 100
    return percent_float


if __name__ == "__main__":
    main()
