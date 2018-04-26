import read_file
"""show_history function: shows the process made to a certain account"""


def show_history(ls):
    # ls is the list contains account data

    choice = input('1) show deposit processes\n2) show withdraw processes\n3) show password'
                   'change process\n4) show all processes\n5) clear processes')

    file_name = str(ls[0]) + '.txt'
    id_list = read_file.read_file(file_name)

    if choice == 1: