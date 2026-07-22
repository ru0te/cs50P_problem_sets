def deep():
    user_input = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? \n"
    )
    if user_input == str(42) or user_input == "forty-two" or user_input == "forty two":
        print("Result: Yes")
    else:
        print("No, the answer is 42")


def main():
    deep()


if __name__ == "__main__":
    main()
