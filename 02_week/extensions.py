def get_media_type():
    user_input = input("File name: ")
    file_ext = user_input.split(".")[1]
    if file_ext in ("gif", "jpg", "jpeg", "png"):
        print(f"image/{file_ext}")
    elif file_ext in ("pdf", "zip"):
        print(f"application/{file_ext}")
    elif file_ext == "txt":
        print("text/plain")


def main():
    get_media_type()


main()
