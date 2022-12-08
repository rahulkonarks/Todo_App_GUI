FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Reads todos.txt file and returns the list of todos """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Writes todos to the todos.txt file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
