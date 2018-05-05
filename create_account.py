import os


def create_account(ls):
    # ls is a list of lists of lines in accounts file
    # ls is the accounts_list

    os.system('clear')
    account_name = input('Enter Your Name (WITHOUT SPACES): ')
    account_password = input('Enter Your Password (WITHOUT SPACES): ')

    print("Creating Your Account .....")
    accounts_file = open('Accounts.txt', 'a')

    if len(ls) == 0:
        new_last_id = 1
    else:
        new_last_id = int(ls[len(ls) - 1][0]) + 1

    line = '{0}\t{1}\t{2}\t0\n'.format(str(new_last_id), account_name, account_password)

    accounts_file.write(line)
    id_file_name = str(new_last_id) + '.txt'
    id_file = open(id_file_name, 'w')

    print("Your Account Has Been Created And Your Id Is " + str(new_last_id))
    id_file.close()
    accounts_file.close()
    ls.append([str(new_last_id), account_name, account_password, '0'])
