import os

file_path = 'PasswordList.txt'
if os.path.isfile(file_path):
    with open(file_path, 'r') as f:
        print(f.read())
else:
    print('The file does not exist.')