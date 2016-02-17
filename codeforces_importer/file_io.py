import os
import errno

WRITE_FLAGS = os.O_CREAT | os.O_WRONLY


def write_to_file(file_path, content):
    try:
        file_handle = os.open(file_path, WRITE_FLAGS)
    except OSError as e:
        print 'Error: ' + e.errno
    else:
        if content is not None:
            with os.fdopen(file_handle, 'w') as file_obj:
                file_obj.write(content)
