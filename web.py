import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state.get('todo_input') + '\n'
    todos.append(new_todo)
    functions.write_todos(todos)


st.title('To-do web app')
st.subheader('This is a to-do up')
st.write('This app is to increase your productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='Enter a todo', placeholder='Enter a todo...',
              on_change=add_todo,
              key='todo_input',
              )
