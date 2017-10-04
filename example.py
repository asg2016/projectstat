from projectstat import *

project = PythonProject('',
                        'https://github.com/geekcomputers/Python.git',
                        'Python')
report = ProjectReport(project, 20)

print('==================PROJECT NAME===================')
print('===============', project.project_name, '===============')
print(report.stat)
print('==================END STATISTIC==================')
