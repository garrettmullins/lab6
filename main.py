def encode(password):
    encoded_password = ""
    for i in range(len(password)):
        encoded_num = str((int(password[i]) +3) % 10)
        encoded_password = encoded_password + str(encoded_num)
    return encoded_password

if __name__ == "__main__":
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option = int(input("Please enter an option:"))
        if option == 1:
            password = (input("Please enter your password to encode:"))
            altered_password = encode(password)
            print("Your password has been encoded and stored!")
            print()
        if option == 2:
            print(altered_password)
        if option == 3:
            exit()


