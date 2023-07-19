# adriana mendoza
def encode(password):
    encoded_password = ""
    for num in password:
        num_int = int(num)
        num_encoded = (num_int + 3) % 10
        encoded_password += str(num_encoded)
    return encoded_password


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")
        if option == "1":
            password = input("Please enter your password to encode: ")
            encode_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == "3":
            print("Menu closed.")
            break


if __name__ == "__main__":
    main()
