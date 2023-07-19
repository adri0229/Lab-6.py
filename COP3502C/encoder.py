# adriana mendoza
def encode(password):
    encoded_password = ""
    for num in password:
        num_int = int(num)
        num_encoded = (num_int + 3) % 10
        encoded_password += str(num_encoded)
    return encoded_password


def decode(password):
    decoded_password = ""
    for num in password:
        num = int(num)
        if 3 <= num <= 9:
            decoded_password += str(num - 3)
        else:
            decoded_password += str(num + 7)
    return decoded_password


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
        elif option == "2":
            decoded_password = decode(encode_password)
            print(f'The encoded password is {encode_password}, and the original password is {decoded_password}.')
        elif option == "3":
            print("Menu closed.")
            break


if __name__ == "__main__":
    main()
