import os
from .modules import *


def is_module_exists(module_full_path):
    return os.path.exists(module_full_path) and os.path.isfile(module_full_path)


class Project:
    def __init__(self, project_path, project_name,
                 max_modules_processing=0, top_size=100):
        self.modules = {}
        self.modules_ext = ''
        self.project_name = project_name
        self.project_path = project_path
        self.max_modules_processing = max_modules_processing
        self.top_size = top_size

    def is_last_module_for_processing(self):
        return 0 < self.max_modules_processing <= len(self.modules.keys())

    def is_my_module(self, module_full_path):
        return module_full_path.endswith(self.modules_ext) and \
               is_module_exists(module_full_path)

    def __load_modules__(self, project_path):
        if project_path is not None and os.path.exists(project_path):
            for dirname, dirs, files in os.walk(project_path, topdown=True):
                for file in files:
                    if self.is_my_module(file) and \
                            not self.is_last_module_for_processing():
                        self.modules[os.path.join(dirname, file)] = None


class PythonProject(Project):
    def __init__(self, project_path, project_name, max_modules_processing=0):
        super().__init__(project_name, max_modules_processing)
        self.modules_ext = '.py'
        self.__load_modules__(project_path)

    def __load_modules__(self, project_path):
        super().__load_modules__(project_path)
        for python_module_filename in self.modules.keys():
            self.modules[python_module_filename] = ProjectPythonModule(python_module_filename)


