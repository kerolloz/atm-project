from menu2 import clear_screen, menu2


def login(acc_list):
    clear_screen()
    login_id = input('Please, Enter your info\n>>ID: ')
    login_password = input('>>Password: ')
    found = False
    for account in acc_list:
        if account[0] == login_id and account[2] == login_password:
            menu2(account)
            found = True
            break

    acc_file = open('Accounts.txt', 'w')
    print('saving changes')
    for acc in acc_list:
        for elements in acc:
            acc_file.write("%s\t" % elements)

    if not found:
        print('Wrong ID or Password')
        login(acc_list)
