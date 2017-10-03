import json
import csv
from collections import Counter
from .stat import get_frequency_word_stat


class BaseReport():
    def __init__(self):
        self.stat = {}


    def to_json(self, filename):
        with open(filename, 'wb') as f:
            f.writelines(json.dumps(self.stat))


    def to_csv(self, filename):
        with open(filename, 'wb') as f:
            w = csv.writer(f)
            w.writerows(self.stat.items())


class ModuleReport(BaseReport):
    def __init__(self, module, top_size):
        self.stat = {'def': {}, 'var': {}, 'class': {}}
        self.__build_stat__(module, top_size)

    def __build_stat__(self, module, top_size):
        for items_key, items_val in module.names.items():
            self.stat[items_key] = get_frequency_word_stat(items_val, top_size)


class ProjectReport(BaseReport):
    def __init__(self, project, top_size):
        self.top_size = top_size
        self.stat = self.__build_stat__(project, top_size)

    def __build_stat__(self, project, top_size):
        verbs = Counter()
        nouns = Counter()
        for module_key, cur_module in project.modules.items():
            verbs += Counter(cur_module.module_stat['def']['verbs']) + \
                         Counter(cur_module.module_stat['var']['verbs']) + \
                         Counter(cur_module.module_stat['class']['verbs'])
            nouns += Counter(cur_module.module_stat['def']['nouns']) + \
                         Counter(cur_module.module_stat['var']['nouns']) + \
                         Counter(cur_module.module_stat['class']['nouns'])
        return {
                'verbs': dict(verbs.most_common(top_size)),
                'nouns': dict(nouns.most_common(top_size))
        }