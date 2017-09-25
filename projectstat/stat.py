"""
Main class for generating verb statistics
"""
import os
import collections

# from .trees import get_python_code_trees
# from .words import get_function_names, get_verbs_from_function_name


class ProjectStat:
    pass


class PythonProjectStat(ProjectStat):
    pass


class JSProjectStat(ProjectStat):
    pass

# class PythonModulesStat:
#     def __init__(self):
#         self.__path = ''
#         self.__projects = []
#         self.__max_project_files = 10
#         self.__verbs = []
#         self.__top_size = 10
#         self.__verb_occurence = {}
#         self.__top_verbs = []
#
#     def __load_project(self, project):
#         project_verbs = []
#         project_path = os.path.join(self.__path, project)
#         for tree in get_python_code_trees(project_path,
#                                           self.__max_project_files):
#             functions_names = get_function_names(tree)
#             for function_name in functions_names:
#                 project_verbs.extend(get_verbs_from_function_name(function_name))
#         return project_verbs
#
#     def load(self, path, projects, max_project_files=100, top_size=100):
#         """
#         load your projects and biuld stat
#         :type top_size: int
#         :type max_project_files: int
#         :type path: str
#         :type projects: list
#         """
#         self.__path = path
#         self.__projects = projects
#         self.__max_project_files = max_project_files
#         self.__top_size = top_size
#         for project in projects:
#             self.__verbs += self.__load_project(project)
#         self.__top_verbs = set(self.__verbs)
#         for verb, value in \
#                 collections.Counter(self.__verbs).most_common(self.__top_size):
#             if self.__verb_occurence.get(verb) is None:
#                 self.__verb_occurence[verb] = value
#
#     def get_top_verbs(self):
#         return self.__top_verbs
#
#     def get_verb_occurence(self, verb):
#         return self.__verb_occurence[verb]
