from projectstat import *

project = PythonProject('',
                        'https://github.com/gitpython-developers/GitPython.git',
                        'GitPython')

print(project.project_name)
print('=================================================')
for path in project.modules.keys():
    if project.modules[path] is not None:

        for class_name in project.modules[path].names['class_names']:
            print('find class - ', class_name)
        for def_name in project.modules[path].names['def_names']:
            print('find def - ', def_name)
        for var_name in project.modules[path].names['var_names']:
            print('find var - ', var_name)


