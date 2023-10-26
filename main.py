"""
Lab 6
Authors: Arin Sareddy and Shan Sundal
Class: COP3502C
Section: 22282
Description: Github encode decode lab
"""


# coded by Arin
# iterates through string and adds three to each number and then returns string
def encoder(password_input):
    string_result = ''
    for i in password_input:
        result = 0
        result = int(i) + 3
        string_result += str(result)
    return string_result


# coded by Shan
def decoder(password_input):
    pass


# displays a menu based on user input
def main():
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode\n2. Decode\n3. Quit')
        user_input = int(input('Please enter an option: '))
        # encodes and stores password
        if user_input == 1:
            password_input = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!')
            encoded_password = encoder(password_input)
        if user_input == 2:
            decoded_password = decoder(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')
        if user_input == 3:
            break


if __name__ == '__main__':
    main()