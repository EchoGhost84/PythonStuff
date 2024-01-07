import os

def find_and_read_files(directory, filenames):
    print("finding files please wait...")
    file_contents = {}
    for root, dirs, files in os.walk(directory):
        for filename in filenames:
            if filename in files:
                file_path = os.path.join(root, filename)
                # Open and read the file
                with open(file_path, 'r') as file:
                    content = file.read()
                    file_contents[filename] = content

    return file_contents

# Example usage
directory_to_search = r'C:/'
files_to_find = ['UserList.txt', 'PasswordList.txt', 'AdminUser.txt', 'AdminPassword.txt']

found_contents = find_and_read_files(directory_to_search, files_to_find)

for filename, content in found_contents.items():
    if content is not None:
        print(f"Content of {filename}:\n{content}")
    else:
        print(f"{filename} not found.")