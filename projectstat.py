import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs='p')
    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
