import os
from .modules import *


class Project:
    def __init__(self, project_name, max_modules_processing=0):
        self.modules = {}
        self.modules_ext = ''
        self.project_name = project_name
        self.max_modules_processing = max_modules_processing

    def is_last_module_for_processing(self):
        return 0 < self.max_modules_processing <= len(self.modules.keys())

    def is_my_module(self, module_filename):
        print(module_filename)
        return module_filename.endswith(self.modules_ext)

    def __load_modules__(self, project_path):
        print('ext - '+self.modules_ext)
        if project_path is not None and os.path.exists(project_path):
            for dirname, dirs, files in os.walk(project_path, topdown=True):
                for file in files:
                    if self.is_my_module(file) and \
                            not self.is_last_module_for_processing():
                        self.modules[os.path.join(dirname, file)] = object



class PythonProject(Project):
    def __init__(self, project_path, project_name, max_modules_processing=0):
        super().__init__(project_name, max_modules_processing)
        self.modules_ext = '.py'
        print(self.modules_ext)
        self.__load_modules__(project_path)

    def __load_modules__(self, project_path):
        super().__load_modules__(project_path)
        for python_module_filename in self.modules.keys():
            self.modules[python_module_filename] = ProjectPythonModule(python_module_filename)


