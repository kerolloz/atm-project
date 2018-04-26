"""returns a list of lines in the file"""


def read_file(file_name):
    opened_file = open(file_name, 'r')
    lines_list = []
    for line in opened_file:
        line = line.split()
        lines_list.append(line)

    '''for account in accounts_list:
        print(account)'''

    return lines_list

