"""returns a list of lists lines in the file - each line in a list all stored in one list"""


def read_file(file_name):
    opened_file = open(file_name, 'r')
    lines_list = []
    for line in opened_file:
        line = line.split()
        lines_list.append(line)

    return lines_list
