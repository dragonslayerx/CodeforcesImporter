import os
from os import path

WRITE_FLAGS = os.O_CREAT | os.O_WRONLY


class CfiIgnore:
    """ CfiIgnore reads cfiignore file in dir_path directory. Ignore submission if id present in cfiignore"""

    CFI_IGNORE_FILENAME = 'cfiignore'

    def __init__(self, dir_path):
        self.ignore_list = []
        self.dir_path = dir_path
        self.fetch_ignore_list()

    def ignore(self, problem_id):
        """Returns True if problem_id is already present in cfiignore

        :param problem_id: problem-id to be checked for in cfiignore
        :return: True or False
        """

        return problem_id in self.ignore_list

    def add(self, problem_id):
        """Adds to ignore list"""

        self.ignore_list.append(problem_id)

    def fetch_ignore_list(self):
        """Reads ignore list from cfiignore file in dir_path directory"""

        try:
            file_path = path.join(self.dir_path, self.CFI_IGNORE_FILENAME)
            with open(file_path, 'r') as ignore_file:
                content = str(ignore_file.read(1000000))
                self.ignore_list = content.split(';')
        except (OSError, IOError) as ex:
            pass

    def write_ignore_list(self):
        """Writes ignore list to cfiignore file in dir_path directory"""

        try:
            file_path = path.join(self.dir_path, self.CFI_IGNORE_FILENAME)
            file_handle = os.open(file_path, WRITE_FLAGS)
            with os.fdopen(file_handle, 'w') as file_obj:
                for identifier in self.ignore_list:
                    file_obj.write(identifier)
                    file_obj.write(';')
        except (OSError, IOError) as ex:
            print ex.strerror

