"""
Given a word dictionary and sorted word frequency list
build a trie data structure.
"""
import os
import sys


DATA_MODULE = """
import marisa_trie

WORDS = {words}

TRIE = marisa_trie.Trie(WORDS.keys())

"""


def write(frequency_file):
    """
    Read in a frequency file.
    Use the data in this file to write out a new data module.
    """
    path = os.path.dirname(frequency_file)
    words = {}

    frequency_list = []
    with open(frequency_file) as f:
        frequency_list = f.readlines()
    # XXX - make the frequency number better
    frequent = len(frequency_list)
    for cword in frequency_list:
        cword = unicode(cword.strip())
        words[cword] = frequent
        frequent -= 1

    with open(path+'/data.py', 'w') as f:
        f.write(DATA_MODULE.format(words=str(words)))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        write(sys.argv[1])
    else:
        usage = "Usage: {0} <word_list> <word_frequency_list>"
        print usage.format(sys.argv[0])
