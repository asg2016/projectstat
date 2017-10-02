import os
from .parsers import *


class ProjectModule:
    def __init__(self, module_full_path):
        self.module_path = module_full_path
        self.verbs = ()
        self.nouns = ()
        self.tree = None
        self.module_content = None
        self.__load_module__(module_full_path)

    def __load_module__(self, module_full_path):
        try:
            with open(module_full_path, 'r', encoding='utf-8') as module_handler:
                self.module_content = module_handler.read()
        except FileNotFoundError:
            raise

    def __module_stat__(self):
        pass

    def is_not_empty(self):
        return self.module_content is not None and \
               self.module_content != ''


class ProjectPythonModule(ProjectModule):

    def __load_module__(self, module_full_path):
        super().__load_module__(module_full_path)
        if self.is_not_empty:
            self.tree = python_module_parse(self.module_content)
