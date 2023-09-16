def get_todos(filepath="todos.txt"):
    """Read the text file and return the list of to do items."""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath="todos.txt",):
    """Write the todo items in the text file """
    with open(filepath, 'w') as file:
         file.writelines(todos_arg)
if __name__ == "__main__":
    print
    print(get_todos())
