import os
from git import Git, GitCommandError
from .modules import *


def is_module_exists(module_full_path):
    return os.path.exists(module_full_path) and os.path.isfile(module_full_path)


class Project:
    def __init__(self, project_path = None,
                 project_clone_url = None,
                 project_name = None,
                 max_modules_processing=0):
        self.modules = {}
        self.modules_ext = ''
        if project_clone_url is not None:
            self.project_path = os.path.join(os.getcwd(), project_name)
            if os.path.exists(self.project_path):
                os.rmdir(self.project_path)
            self.__clone_project_from_github__(project_clone_url)
        else:
            self.project_path = project_path
        self.project_name = project_name
        self.max_modules_processing = max_modules_processing

    def is_last_module_for_processing(self):
        return 0 < self.max_modules_processing <= len(self.modules.keys())

    def is_my_module(self, module_full_path):
        return module_full_path.endswith(self.modules_ext) and \
               is_module_exists(module_full_path)

    def __clone_project_from_github__(self, clone_url):
        try:
            return Git(os.getcwd()).clone(clone_url)
        except GitCommandError as err:
            print(err)
            return

    def __load_modules__(self):
        if self.project_path is not None:
            for dirname, dirs, files in os.walk(self.project_path, topdown=True):
                for file in files:
                    full_path = os.path.join(dirname, file)
                    if self.is_my_module(full_path) and \
                        not self.is_last_module_for_processing():
                        self.modules[full_path] = None


class PythonProject(Project):
    def __init__(self, project_path=None,
                 project_clone_url=None,
                 project_name=None,
                 max_modules_processing=0):
        super().__init__(project_path, project_clone_url,
                         project_name, max_modules_processing)
        self.modules_ext = '.py'
        self.__load_modules__()

    def __load_modules__(self):
        print(self.project_path)
        super().__load_modules__()
        for python_module_filename in self.modules.keys():
            self.modules[python_module_filename] = \
                ProjectPythonModule(python_module_filename)
