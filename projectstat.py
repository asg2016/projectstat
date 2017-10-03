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
    parser.add_argument('-topsize', action='store',
                        help='top size for project')
    parser.add_argument('-maxfiles', action='store',
                        help='max files for processing in project')
    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
