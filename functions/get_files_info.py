import os
def get_files_info(working_directory, directory=None):
    join_paths = os.path.join(working_directory, directory)
    dir_path = os.path.abspath(join_paths)
    working_dir_path = os.path.abspath(working_directory)
    if not dir_path.startswith(working_dir_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(dir_path):
        return f'Error:  "{directory}" is not a directory'
    try:
        print_list = []
        dir_list = os.listdir(dir_path)
        for item in dir_list:
            item_path = os.path.join(dir_path, item)
            if os.path.isdir(item_path):
                size = os.path.getsize(item_path)
                joined = f"- {item}: file_size={size} bytes, is_dir=True"
                print_list.append(joined)
            if os.path.isfile(item_path):
                size = os.path.getsize(item_path)
                joined = f"- {item}: file_size={size} bytes, is_dir=False"
                print_list.append(joined)
        return "\n".join(print_list)
    except Exception as e:
        return f'Error: {str(e)}'