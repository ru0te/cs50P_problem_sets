def slow_down():
    user_input = input("Enter a phrase or sentence: ")
    new_input = user_input.replace(" ", "...")
    return new_input


def main():
    result = slow_down()
    print(result)


if __name__ == "__main__":
    main()
