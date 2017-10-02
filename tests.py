from projectstat import *


#project = PythonProject('D:/PyCharmProjects/home_work1/verbstat', 'verbstat')
project = PythonProject('C:/Users/Администратор/PycharmProjects/projectstat', 'projectstat')

print(project.project_name)
print(project.project_path)

for path in project.modules.keys():
    print(path)

