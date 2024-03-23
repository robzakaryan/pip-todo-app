import functions
import PySimpleGUI as Gui

label = Gui.Text('Type in a to-do')
input_box = Gui.InputText(tooltip='Enter a to-do', key='todo')
add_button = Gui.Button('Add', key='add')

window = Gui.Window('My To-do app',
                    layout=[[label], [input_box, add_button]],
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
        case Gui.WIN_CLOSED | 'exit':
            break
window.close()
