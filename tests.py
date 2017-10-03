from projectstat import *

project = PythonProject('',
                        'https://github.com/geekcomputers/Python.git',
                        'Python', 0, 10)

print('==================PROJECT NAME===================')
print('===============', project.project_name, '===============')
print(project.get_project_stat())
print('==================END STATISTIC==================')
