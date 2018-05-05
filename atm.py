# create Accounts.txt if not exist

try:
    # read the 'Accounts.txt' file
    # if you try to open non existing file in read mode, this will throw an error
    f = open('Accounts.txt', 'r')
    f.close()
except FileNotFoundError:
    # if 'Accounts.txt' file is not found, create it
    f = open('Accounts.txt', 'w')
    f.close()

# import modules
import menu1
import os

os.system('clear')
menu1.menu1()  # start the program - call menu1() function
