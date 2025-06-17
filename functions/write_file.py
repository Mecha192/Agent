import os

def write_file(working_directory, file_path, content):
    join_paths = os.path.join(working_directory, file_path)
    file_path = os.path.abspath(join_paths)
    working_dir_path = os.path.abspath(working_directory)
    if not file_path.startswith(working_dir_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    try:
        with open(file_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return f'Error: {str(e)}'
