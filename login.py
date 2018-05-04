from menu2 import clear_screen, menu2


def login(acc_list):

    login_id = input('Please, Enter your info\n>>ID: ')
    login_password = input('>>Password: ')
    found = True
    for account in acc_list:
        if account[0] == login_id and account[2] == login_password:
            found = False
            break
        else:
            continue

    if found:
        clear_screen()
        print('Wrong ID or Password')
        login(acc_list)

    else:
        print("*** Name and Password are correct <3 *** \n")
        menu2(account)

        acc_file = open('Accounts.txt', 'w')
        print('Saving changes...')

        # after logging out of the account
        # write changes to accounts.txt file

        for acc in acc_list:
            for elements in acc:
                acc_file.write("%s\t" % elements)
            acc_file.write('\n')


