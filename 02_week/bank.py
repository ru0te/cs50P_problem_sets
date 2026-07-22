def pay_user():
    user_input = input("Greeting: ")
    if user_input.startswith("hello"):
        print("$0")
    elif user_input[0] == "h":
        print("$20")
    else:
        print("$100")


def main():
    pay_user()


main()
