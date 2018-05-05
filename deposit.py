import time
import read_file

"""deposit function: receives a list of info of account, and returns the account info in a list"""


def deposit(ls):
    # ls is a list of the information of the account
    # ls elements are of type string
    # ls[0] id
    # ls[1] name
    # ls[2] password
    # ls[3] balance
    current_balance = int(ls[3])  # make changes to another variable to keep the previous balance
    # to print it later, then save ls[3] = current_balance
    print('Your current balance: ' + ls[3])
    deposit_amount = int(input('Enter deposit amount: '))

    current_balance += abs(deposit_amount)  # to guarantee the entered value

    file_name = ls[0] + '.txt'
    process_list = read_file.read_file(file_name)
    id_file = open(file_name, 'a')

    if len(process_list) == 0:  # if there are no processes in the file
        last_id = 1
    else:
        last_id = int(process_list[len(process_list) - 1][0]) + 1  # get last id and increment it

    id_file.write('{0}\tdeposit\t\t\t\t{1}\t{2}\t{3}\n'.format(str(last_id), str(time.ctime()), ls[3], str(current_balance)))
    # write->   process_id    process_name    process_date_and_time    before_process    after_process
    id_file.close()
    ls[3] = str(current_balance)
    print('Your current balance: ' + ls[3])

    return ls
