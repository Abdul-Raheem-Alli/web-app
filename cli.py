from project.text import get_todos, write_todos
import time

age = time.strftime("%b %d, %Y %H:%M:%S")
print("it is ", age)
print("the time is below:")
while True:
    user_name = input("click show, add, complete, edit or exist")
    user_name = user_name.strip()

    if 'add' in user_name or 'new' in user_name or 'more' in user_name:
            todo = user_name[4:]

            todos = get_todos()

            todos.append(todo + '\n')

            write_todos(todos)

    elif user_name.startswith("show"):
            todos = get_todos()

            for index, items in enumerate(todos):

                row = f"{index+1}-{items}"

                print(row)
    elif user_name.startswith("complete"):
            name = int(user_name[9:])
            todos = get_todos()
            index = number - 1
            todos.pop(number - 1)
            write_todos( todos)

    elif user_name.startswith("edit"):
            number = int(user_name[5:])
            print(number)
            number = number - 1
            todos = get_todos()
            new_todo = input("enter new todo")
            todos[number] = new_todo
            write_todos( todos)

    elif user_name.startswith("exist"):
            break
    else:
        print("command is not valid")
print("bye")

