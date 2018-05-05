import time
from read_file import read_file


def gate_x(t_password):
    # Enter old password to confirm the new password
    wrong_flag = True  # True if end all tries wrong

    print("\nIf you want go back type \"Exit\"\n")
    for i in range(3):  # Limit the try to enter the password
        entered_password = input('\nEnter The Old Password : ')
        if entered_password == "Exit":  # Return the Exit flag
            return '-1'
        if entered_password == t_password:  # Compere if the Entered password = the True password
            wrong_flag = False  # Set to false mean the entered password confirmed
            break

    if wrong_flag:  # Return the wrong flag
        return '1'
    else:  # Return the true flag
        return '0'

    # Change password


def change_password(ls):
    # Get the old password
    old_password = ls[2]

    # Ask to old password to enter new one
    flag = gate_x(old_password)
    # Security flag get the output flag
    if flag == '0':
        new_password = input("\nEnter the new password: ")
        '''Get the new password'''
        file_name = ls[0] + '.txt'
        process_list = read_file(file_name)
        id_file = open(file_name, 'a')

        if len(process_list) == 0:  # if there are no processes in the file
            last_id = 1
        else:
            last_id = int(process_list[len(process_list) - 1][0]) + 1  # get last id and increment it

        id_file.write(
            '{0}\tchange_password\t\t{1}\t{2}\t{3}\n'.format(str(last_id), str(time.ctime()), old_password, str(new_password)))
        # write process id type before after
        id_file.close()

        # Check if Different is negative value
        ls[2] = new_password

        # Write the new password
    elif flag == '1':
        input("Out of range of try ... press Enter")
