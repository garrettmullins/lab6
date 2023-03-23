# Garrett Mullins's Encoder
def encode(password):
    encoded_password = ""
    for i in range(len(password)):
        encoded_num = str((int(password[i]) +3) % 10)
        encoded_password = encoded_password + str(encoded_num)
    return encoded_password
# encoding function added 3 to each digit of password
def decode(encoded_password):
    decoded_password = ""
    for char in encoded_password:
        decoded_char = str(int(char) - 3)
        decoded_password += decoded_char
    return decoded_password

if __name__ == "__main__":
    # while loop for menu
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option = int(input("Please enter an option:"))
        # prompt for option 1
        if option == 1:
            password = (input("Please enter your password to encode:"))
            altered_password = encode(password)
            print("Your password has been encoded and stored!")
            print()
        if option == 2:
            decoded_password = decode(altered_password)
            print(f'The encoded password is {altered_password}, and the original password is {decoded_password}.\n')
        if option == 3:
            exit()


