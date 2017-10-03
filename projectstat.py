import os
import argparse
from projectstat.projects import PythonProject
from projectstat.reports import ProjectReport, ModuleReport


def create_parser():
    parser = argparse.ArgumentParser(description='Build some stat about your projects.')
    parser.add_argument('path', action='store', type=str,
                        help='path to local project')
    parser.add_argument('git', action='store', type=str,
                        help='clone url for project.git')
    parser.add_argument('--common', action='store_true',
                        help='common project stat')
    parser.add_argument('--detail', action='store_true',
                        help='detail module stat')
    parser.add_argument('-topsize', type=int, action='store',
                        help='top size for project')
    parser.add_argument('-maxfiles', type=int, action='store',
                        help='max files for processing in project')
    parser.add_argument('-json', action='store',
                        help='save report to json file')
    parser.add_argument('-csv', action='store',
                        help='save report to csv file')
    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    top_size = namespace.topsize
    max_files = namespace.maxfiles
    if namespace.path is not None and os.path.exists(namespace.path):
        path = namespace.path
        project = PythonProject(project_path=path, project_clone_url=None,
                                project_name='noname', max_modules_processing=max_files)
