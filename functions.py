FILEPATH = 'todos.txt'


def get_todos(filepath: str = FILEPATH):
    """ Returns todos from the given text file """
    with open(filepath, 'r') as todos_file:
        todos_from_file = todos_file.readlines()
    return todos_from_file


def write_todos(todos_to_write: list, filepath: str = FILEPATH):
    """ Writes todos in the given text file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_to_write)


if __name__ == '__main__':
    """ will be executed only if we run functions.py directly """
    print('Hello')
    print(get_todos())
