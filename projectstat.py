import os
import argparse
from projectstat.projects import PythonProject
from projectstat.reports import ProjectReport, ModuleReport


def create_parser():
    parser = argparse.ArgumentParser(description='Build some stat about your projects.')
    parser.add_argument('-path', action='store', type=str,
                        help='path to local project')
    parser.add_argument('-git', action='store', type=str,
                        help='clone url for project.git')
    parser.add_argument('--common', action='store_true',
                        help='common project stat')
    parser.add_argument('--detail', action='store_true',
                        help='detail module stat')
    parser.add_argument('-name', type=str, action='store',
                        help='project name')
    parser.add_argument('-topsize', type=int, action='store',
                        help='top size for project')
    parser.add_argument('-maxfiles', type=int, action='store',
                        help='max files for processing in project')
    parser.add_argument('-json', action='store',
                        help='path for save report to json file')
    parser.add_argument('-csv', action='store',
                        help='path for save report to csv file')
    return parser


if __name__ == '__main__':
    parser = create_parser()
    path = None
    clone_url = None
    project = None
    report_common = None
    report_module = None
    namespace = parser.parse_args()
    if namespace.topsize:
        top_size = namespace.topsize
    else:
        top_size = 10
    if namespace.maxfiles:
        max_files = namespace.maxfiles
    else:
        max_files = 0
    if namespace.name:
        project_name = namespace.name
    else:
        project_name = 'project'
    if namespace.path is not None and os.path.exists(namespace.path):
        path = namespace.path
        project = PythonProject(project_path=path, project_clone_url=None,
                                project_name=project_name, max_modules_processing=max_files)

    elif namespace.git is not None and namespace.git != '':
        clone_url = namespace.git
        project = PythonProject(project_path=None, project_clone_url=clone_url,
                                project_name=project_name, max_modules_processing=max_files)

    else:
        print('Not enter path or git. Program is exit.')

    if project is not None:
        if namespace.common:
            report_common = ProjectReport(project, top_size)
            print('==========================================')
            print('Common Report for ', project_name, '======')
            print(report_common.stat)
            print('==========================================')
            if namespace.json is not None and os.path.exists(namespace.json):
                report_common.to_json(os.path.join(namespace.json, project_name + '.json'))
            if namespace.csv is not None and os.path.exists(namespace.csv):
                report_common.to_csv(os.path.join(namespace.csv, project_name + '.csv'))
        if namespace.detail:
            for module_path, project_module in project.modules.items():
                report_module = ModuleReport(project_module, top_size)
                print('-----------------------------------------')
                print('Details for module ', project_module.module_path)
                print('-----------------------------------------')
                print(report_module.stat)
                print('-----------------------------------------')
                dir_name, file_name = os.path.split(project_module.module_path)
                if namespace.json is not None and os.path.exists(namespace.json):
                    report_module.to_json(os.path.join(namespace.json, project_name + '_' + file_name + '.json'))
                if namespace.csv is not None and os.path.exists(namespace.csv):
                    report_module.to_csv(os.path.join(namespace.csv, project_name + '_' + file_name + '.csv'))

