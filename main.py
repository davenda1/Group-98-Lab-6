# Diego Avendano
def encoder(password):
    encoded_password  = ''
    for number in password:
        number = int(number)
        new_num = str((number + 3) % 10)
        encoded_password += new_num
    return encoded_password

if __name__ == '__main__':
    menu = True
    
    while menu:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
    
        print('Please enter an option: ', end='')
        user_choice = int(input())
        if user_choice == 1:
            print('Please enter your password to encode: ', end='')
            user_password = str(input())
            encoded_password = encoder(user_password)
            print('Your password has been encoded and stored!')
        elif user_choice == 2:
            # original_password = decoder(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is ')
        elif user_choice == 3:
            exit()
