def convert():
    user_input = input("Enter a word or phrase with an emoticon - :) or :( \n")
    new_input = user_input.replace(":)", "🙂").replace(":(", "🙁")
    return new_input


def main():
    result = convert()
    print(result)


if __name__ == "__main__":
    main()
