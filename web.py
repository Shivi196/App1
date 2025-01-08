import streamlit as st
import functions

todos = functions.get_todos()

st.title("My TO-DO APP")
st.subheader("This is my todo app..")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a to-do", placeholder="Add or Edit or Delete todo here")

print("Hello")