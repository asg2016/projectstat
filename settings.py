"""
    Example of the config file for using Lib
"""

PROJECTS_SETTINGS = {
    # 'python_projects': {
    #     'location': 'local',
    #     'max_files_processing': 10,
    #     'file_patterns': ('*.py',),
    # },
    'python_projects': {
        'location': 'github',
        'max_files_processing': 10,
        'file_patterns': ('*.py',),
    },
}

LOCATIONS = {
    'local': {
        'path': 'C:/Users/Администратор/PycharmProjects',
    },
    'github': {
        'user': '',
        'password': '',
        # 'key': 'asasdferdrfrefesd345323423523fgdfgg4ert34',
        'temp_dir': 'd:/temp',
        'clear_temp': True,
    }
}


