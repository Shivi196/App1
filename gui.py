import functions

import FreeSimpleGUI as sg


label = sg.Text('Type in a To-Do ')
input_box = sg.InputText(tooltip="Enter a to-do item ")
add_button = sg.Button("Add")

window = sg.Window('My To-do app',layout=[[label],[input_box,add_button]])
window.read()
print("hello")
window.close()



