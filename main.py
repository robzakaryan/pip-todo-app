# from functions import get_todos, write_todos
import functions
import time

now = time.strftime('%d %b, %Y %H:%M:%S')
print(f'It is {now}')
while True:
    user_action = input('Type add, show, edit, complete or exit: ').strip()
    if user_action.startswith('add') or user_action.startswith('new'):
        todos = functions.get_todos()
        todo = user_action[4:] + '\n'
        todos.append(todo)
        functions.write_todos(todos)
    elif user_action.startswith('show') or user_action.startswith('display'):
        todos = functions.get_todos()
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{index + 1}.{item}')
    elif user_action.startswith('complete'):
        try:
            todos = functions.get_todos()
            index = int(user_action[9:])
            index = index - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos)
            message = f'Todo {todo_to_remove} was removed from the list'
            print(message)
        except ValueError:
            print('Your command is not valid, please provide number after complete')
            continue
        except IndexError:
            print('There is no item with that number')
            continue
    elif user_action.startswith('edit'):
        try:
            todos = functions.get_todos()
            number = int(user_action[5:])
            number = number - 1
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'
            functions.write_todos(todos)
        except ValueError:
            print('Your command is not valid, please provide number after edit')
            continue
        except IndexError:
            print('There is no item with that number')
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print('You entered a wrong contract')
print('Bye!')

