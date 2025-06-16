import os

def get_file_content(working_directory, file_path):
    join_paths = os.path.join(working_directory, file_path)
    file_path = os.path.abspath(join_paths)
    working_dir_path = os.path.abspath(working_directory)
    if not file_path.startswith(working_dir_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        max_chars = 10000

        with open(file_path, "r") as f:
            file_content_string = f.read(max_chars) + f'\n[...File "{file_path}" truncated at 10000 characters]'
        return file_content_string
    except Exception as e:
        return f'Error: {str(e)}'