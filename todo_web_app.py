import streamlit as st
import functions


todos=functions.get_todos()
def add_todo():
    todo=st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo List")
st.write("Stay focused and driven towards your goals with the power of a well-organized"
         " todo list guiding you every step of the way.")
for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox == True:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
st.text_input(label="",
              placeholder="Add a new Todo",on_change=add_todo,key='new_todo')

