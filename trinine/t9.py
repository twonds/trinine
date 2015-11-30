"""
"""
import imp
import os

import marisa_trie


KEY_MAP = {0: [],
           1: [],
           2: [u'a', u'b', u'c'],
           3: [u'd', u'e', u'f'],
           4: [u'g', u'h', u'i'],
           5: [u'j', u'k', u'l'],
           6: [u'm', u'n', u'o'],
           7: [u'p', u'q', u'r', u's'],
           8: [u't', u'u', u'v'],
           9: [u'w', u'x', u'y', u'z']
           }


class T9:

    def __init__(self, data_dir="./data"):
        self.data_dir = data_dir
        self.data_module = self.data_dir+"/data.py"
        self.trie_data_file = self.data_dir+"/t9.trie"

    def load(self):
        """
        Load up words and tri data structure that is saved to disk.
        If it does not exist then use existing data to build it.
        """
        if os.path.exists(self.trie_data_file):
            self.word_trie = marisa_trie.Trie()
            with open(self.trie_data_file, 'r') as f:
                self.word_trie.read(f)
        if os.path.exists(self.data_module):
            self.data = imp.load_source('data', self.data_module)

    def map_number(self, number):
        ret_chars = []
        for num in str(number):
            chars = KEY_MAP[int(num)]
            if not chars:
                break
            ret_chars.append(chars)
        return ret_chars

    def words(self, number):
        """
        Given a number return possible word combinations sorted by frequency.
        """
        ret_words = []
        for i, chars in enumerate(self.map_number(number)):
            if i == 0:
                ret_words = chars
            else:
                new_words = []
                for word in ret_words:
                    for c in chars:
                        new_word = word+c
                        if self.data.trie.keys(new_word):
                            new_words.append(new_word)
                ret_words = new_words

        return sorted(filter(lambda x: x in self.data.trie, ret_words),
                      key=lambda x: self.data.WORDS[x],
                      reverse=True)
