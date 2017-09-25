"""
    Example of the config file for using Lib
"""

PROJECTS_SETTINGS = {
    'python_projects': {
        'location': 'local',
        'file_patterns': ('*.py',),
    },
    'js_projects': {},
    'project_names': ('home_work', 'home_work1', 'projectstat'),
}

LOCATIONS = {
    'local': {
        'path': 'C:/Users/Администратор/PycharmProjects',
    },
    'github': {
        'user': 'asg2016',
        'password': 'uR7ExM51',
        'temp_dir': 'd:/temp',
        'del_after': True,
    }
}
