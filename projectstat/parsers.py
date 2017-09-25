import ast


def python_module_parse(module_content):
    python_module_tree = None
    if module_content is not None:
        try:
            python_module_tree = ast.parse(module_content)
        except SyntaxError:
            raise
    return python_module_tree


class ModuleParser:
    def __init__(self, module_content):
        self.module_tree = None
        if module_content is not None:
            self.__parse__(module_content)

    def __parse__(self, module_content):
        pass


class PythonModuleParser(ModuleParser):
    def __parse__(self, module_content):
        try:
            self.module_tree = ast.parse(module_content)
        except SyntaxError:
            raise
