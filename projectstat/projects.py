from .modules import *


class Project:
    def __init__(self, project_path):
        self.modules = {}
        self.project_name = ''
        self.__load__(project_path)

    def __load__(self, path):
        pass


class PythonProject(Project):
    pass
