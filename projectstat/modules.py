import os
from .parsers import *


class ProjectModule:
    def __init__(self, module_path, module_file):
        self.module_path = module_path
        self.module_file = module_file
        self.verbs = ()
        self.nouns = ()
        self.tree = None
        self.module_content = ''
        self.__load_module__(os.path.join(module_path, module_file))

    def __load_module__(self, module_path):
        try:
            with open(module_path, 'r', encoding='utf-8') as module_handler:
                self.module_content = module_handler.read()
        except FileNotFoundError:
            self.module_content = None
            raise

    def __build_stat__(self):
        pass


class ProjectPythonModule(ProjectModule):
    def __load_module__(self, module_path):
        super().__load_module__(module_path)
        if self.module_content is not None:
            self.tree = python_module_parse(self.module_content)

    def __build_stat__(self):
        pass




class ProjectJSModule(ProjectModule):
    def __init__(self, module_path, module_file):
        super().__init__(module_path, module_file)

