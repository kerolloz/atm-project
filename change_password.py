import time

from read_file import read_file


def GateX(TPassword):
    '''The true password'''
    # Enter old password to confirm the new password
    Wrongfag = True  # '''True if end all tries wrong'''
    Epassword = '' '''Curry try password'''

    print("\nIf you want go back type \"Exit\"\n")
    for i in range(3):  # '''Limit the try to enter the password'''
        Epassword = input('\nEnter The Old Password : ')
        if (Epassword == "Exit"):  # '''Return the Exit flag'''
            return '-1'
        if (Epassword == TPassword):  # '''Compere if the Entred password = the True password'''
            Wrongfag = False  # '''Set to false mean the entered password confirmed'''
            break

    if (Wrongfag):  # '''Return the wrong flag'''
        return '1'
    else:  # '''Return the true flage'''
        return '0'

    # Change password


def change_password(ls):
    # Get the old password
    old_password = ls[2]
    '''curry the old password'''

    # Ask to old password to enter new one
    fag = GateX(old_password)
    '''Security flag get the output flage'''
    if fag == '0':
        new_password = input("\nEntre the new password: ")
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
    elif fag == '1':
        '''Wrong massage'''
        input("Out of range of try ... press Enter")
