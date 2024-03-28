import functions
import PySimpleGUI as Gui
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

Gui.theme('BlueMono')
label_clock = Gui.Text('', key='clock')
label = Gui.Text('Type in a to-do')
input_box = Gui.InputText(tooltip='Enter a to-do', key='todo')
add_button = Gui.Button(key='add', tooltip='Add', image_source='images/add.png', mouseover_colors='lightblue')
list_box = Gui.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=(45, 10))
edit_button = Gui.Button('Edit', key='edit')
complete_button = Gui.Button(key='complete', tooltip='Complete', image_source='images/complete.png',
                             mouseover_colors='lightblue')
exit_button = Gui.Button('Exit', key='exit', button_color='red')

window = Gui.Window('My To-do app',
                    layout=[
                        [label_clock],
                        [label],
                        [input_box, add_button],
                        [list_box, edit_button, complete_button],
                        [exit_button]
                    ],
                    font=('Helvetica', 10),
                    )
while True:
    event, values = window.read(timeout=500)
    window['clock'].update(value=time.strftime('%d %b, %Y %H:%M:%S'))
    match event:
        case 'add':
            todos = functions.get_todos()
            if values['todo'] == '':
                Gui.popup('Please write todo')
                continue
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                Gui.popup('select item first', font=('Helvetica', 10), text_color='red', background_color='white')
        case 'complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                Gui.popup('select item first', font=('Helvetica', 10), text_color='red', background_color='white')
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case Gui.WIN_CLOSED | 'exit':
            break
window.close()
