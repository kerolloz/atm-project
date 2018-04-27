from login import login
from create_account import create_account
from read_file import read_file
from menu2 import clear_screen
import os

accounts_list = read_file('Accounts.txt')


def menu1():
    print('>>>>>>>>WELCOME<<<<<<<<\n')
    choice = int(input('1) Login\n2) Create Account\n3) Exit\n\nchoice>> '))
    if choice == 1:
        clear_screen()
        login(accounts_list)
    elif choice == 2:
        create_account(accounts_list)
    elif choice == 3:
        exit(0)  # we didn't save changes here
    else:
        print("ERROR: Wrong choice\n")
        menu1()
    # os.system('clear')
    menu1()


if __name__ == '__main__':
    menu1()
