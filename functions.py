FILEPATH = "todos.txt"
# from http.cookiejar import user_domain_match
def get_todos(filepath=  FILEPATH):
    ''' Read the file and return the list of to-do items '''
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

# print(help(get_todos))  for printing the documentation string

def write_todos( todos_arg,filepath= FILEPATH):
    ''' Write the to-do items list in the text file '''
    with open(filepath, 'w') as local_file:
        local_file.writelines(todos_arg)
# print(help(write_todos))

# print(__name__)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())




#
# text = "\
#         principles of ai: \n\
#         data \
#         deep learning \
#         machine learning \
#         artificial intelligence \
# "

# text = '''
# principles of ai :
# hiii
# byee
# jjiiii
# '''
#
# print(text)