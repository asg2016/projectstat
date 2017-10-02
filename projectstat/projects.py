import os
from git import Git, GitCommandError
from .modules import *


def is_module_exists(module_full_path):
    return os.path.exists(module_full_path) and os.path.isfile(module_full_path)


class Project:
    def __init__(self, project_path = None,
                 project_clone_url = None,
                 project_name = None,
                 max_modules_processing=0, top_size=100):
        self.modules = {}
        self.modules_ext = ''
        if project_clone_url is not None:
            self.__clone_project_from_github__(project_clone_url)
            self.project_path = os.path.join(os.getcwd(), project_name)
        else:
            self.project_path = project_path
        self.project_name = project_name
        self.max_modules_processing = max_modules_processing
        self.top_size = top_size

    def is_last_module_for_processing(self):
        return 0 < self.max_modules_processing <= len(self.modules.keys())

    def is_my_module(self, module_full_path):
        return module_full_path.endswith(self.modules_ext) and \
               is_module_exists(module_full_path)

    def __clone_project_from_github__(self, clone_url):
        try:
            return Git().clone(clone_url)
        except GitCommandError as err:
            print(err)
            return

    def __load_modules__(self, project_path):
        if project_path is not None and os.path.exists(project_path):
            for dirname, dirs, files in os.walk(project_path, topdown=True):
                for file in files:
                    full_path = os.path.join(dirname, file)
                    if self.is_my_module(full_path) and \
                        not self.is_last_module_for_processing():
                        self.modules[full_path] = None


class PythonProject(Project):
    def __init__(self, project_path=None,
                 project_clone_url=None,
                 project_name=None,
                 max_modules_processing=0,
                 top_size=100):
        super().__init__(project_path, project_clone_url,
                         project_name, max_modules_processing,
                         top_size)
        self.modules_ext = '.py'
        self.__load_modules__(project_path)

    def __load_modules__(self, project_path):
        super().__load_modules__(project_path)
        for python_module_filename in self.modules.keys():
            self.modules[python_module_filename] = \
                ProjectPythonModule(python_module_filename)
