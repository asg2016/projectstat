"""
Functions for working with words
"""
import ast
from nltk import pos_tag


class ProjectWords:
    pass


class PythonProjectWords(ProjectWords):
    pass

# def is_verb(word):
#     if not word:
#         return False
#     pos_info = pos_tag([word])
#     return pos_info[0][1] == 'VB'
#
#
# def get_verbs_from_function_name(function_name):
#     """
#     :param function_name: str
#     :return: generator of verbs
#     """
#     return (word for word in function_name.split('_') if is_verb(word))
#
#
# def internal_python_function(function_name):
#     return function_name.startswith('__') and function_name.endswith('__')
#
#
# def get_function_names(python_module_tree):
#     '''
#     :param python_module_tree: object
#     :return: generator of function names
#     '''
#     return (function.name.lower() for function in ast.walk(python_module_tree)
#             if isinstance(function, ast.FunctionDef)
#             and not internal_python_function(function.name))
