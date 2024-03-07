import os

#Write a Python program to list only directories, files and all directories, files in a specified path.
#path = input("Enter a specified path:")
path = "//Users/assemseidkarim//Desktop//PP_2//Practice//lab 6"
os.chdir(path)
print(os.listdir(path))

#Write a Python program to check for access to a specified path. 
#Test the existence, readability, writability and executability of the specified path.

print("Exists:",os.access(path, os.F_OK))
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executabe:", os.access(path, os.X_OK))

#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
if os.access(path, os.F_OK):
    basename = os.path.basename(path)
    print(basename)
    dirname = os.path.dirname(path)
    print(dirname)

#Write a Python program to count the number of lines in a text file.
with open('text.txt', 'r') as file:
    content = file.readlines()
    print(len(content))

#Write a Python program to write a list to a file.
with open('text.txt', 'a') as file:
    list = ["1", "2", "3", "3"]

    for item in list:
       file.write(str(item) + "\n")
    #file.write(''.join(list))

    print(content)


#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
    
for i in range(65, 91):
    file_name = open(f"{chr(i)}.txt", 'x')


#Write a Python program to copy the contents of a file to another file
with open('text.txt', 'r') as files:
    contents = files.read()

with open('textfile_copy.txt', 'a') as copy_file:
    copy_file.write(contents)

#Write a Python program to delete file by specified path. 
#Before deleting check for access and whether a given path exists or not.


file_to_delete = input("Enter a path to delete file: ")
if os.access(file_to_delete, os.F_OK):
    os.chdir(path)
    os.remove(file_to_delete)
else:
    print('Path not found!')

    
    


