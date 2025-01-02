from PySimpleGUI import Window

import functions

import PySimpleGUI as sg


label = sg.Text('Type in a To-Do ')
input_box = sg.InputText(tooltip="Enter a to-do item ",key= "add_data")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),enable_events=True,key= 'edit_data',size=[45,10])
# key helps in recognising the events data that whether its edit event data or add event
# enable_events helps in getting the run time selected data at the backend program and see what event is getting selected and when

edit_button = sg.Button("Edit")

window = sg.Window('My To-do app',
                   layout=[[label,input_box,add_button],
                           [list_box,edit_button]],
                   font= ('Helvetica',14)
                   )
while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['add_data']+ '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            # The below line code is for showing the newly added value in window of edit data block at front end with uodated new todo list
            window['edit_data'].update(values=todos)

        case 'Edit':
            todo_to_edit = values['edit_data'][0]
            new_todo = values['add_data'] + '\n'

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['edit_data'].update(values=todos)

        case 'edit_data':
            window['add_data'].update(value=values['edit_data'][0])
        # This code is for updating the selected value from edit data fields in the add input text box as earlier after editing the edited data only showing there no newly selected data changing in the add inout box field for editing further
        case sg.WINDOW_CLOSED:
            # This case is for avoiding the killing app error while clicking on close(x) button of the app so this prevents us from that error
            break
#

# print("hello")
window.close()



