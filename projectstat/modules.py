import ast
from .parsers import *


class ProjectModule:
    def __init__(self, module_full_path):
        self.module_path = module_full_path
        self.names = {}
        self.tree = None
        self.module_content = None
        self.__load_module__(module_full_path)
        self.__categorize_nodes__()

    def __load_module__(self, module_full_path):
        try:
            with open(module_full_path, 'r', encoding='utf-8') as module_handler:
                self.module_content = module_handler.read()
        except FileNotFoundError:
            raise

    def __categorize_nodes__(self):
        self.names['def_names'] = []
        self.names['var_names'] = []
        self.names['class_names'] = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef) and self.is_valid_def_name(node.name):
                self.names['def_names'].append(node.name)
            elif isinstance(node, ast.ClassDef) and self.is_valid_class_name(node.name):
                self.names['class_names'].append(node.name)
            elif isinstance(node, ast.Name) and not isinstance(node.ctx, ast.Load) and \
                    self.is_valid_var_name(node.id):
                self.names['var_names'].append(node.id)

    def is_valid_def_name(self, def_name):
        return True

    def is_valid_class_name(self, class_name):
        return True

    def is_valid_var_name(self, var_name):
        return True

    def is_not_empty(self):
        return self.module_content is not None and \
               self.module_content != ''


class ProjectPythonModule(ProjectModule):

    def is_valid_def_name(self, def_name):
        return not (def_name.startswith('__') and def_name.endswith('__'))

    def __load_module__(self, module_full_path):
        super().__load_module__(module_full_path)
        if self.is_not_empty:
            self.tree = python_module_parse(self.module_content)
