def shorten_word(text):
    text_list = []
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    for letter in text:
        if letter in vowels:
            letter = ""
        text_list.append(letter)
    return "".join(text_list)


def main():
    text = shorten_word(input("Input: "))
    print(f"Output: {text}")


if __name__ == "__main__":
    main()
