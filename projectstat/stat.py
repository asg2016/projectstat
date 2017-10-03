from collections import Counter
from nltk import pos_tag


def get_frequency_word_stat(list_of_names, top_size):
    words_by_categories = names_to_words_by_categories(list_of_names)
    stat = {}
    for category, word_list in words_by_categories.items():
        category_dict = {}
        for word, value in \
                Counter(word_list).most_common(top_size):
            category_dict[word] = value
        stat[category] = category_dict
    return stat


def names_to_words_by_categories(list_of_names):
    words = get_words_from_split_names(list_of_names)
    categories = {'verbs': [], 'nouns': []}
    for word in words:
        if word and word != '':
            if is_verb(word):
                categories['verbs'].append(word)
            else:
                categories['nouns'].append(word)
    return categories


def get_words_from_split_names(list_of_names):
    words = []
    for item_name in list_of_names:
        if '_' in item_name:
            words.extend(item_name.split('_'))
        else:
            words.append(item_name)
    return words


def is_verb(word):
    pos_info = pos_tag([word])
    return pos_info[0][1] == 'VB'
