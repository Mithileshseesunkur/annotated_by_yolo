import os

def list_files_in_folder(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

folder_path = 'path/to/your/folder'
files = list_files_in_folder(folder_path)
for file in files:
    print(file)
