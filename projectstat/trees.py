"""
Functions for working with ast.trees
"""
import os
import ast


class ProjectTree:
    def __init__(self, project_path, project_name,
                 project_max_files_processing=10):
        self.project_path = project_path
        self.project_name = project_name
        self.project_max_files_processing = project_max_files_processing
        self.project_files_processing = 0
        self.project_files = ()
        self.project_words_stat = {}

    def __parse__(self):
        pass

    def __load_module__(self, module_path):
        pass


class PythonProjectTree(ProjectTree):
    pass


class JSProjectTree(ProjectTree):
    pass

# def is_python_file(filename):
#     return filename.endswith('.py')
#
#
# def get_python_module_filenames_from_path(
#         path,
#         max_processing_files,
# ):
#     """
#     getting list of filenames from path
#     :type max_processing_files: int
#     :type path: str
#     :return: list of .py filenames
#     """
#     module_filenames = []
#     for dirname, dirs, files in os.walk(path, topdown=True):
#         module_filenames += [os.path.join(dirname, file)
#                              for file in files
#                              if len(module_filenames) <= max_processing_files
#                              and is_python_file(file)]
#     return module_filenames
#
#
# def get_python_code_trees(
#         path='',
#         max_processing_modules=100
# ):
#     """
#     build trees from files of path
#     :type path: str
#     :type max_processing_modules: int
#     :return: list of tree objects
#     """
#     modules_files = \
#         get_python_module_filenames_from_path(path,
#                                               max_processing_modules)
#     python_code_trees = []
#     for python_module in modules_files:
#         with open(python_module, 'r', encoding='utf-8') as module_handler:
#             python_module_content = module_handler.read()
#         try:
#             tree = ast.parse(python_module_content)
#             python_code_trees.append(tree)
#         except SyntaxError:
#             raise
#         return python_code_trees
