def transform_user_input():
    user_input = input("Enter a word, phrase or sentence: ")
    input_indoor = user_input.lower()
    return input_indoor


def main():
    result = transform_user_input()
    print(result)


if __name__ == "__main__":
    main()
