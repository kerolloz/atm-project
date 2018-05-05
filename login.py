from menu2 import clear_screen, menu2


def login(acc_list):

    login_id = input('Please, Enter your info(press "Ctrl+C" to go back) \n>>ID: ')
    login_password = input('>>Password: ')
    found = False
    for account in acc_list:
        if account[0] == login_id and account[2] == login_password:
            found = True
            clear_screen()
            menu2(account)
            break
        else:
            continue

    if not found:
        clear_screen()
        print('Wrong ID or Password')
        login(acc_list)

    else:
        acc_file = open('Accounts.txt', 'w')
        print('Saving changes...')
        # after logging out of the account
        # write changes to accounts.txt file
        for acc in acc_list:
            for elements in acc:
                acc_file.write("%s\t" % elements)
            acc_file.write('\n')
