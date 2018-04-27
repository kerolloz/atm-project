# create Accounts.txt if not exist

try:
    # read the 'Accounts.txt' file
    f = open('Accounts.txt', 'r')
    f.close()
except FileNotFoundError:
    # if 'Accounts.txt' file is not found, create it
    f = open('Accounts.txt', 'w')
    f.close()


import menu1
import os

os.system('clear')
menu1.menu1()
