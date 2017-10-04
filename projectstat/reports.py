import json
import csv
from collections import Counter
from .stat import get_frequency_word_stat


class BaseReport():
    def __init__(self, project, top_size):
        self.stat = {}


    def to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.stat, f)


    def to_csv(self, filename):
        with open(filename, 'w') as f:
            w = csv.writer(f)
            w.writerows(self.stat.items())


class ModuleReport(BaseReport):
    def __init__(self, project_module, top_size):
        self.stat = {'def': {}, 'var': {}, 'class': {}}
        self.__build_stat__(project_module, top_size)

    def __build_stat__(self, project_module, top_size):
        for items_key, items_val in project_module.names.items():
            self.stat[items_key] = get_frequency_word_stat(items_val, top_size)


class ProjectReport(BaseReport):
    def __init__(self, project, top_size):
        self.top_size = top_size
        self.stat = self.__build_stat__(project, top_size)

    def __build_stat__(self, project, top_size):
        verbs = Counter()
        nouns = Counter()
        for module_key, cur_module in project.modules.items():
            verbs += Counter(ModuleReport(cur_module, top_size).stat['def']['verbs']) + \
                         Counter(ModuleReport(cur_module, top_size).stat['var']['verbs']) + \
                         Counter(ModuleReport(cur_module, top_size).stat['class']['verbs'])
            nouns += Counter(ModuleReport(cur_module, top_size).stat['def']['nouns']) + \
                         Counter(ModuleReport(cur_module, top_size).stat['var']['nouns']) + \
                         Counter(ModuleReport(cur_module, top_size).stat['class']['nouns'])
        return {
                'verbs': dict(verbs.most_common(top_size)),
                'nouns': dict(nouns.most_common(top_size))
        }