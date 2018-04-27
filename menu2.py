import os
import withdraw
import deposit
import show_history


def clear_screen():  # function to clear the output of the screen
    os.system('clear')


def menu2(account):
    # account is a list of account info
    # account[0] id
    # account[1] name
    # account[2] password
    # account[3] balance

    print("\n---------Hello, {0}--------- ".format(account[1]))
    ch = int(input("\n1) show balance \n2) show history\n3) deposit\n4) withdraw\n"
                   "5) change password \n6) logout\n\nchoice>> "))

    if ch == 1:
        clear_screen()
        print("ID: {}\nName: {}\nBalance: {}\n".format(account[0], account[1], account[3]))
    elif ch == 2:
        clear_screen()
        show_history.show_history(account)
    elif ch == 3:
        clear_screen()
        print("#deposit()")
        deposit.deposit(account)
    elif ch == 4:
        clear_screen()
        print("#withdraw()")
        withdraw.withdraw(account)
    elif ch == 5:
        clear_screen()
        print("#change_pasword()")
    elif ch == 6:
        clear_screen()
        return account
    else:
        clear_screen()
        print("ERROR: Wrong choice\n")
        menu2(account)

    menu2(account)
