# from functions import get_todos,write_todos
import functions
import time

now = time.strftime("%b %d %Y %H:%M: %S")
print("Today is ", now)

while True:
    user_action = input("Type add or show or edit or complete or  exit ")
    user_action = user_action.strip()

    # match user_action:
    #     case 'add':
    # if 'add'  in user_action and 'new' not in user_action:
                  # todo = input("Enter a todo : ") + '\n'

    if user_action.startswith('add'):

                  todo = user_action[4:]

                  # file = open('todos.txt','r')
                  # with context manager help you to close the file automatically without writing code for file close
                  # with open('todos.txt', 'r') as file:
                  #     todos = file.readlines()
                  todos = functions.get_todos()
                      # file.close()
                  # Readlines will return output in form of list where only read method will  return the whole o/p in string
                  # If you try to read the file twice you can;t as the cursor will exhaust with one file.read funx after that if you write file.read method again it try to read the spaces which is at the end of the whole file content

                  todos.append(todo + '\n')
                  functions.write_todos(todos)
                  # with open('todos.txt', 'w') as file:
                  #     file.writelines(todos)



                  # file = open('todos.txt','w')

                 # writelines  method will write lines in diff line but write method is to write a single long line to one line
                 #    file.close()

     # case 'show' | 'display':
    # elif 'show' in user_action:
    elif user_action.startswith('show'):
                # file  = open('todos.txt','r')
                # with open('todos.txt', 'r') as file:
                #     todos = file.readlines()
                todos = functions.get_todos()
                for index, item in enumerate(todos):
                    # print(index,'-',item.title())
                    row = f"{index + 1},:- {item.strip()}"
                    print(row)

    elif user_action.startswith('edit'):
    # elif 'edit' in user_action:
    # case 'edit':
    #         number = int(input("Number of to-do item to be edited : "))
            try:
                number = int(user_action[5:])
                number = number - 1
                # with open('todos.txt', 'r') as file:
                #     todos = file.readlines()
                todos = functions.get_todos()
                print(todos[number])

                new_todo = input("Enter new to-do : ")
                todos[number] = new_todo + '\n'
                functions.write_todos (todos)
                # with open('todos.txt', 'w') as file:
                #     file.writelines(todos)
            except ValueError:
                print("Your command is not valid!!!")

    elif user_action.startswith('complete'):
    # elif 'complete' in user_action:
        # case 'complete':
        #     number = int(input("Number of to-do item to be Completed : "))
            try:
                number = int(user_action[9:])
                number = number - 1
                # with open('todos.txt', 'r') as file:
                #     todos = file.readlines()
                todos = functions.get_todos()
                todo_to_remove = todos[number].strip('\n')
                print(todos.pop(number))

                functions.write_todos(todos)
                # with open('todos.txt', 'w') as file:
                #     file.writelines(todos)

                message = f"This todo {todo_to_remove} was removed from the list "
                print(message)
            except IndexError:
                print("The value provided is not in the list")

    elif user_action.startswith('exit'):
        # case 'exit':
            break

        # case  _:
    else:
            print("You have entered the some anonymous parameter....")

print("Take care.. see ya!!!")


'''
while True:
    user_action = input("Type add or show or edit or complete or  exit ")
    user_action = user_action.strip()

    if user_action.startswith('add'):

                  todo = user_action[4:]

                  todos = functions.get_todos()

                  todos.append(todo + '\n')
                  functions.write_todos(todos)

    elif user_action.startswith('show'):

                todos = functions.get_todos()
                for index, item in enumerate(todos):

                    row = f"{index + 1},:- {item.strip()}"
                    print(row)

    elif user_action.startswith('edit'):

            try:
                number = int(user_action[5:])
                number = number - 1

                todos = functions.get_todos()
                print(todos[number])

                new_todo = input("Enter new to-do : ")
                todos[number] = new_todo + '\n'
                functions.write_todos (todos)

            except ValueError:
                print("Your command is not valid!!!")

    elif user_action.startswith('complete'):

            try:
                number = int(user_action[9:])
                number = number - 1

                todos = functions.get_todos()
                todo_to_remove = todos[number].strip('\n')
                print(todos.pop(number))

                functions.write_todos(todos)

                message = f"This todo {todo_to_remove} was removed from the list "
                print(message)
            except IndexError:
                print("The value provided is not in the list")

    elif user_action.startswith('exit'):

            break
    else:
            print("You have entered the some anonymous parameter....")

print("Take care.. see ya!!!")'''