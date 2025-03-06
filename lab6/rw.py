import os
import string


# def l(p):
#     if not os.path.exists(p):
#         return
    
#     dirs = []
#     files = []
#     all = os.listdir(p)
    
#     for i in all:
#         f = os.path.join(path, i)
#         if os.path.isdir(f):
#             dirs.append(i)
#         elif os.path.isfile(f):
#             files.append(i)
#     print(dirs)
#     print(files)


# def l(path):
#     if not os.path.exists(path):
#         print("Not exists")
#         return
#     else: print("Yes")
#     if os.access(path, os.R_OK):
#         print("Yes")
#     else: print("No")
#     print("Yes" if os.access(path, os.W_OK) else "No")
#     print("Yes" if os.access(path, os.X_OK) else "No")


# def l(path):
    # if not os.access(path, os.F_OK):
    #     print("path do not exsist")
    #     return
    # else: print("path exist")

    # if os.path.isfile(path):
    #     print(f"Filename: {os.path.basename(path)}")
    #     print(f"Directory: {os.path.dirname(path)}")
    # elif os.path.isdir(path):
    #     print(f"'{path}' is a directory.")

# def l(path):
    # if not os.path.exists(path):
    #     return
    
    # with open(path, 'r') as fp:
    #     lines = len(fp.readlines())
    #     print('Total Number of lines:', lines)


# def write_list_to_file(file_path, data_list):
#     with open(file_path, 'w', encoding='utf-8') as file:
#         for item in data_list:
#             file.write(f"{item}\n")

# file_path = input("Enter the file path: ")
# data_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
# write_list_to_file(file_path, data_list)


# Create text files named A.txt, B.txt, ..., Z.txt
# for letter in string.ascii_uppercase:
#     filename = f"{letter}.txt"
#     with open(filename, 'w') as file:
#         file.write(f"This is file {filename}\n")

# print("26 text files created successfully!")

# Program to copy contents from one file to another

# def copy_file(source_file, destination_file):
#     try:
#         with open(source_file, 'r') as src:
#             content = src.read()
        
#         with open(destination_file, 'w') as dest:
#             dest.write(content)
            
#         print(f"Contents successfully copied from {source_file} to {destination_file}.")
        
#     except FileNotFoundError:
#         print(f"Error: The file {source_file} does not exist.")
#     except IOError as e:
#         print(f"I/O error occurred: {e}")

# source = 'source.txt'
# destination = 'destination.txt'

# copy_file(source, destination)

# def delete_file(file_path):
#     # Check if file exists
#     if os.path.exists(file_path):
#         # Check if file is accessible and writable
#         if os.access(file_path, os.W_OK):
#             try:
#                 os.remove(file_path)
#                 print(f"File '{file_path}' deleted successfully.")
#             except Exception as e:
#                 print(f"Error while deleting the file: {e}")
#         else:
#             print(f"No permission to delete '{file_path}'. Check file permissions.")
#     else:
#         print(f"File '{file_path}' does not exist.")


# file_to_delete = 'path/to/your/file.txt'
# delete_file(file_to_delete)




# path = input()
# l(path)