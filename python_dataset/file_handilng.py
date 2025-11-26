# file handling allows python to read, write update, and delete the files which are availabe in to your local system (pc)
# .csv,.txt,.json
# file handling functions:
# open()--> opens a file and returns a file object
# read()--> used to read entire content of a file
# readline()--> read online at a time
# readlines()-->read all the lines of the file and return as list("a","b")
# write() --> write a string to file;
# writelines()-->write list of strings in to the file
# seek()--->moves the file pointerntoma spicific [position]
# tell() -->return the current poision of pointer
# close()--> close the file
import os
from os import getcwd

#
# file opening modes:
# 'r'--> read -- default
# 'w'--> write --> over write existing data
# 'a' --> append (adds data for the file without overwriting )
# 'r+' read and write
# 'w+' write and read(creates new file if not exists)
# 'a+' append read

# file=open('demo.py','r')
# print(file.read())
# file.close()

#using context manager to open file

# with open('demo.py') as demofile:
#     for line in demofile:
#         print(line,end='')
# read() can read all the file content at single time and place it into memory (cause of memory issue)
# with open('demo.py') as demofile:
#     for line in demofile:
#        print(line,end='')


# with open('demo.py') as demofile:
#         # print(demofile.read(10000))
#         print(demofile.readlines())

# # Write mode
# with open('country_capital.txt','w') as file:
#     file.write('heloo python ')
# append mode(a)
# with open('country_capital.txt','a') as file:
#      file.write('\nheloo python ')

# with open('country_capital.txt','r') as readfile:
#     for line in readfile:
#         if line.startswith('Answer') is True:
#             with open('Answer.txt','a') as appendfile:
#                 appendfile.write(line)

#access files from any location
# print(os.getcwd())
# os.chdir(r"C:\Users\Desktop\myref\GIT")
# url->
# 1.absolute -->"C:\Users\babud\PycharmProjects\PythonProject1"
# relative url -->"\..\demo.py"
file_name=r"C:\Users\babud\Desktop\myref\GIT\indesxes.sql"
with open(file_name,'r') as file:
    for line in file:
        print(line,end='')

