import functions
import PySimpleGUI as Gui

label = Gui.Text('Type in a to-do')
input_box = Gui.InputText(tooltip='Enter a to-do', key='todo')
add_button = Gui.Button('Add', key='add')
list_box = Gui.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=(45, 10))
edit_button = Gui.Button('Edit', key='edit')

window = Gui.Window('My To-do app',
                    layout=[
                        [label],
                        [input_box, add_button],
                        [list_box, edit_button]
                    ],
                    font=('Helvetica', 12)
                    )
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case Gui.WIN_CLOSED | 'exit':
            break
window.close()
