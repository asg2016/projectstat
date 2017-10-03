from .parsers import *
from .stat import get_frequency_word_stat


class ProjectModule:
    def __init__(self, module_full_path, top_size):
        self.module_path = module_full_path
        self.names = {'def': [], 'var': [], 'class':[]}
        self.tree = None
        self.module_content = None
        self.module_stat = {'def': {}, 'var': {}, 'class': {}}
        self.__load_module__(module_full_path)
        self.__categorize_nodes__()
        self.__build_stat__(top_size)

    def __load_module__(self, module_full_path):
        try:
            with open(module_full_path, 'r',
                      encoding='utf-8') as module_handler:
                self.module_content = module_handler.read()
        except FileNotFoundError as err:
            print(err)

    def __categorize_nodes__(self):
        try:
            for node in ast.walk(self.tree):
                if isinstance(node, ast.FunctionDef) and self.is_valid_def_name(node.name):
                    self.names['def'].append(node.name)
                elif isinstance(node, ast.ClassDef) and self.is_valid_class_name(node.name):
                    self.names['class'].append(node.name)
                elif isinstance(node, ast.Name) and not isinstance(node.ctx, ast.Load) and \
                        self.is_valid_var_name(node.id):
                    self.names['var'].append(node.id)
        except AttributeError as err:
            print(self.module_path, ' ', err)

    def is_valid_def_name(self, def_name):
        return True

    def is_valid_class_name(self, class_name):
        return True

    def is_valid_var_name(self, var_name):
        return True

    def is_not_empty(self):
        return self.module_content is not None and \
               self.module_content != ''

    def __build_stat__(self, top_size):
        for items_key, items_val in self.names.items():
            self.module_stat[items_key] = get_frequency_word_stat(items_val, top_size)


class ProjectPythonModule(ProjectModule):
    def is_valid_def_name(self, def_name):
        return not (def_name.startswith('__') and def_name.endswith('__'))

    def is_valid_var_name(self, var_name):
        return not (var_name.startswith('__') and var_name.endswith('__'))

    def __load_module__(self, module_full_path):
        super().__load_module__(module_full_path)
        if self.is_not_empty:
            self.tree = python_module_parse(self.module_content)
