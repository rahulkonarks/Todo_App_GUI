import functions
import PySimpleGUI as psGUI
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

psGUI.theme("BluePurple")

clock = psGUI.Text(key='clock')
prompt_label = psGUI.Text("Type in a to-do")
todo_input = psGUI.Input(tooltip="Enter in a to-do", key="todo")
add_button = psGUI.Button(image_source="add.png", size=2, mouseover_colors="LightBlue2",
                          tooltip="Add todo", key="Add")
list_box = psGUI.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45, 10])
edit_button = psGUI.Button("Edit")
complete_button = psGUI.Button("Complete")
exit_button = psGUI.Button("Exit")

window = psGUI.Window("Todo App",
                      layout=[[clock, prompt_label],
                              [todo_input, add_button],
                              [list_box, edit_button, complete_button],
                              [exit_button]],
                      font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    print(values['todo'])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0].strip("\n")
                new_todo = values['todo'] + '\n'

                todos = functions.get_todos()
                index = todos.index(todo_to_edit + '\n')
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)

            except IndexError:
                psGUI.popup("Please select an item first", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')

            except IndexError:
                psGUI.popup("Please select an item first", font=("Helvetica", 20))

        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case psGUI.WIN_CLOSED:
            break

window.close()
