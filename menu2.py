import os

import withdraw
import deposit
import show_history

lls = [1, 1, 1, 1500]


def menu2():
    os.system('clear')
    print("\nWelcome ")
    ch = input("\n1) show balance \n2) show history\n3) deposit\n4) withdraw\n"
               "5) change password \n6) logout\n\nchoice>> ")

    if ch == 1:
        # query
        print("query()")
    elif ch == 2:
        # show_history()
        print("show_history()")
        ls = show_history.show_history(lls)
    elif ch == 3:
        # deposit()
        print("#deposit()")
        ls = deposit.deposit(lls)
    elif ch == 4:
        # withdraw()
        print("#withdraw()")
        ls = withdraw.withdraw(lls)
    elif ch == 5:
        # change_password()
        print("#change_pasword()")
    elif ch == 6:
        # logout()
        print("#logout()")
    else:
        print("ERROR: Wrong choice\n")
        menu2()

    menu2()


