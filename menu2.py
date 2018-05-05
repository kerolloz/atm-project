import os
import withdraw
import deposit
import show_history
import change_password


def clear_screen():
    # function to clear the output of the screen
    os.system('clear')
    print()  # print blank line after clearing the screen


def menu2(account):
    # account is a list of account info
    # account[0] id
    # account[1] name
    # account[2] password
    # account[3] balance

    print("\n---------Hello, {0}--------- ".format(account[1]))
    ch = int(input("\n1) show info \n2) show process history\n3) deposit\n4) withdraw\n"
                   "5) change password \n6) logout\n\nchoice>> "))

    clear_screen()
    if ch == 1:
        print("ID: {}\nName: {}\nBalance: {}\n".format(account[0], account[1], account[3]))
    elif ch == 2:
        show_history.show_history(account)
    elif ch == 3:
        deposit.deposit(account)
    elif ch == 4:
        withdraw.withdraw(account)
    elif ch == 5:
        change_password.change_password(account)
    elif ch == 6:
        return
        # logout - go back to menu1
    else:
        print("ERROR: Wrong choice\n")

    menu2(account)
