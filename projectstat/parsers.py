import ast


def python_module_parse(module_content):
    python_module_tree = None
    if module_content is not None:
        try:
            python_module_tree = ast.parse(module_content)
        except SyntaxError:
            raise
    return python_module_tree
