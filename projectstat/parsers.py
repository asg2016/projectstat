import ast


def python_module_parse(module_content):
    if module_content is not None:
        try:
            return ast.parse(module_content)
        except SyntaxError as e:
            print(e)
            return
