import os
import withdraw
import deposit
import show_history


def clear_screen():  # function to clear the output of the screen
    os.system('clear')


lls = [1, 1, 1, 1500]


def menu2():
    print("\n---------Welcome--------- ")
    ch = input("\n1) show balance \n2) show history\n3) deposit\n4) withdraw\n"
               "5) change password \n6) logout\n\nchoice>> ")

    if ch == 1:
        clear_screen()
        print("query()")
    elif ch == 2:
        clear_screen()
        print("show_history()")
        ls = show_history.show_history(lls)
    elif ch == 3:
        clear_screen()
        print("#deposit()")
        ls = deposit.deposit(lls)
    elif ch == 4:
        clear_screen()
        print("#withdraw()")
        ls = withdraw.withdraw(lls)
    elif ch == 5:
        clear_screen()
        print("#change_pasword()")
    elif ch == 6:
        clear_screen()
        print("#logout()")
    else:
        clear_screen()
        print("ERROR: Wrong choice\n")
        menu2()

    menu2()


if __name__ == '__main__':
    menu2()
