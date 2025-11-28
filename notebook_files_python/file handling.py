# File handling
# -------------

# Files are named locations on disk to store related information. They are used to permanently store data in a non-volatile memory (e.g. hard disk).

# Since Random Access Memory (RAM) is volatile (which loses its data when the computer is turned off), we use files for future use of the data by permanently storing them.

# When we want to read from or write to a file, we need to open it first. When we are done, it needs to be closed so that the resources that are tied with the file are freed.

# Hence, in Python, a file operation takes place in the following order:

# Open a file
# Read or write (perform operation)
# Close the file


# Types of files:
# ---------------

path = r"/Users/maheshkumar/Downloads/Besant_tech/Python_Template/sample.txt"

# f = open(path , mode='r')
# print(f.read())

# f.close()



# 1.Character file/Textual file ex: .txt
# 2.Binary file/Non textual file ex: images,video,audio,zip file

# Read operation:
# ---------------

def read(path):
    f=open(file=path)
    print('file is successfully opened')
    # print(f.readlines())
    # print(f.readline())

    for i in f.readlines():
        print(i)
    f.close()
    print('File got closed')
    print(f.read())

# read(path)

# Reading Character data from the text file:
# -------------------------------------------
# We can read character data from text file by using the following
# read methods.
# read()--> To read total data from the file
# read(n) --> To read 'n' characters from the file
# readline()--> To read only one line
# readlines()--> To read all lines into a list

# Write operation:

# --> This mode is used to write the data onto the file
# --> Syntax:
#     open(file='filename.txt',mode='w')
# --> There are 2 methods to perform write operations
#     1.write() -->string
#     2.writelines() -->list of lines

# WAP to perform write operation using write()
# file_path = "D:\\F drive\\learning\\Bes_tech\\Batch8_morning\\Assignment2.txt"

def write_operations(path):
    f=open(file=path,mode='w')
    print('File is successfully opened')
    f.write('My name')
    f.write('is')
    f.write('Mahesh')
    f.writelines(['I am working as ', 'a datascientistxs'])
    print('Data has been written into file',f.name)
    f.close()
    print('File got closed')

# if __name__ == '__main__':
    # write_operations(path)
    # write_operations(r"/Users/maheshkumar/Downloads/Besant_tech/Python_Template/sample1.txt")

# append mode:(a)
# ------------
# This mode is used to append the data to the file at the end of the
# cursor position


# syntax:
# --------
# open(file='filename.txt',mode='a')


def append_operations():
    f=open(file=path,mode='a')
    print('File is successfully opened')
    f.write('python\n')
    f.write('django\n')
    f.write('restapi\n')
    f.write('SANDESH\n')
    f.write('PYTHON\n')
    f.write('DJANGO\n')
    print('Data has been written into file',f.name)
    f.close()
    print('File got closed')
if __name__ == '__main__':
    append_operations()


# Mode    Description
# r       Opens a file for reading. (default)
# w       Opens a file for writing. Creates a new file if it does 
#         not exist or truncates the file if it exists.
# x       Opens a file for exclusive creation. If the file already 
#         exists, the operation fails.
# a       Opens a file for appending at the end of the file without 
#         truncating it.  Creates a new file if it does not exist.
# t       Opens in text mode. (default)
# b       Opens in binary mode.
# +       Opens a file for updating (reading and writing)


# Various properties of a File object:

# 1.name -->      Name of opened file
# 2.mode -->      Mode in which the file is opened
# 3.closed-->     used to check whether the opened file is closed or not
#                 It will return True if the file is closed else it will return False
# 4.readable()--> used to check whether the opened file is readable or not
#                 It will return True if the file is readable else it will return False
# 5.writable()--> used to check whether the opened file is writable or not It will return True 
#                 if the file is writable else it will return False


# Write a python program to check the properties of a file


# def properties(file_path):
#     f=open(file_path)
#     print('file is successfully opened')
#     print(f.read())
#     print(f'File name: {f.name}')
#     print(f'File mode: {f.mode}')
#     print(f'Is file Readable: {f.readable()}')
#     print(f'Is file Writable: {f.writable()}')
#     print(f'Is file closed: {f.closed}')
    
#     f.close()
#     print(f'Is file closed: {f.closed}')
#     print('File got closed')

# properties(path)

# properties("D:\\F drive\\learning\\Bes_tech\\Batch8_morning\Assignment2.txt")

# Context Manager/with statement
# ------------------------------

# Syntax:
# f=open(file,mode) -->Normal syntax

# with open(file,mode) as f: -->Syntax using with statement

# def with_statement(file_path):
#     with open(file_path,'w') as f:
#         f.write('Sandesh\n')
#         f.write('will teach\n')
#         f.write('Django')
#         print(f'Data has been written into : {f.name}')
#         print(f'Is file Closed: {f.closed}') 
#     print(f'Is file Closed: {f.closed}') 
# if __name__ == '__main__':
#     with_statement(path)

# tell() and seek()
# -----------------

def tell_operation(file_path):
    with open(file_path,'r') as l:
        print(l.tell()) 
        print(l.read(3)) 
        print(l.tell())
        print(l.read(3)) 
        print(l.tell()) 
        print(l.read(3)) 
        print(l.tell()) 
        # print(l.tell(3)) 
        print(l.read(-1))
        print(l.tell()) 

# if __name__ == '__main__':
    # tell_operation(path)



# seek()
# def operation_seek():
#     data='Hello world You are learning Python from Mahesh'

#     with open(path,'w') as f:
#         f.write(data)
#         print('data has been written into :',f.name)
    
#     with open(path,'r+') as f:
#         data=f.read()
#         print(data)
#         print('The current cursor position',f.tell())
#         f.seek(data.rfind("Mahesh"))
#         print('The current cursor position',f.tell())
#         f.write('Mahesh kumar')
#         f.seek(0)
#         print('The current cursor position',f.tell())
#         f.write("Mello ")
#         f.seek(0)
#         new_data=f.read()
#         print('Data after modification')
#         print(new_data)
# if __name__ == '__main__':
#     operation_seek()


# with open('filename', 'a') as f: # able to append data to file
#     f.write(var1) # Were var1 is some variable you have set previously
#     f.write('data') 
#     f.close() # You can add this but it is not mandatory 

# with open('filename', 'r') as f: # able to read data from file ( also is the  default mode when opening a file in python)

# with open('filename', 'x') as f: # Creates new file, if it already exists it will 
#                                     cause it to fail

# with open('filename', 't') as f: # opens the file in text mode (also is defualt)

# with open('filename', 'b') as f: # Use if your file will contain binary data
  
# with open('filename', 'w') as f: # Open file with ability to write, will also create the file if it does not exist (if it exists will cause it to fail)

# with open('filename', '+') as f: # Opens file with reading and writing
