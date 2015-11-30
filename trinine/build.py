"""
Given a word dictionary and sorted word frequency list
build a trie data structure.
"""
import os
import sys


DATA_MODULE = """
import marisa_trie

WORDS = {words}

trie = marisa_trie.Trie(WORDS.keys())

"""


def write(words_file, frequency_file):
    path = os.path.dirname(words_file)
    words = {}
    with open(words_file) as f:
        word = f.readline()
        while word:
            words[unicode(word.strip())] = 0
            word = f.readline()

    frequency_list = []
    with open(frequency_file) as f:
        frequency_list = f.readlines()
    # XXX - make the frequency number better

    frequent = len(frequency_list)
    for cword in frequency_list:
        cword = cword.strip()
        words[cword] = frequent
        frequent -= 1

    with open(path+'/data.py', 'w') as f:
        f.write(DATA_MODULE.format(words=str(words)))


if __name__ == '__main__':
    if len(sys.argv) == 3:
        write(sys.argv[1], sys.argv[2])
    else:
        usage = "Usage: {0} <word_list> <word_frequency_list>"
        print usage.format(sys.argv[0])
