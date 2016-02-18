import os

WRITE_FLAGS = os.O_CREAT | os.O_WRONLY


def write_to_file(file_path, content):
    try:
        file_handle = os.open(file_path, WRITE_FLAGS)
        with os.fdopen(file_handle, 'w') as file_obj:
            file_obj.write(content)
    except OSError as ex:
        print 'Error: ' + ex.errno
        raise ex
    except ValueError as ex:
        print 'Error: ' + ex.errno
        raise ex

