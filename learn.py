# files in python and paths

# the with keyword is used for clean up tasks when working with unmanaged resources eg opening a file
# it is a control structure in python
with open("my_file.txt") as file:
    content = file.read() #returns the content of the file as a string
    print(content)
    # always close the file

# writing to a file
with open("my_file_2.txt", mode="w") as file:
    file.write("some new text here")

# we can also append something to a file using the append mode
with open("my_file_2.txt", mode="a") as file:
    file.write("\nThis is an appended text.")


# Relative and absolute paths in python.

# absolute file path would look something like: 
# /Work/Project/talk.ppt
# working directory is the directory you are currently working in

with open("C:\\Users\\Zaph_PC\\Desktop\\lost_file.txt") as file:
    content = file.read()
    print(content)

# or we can use forward slash since back slash means escaping
with open("C:/Users/Zaph_PC/Desktop/lost_file.txt") as lost_file:
    content = lost_file.read()
    print(content)

# Absolute file path is always relative to the root of the computer, relative file path is relative to the current working directory