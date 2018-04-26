"""this function returns a list of lists of accounts in the file"""


def read_accounts():
    accounts_file = open('Accounts.txt', 'r')
    accounts_list = []
    for line in accounts_file:
        line = line.split()
        accounts_list.append(line)

    for account in accounts_list:
        print(account)

    return accounts_list

