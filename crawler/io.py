import os


def load_users_list_from_file(path='./users'):
    # the file must exist
    if not os.path.isfile(path):
        print('File does not exist')
        return False, []

    # get full path of file
    file_abs_path = os.path.abspath(path)

    # open file to read its content
    with open(file_abs_path) as f:
        lines = f.readlines()

    users_list = [l.strip() for l in lines]

    return True, users_list
