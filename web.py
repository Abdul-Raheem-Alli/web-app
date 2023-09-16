import streamlit as st
import text
todos = text.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] +"\n"
    print(todo)
    todos.append(todo)
    text.write_todos(todos)


st.title("My todos app")
st.subheader("this is my todo app")
st.write("this app is a tod app")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        text.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
    st.checkbox(todo)
st.text_input(label="", placeholder="enter a todo app", on_change=add_todo, key='new_todo')
