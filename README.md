# projectstat
## Build statistics about your project and modules

Very simple example for git-project:
```python
from projectstat import *

project = PythonProject(None, 'https://github.com/geekcomputers/Python.git', 'Python')
report = ProjectReport(project, 20)
```
Very simple example for local-project:
```python
from projectstat import *

project = PythonProject('/home/user/project', None, 'Python')
report = ProjectReport(project, 20)
```
## You can use projectstat from cmdline with projectstat.py

>usage: projectstat.py [-h] [-path PATH] [-git GIT] [--common] [--detail]
>                      [-name NAME] [-topsize TOPSIZE] [-maxfiles MAXFILES]
>                      [-json JSON] [-csv CSV]
>
>Build some stat about your projects.
>
>optional arguments:
>  -h, --help          show this help message and exit
>  -path PATH          path to local project
>  -git GIT            clone url for project.git
>  --common            common project stat
>  --detail            detail module stat
>  -name NAME          project name
>  -topsize TOPSIZE    top size for project
>  -maxfiles MAXFILES  max files for processing in project
>  -json JSON          path for save report to json file
>  -csv CSV            path for save report to csv file

Examples:

> python3 projectstat.py -git https://github.com/geekcomputers/Python.git --common -topsize 10

> python3 projectstat.py -path /home/path/project --common --detail -topsize 20 -maxfiles 100

> python3 projectstat.py -path /home/path/project --common -json /home/path/reports

> python3 projectstat.py -path /home/path/project --common --detail -csv /home/path/reports
