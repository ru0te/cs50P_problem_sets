def convert_to_snake_case(str):
    new_list = []
    for letter in str:
        if letter.isupper():
            letter = "_" + letter.lower()
        new_list.append(letter)
    result = "".join(new_list)
    return result


def main():
    user_input = convert_to_snake_case(input("Enter word in camelCase: "))
    print(f"snake_case: {user_input}")


if __name__ == "__main__":
    main()
