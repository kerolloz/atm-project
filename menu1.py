from login import login
from create_account import create_account
from read_file import read_file
from menu2 import clear_screen

accounts_list = read_file('Accounts.txt')


def menu1():
    print('>>>>>>>>WELCOME<<<<<<<<\n')
    choice = int(input('1) Login\n2) Create Account\n3) Exit\n\nchoice>> '))
    if choice == 1:
        clear_screen()
        try:
            # to enable the option of (ctrl+c) to go back
            login(accounts_list)
        except KeyboardInterrupt:
            clear_screen()
    elif choice == 2:
        create_account(accounts_list)
    elif choice == 3:
        # close the program
        exit(0)
    else:
        clear_screen()
        print("ERROR: Wrong choice\n")
    
    menu1()


if __name__ == '__main__':
    menu1()
