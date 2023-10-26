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
        result = int(i) + 3
        string_result += str(result)
    return string_result


# coded by Shan
def decoder(password_input):
    # this function will take in the encoded password and subtract 3 from each number
    # to decode the password, the decoded password is returned as a string
    res = []
    for i in password_input:
        result = str(int(i) - 3)
        res.append(result)
    return "".join(res)


# The main function will run the program
def main():
    while True:
        # this while loop keeps the program running until the user selects option 0 to quit
        print('Menu')
        print('-------------')
        print('1. Encode\n2. Decode\n3. Quit')
        print()
        # asks the user to select an option
        user_input = int(input('Please enter an option: '))

        if user_input == 1:
            # This will as the user to input their password
            password_input = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!')
            print()
            # this will encode the password and store the encoded password in the variable encoded_password
            encoded_password = encoder(password_input)
        if user_input == 2:
            # this will take the encoded password and decode it and store the value in the variable decoded_password
            decoded_password = decoder(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')
            print()
        if user_input == 3:
            # this goes out of the while loop to end the program when the user selects option 3
            break


if __name__ == '__main__':
    main()