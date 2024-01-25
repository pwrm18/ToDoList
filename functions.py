def write_todos(writing, filepath="todos.txt"):
    '''Writes up your todos in a file (todos.txt by default)'''
    with open(filepath, 'w') as file:
        file.writelines(writing)

def read_todos(filepath="todos.txt"):
    '''Gets your todos in a list'''
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos