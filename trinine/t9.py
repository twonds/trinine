"""
"""
import imp
import os
import sys


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

        self.suggest_length = 10
        self.word_length = 4

    def load(self):
        """
        Load up words and tri data structure that is saved to disk.
        If it does not exist then use existing data to build it.
        """
        if os.path.exists(self.data_module):
            self.data = imp.load_source('data', self.data_module)
        else:
            msg = "WARNING: Data module is not loaded. "
            msg += "Please build by running `make build-data`"
            print msg
            sys.exit(1)

    def map_number(self, number):
        """
        Map numbers from a dial pad to characters.

        @param number: A string of numbers dialed from a key pad.
        @type number: C{int}
        """
        ret_chars = []
        for num in str(number):
            chars = KEY_MAP[int(num)]
            if not chars:
                break
            ret_chars.append(chars)
        return ret_chars

    def _sort(self, words):
        return sorted(words,
                      key=lambda x: self.data.WORDS.get(x, 0),
                      reverse=True)

    def map_words(self, number):
        """
        Map a string of numbers from a phone's key pad to possible
        words.

        @param number: A string of numbers dialed from a key pad.
        @type number: C{int}
        """
        number_words = []
        for i, chars in enumerate(self.map_number(number)):
            if i == 0:
                number_words = chars
            else:
                new_words = []
                for word in number_words:
                    for c in chars:
                        new_word = word+c
                        # Only use words in our word trie
                        if self.data.TRIE.keys(new_word):
                            new_words.append(new_word)
                number_words = new_words
        return number_words

    def words(self, number):
        """
        Given a number return possible word combinations
        sorted by usage frequency.

        @param number: A string of numbers dialed from a key pad.
        @type number: C{int}
        """
        ret_words = []
        number_words = self.map_words(number)

        # Sort and filter words, adding extra words if our options are slim
        suggested_words = []
        for word in self._sort(number_words):
            if word in self.data.WORDS:
                ret_words.append(word)

            word_keys = filter(lambda x: x != word,
                               self._sort(self.data.TRIE.keys(word)))
            suggested_words += word_keys[:self.suggest_length]

        ret_words = ret_words + self._sort(suggested_words)

        return ret_words[:self.suggest_length]


def main_user_loop(t):
    while True:
        try:
            number = int(input("Enter a number: "))
        except EOFError:
            break
        except SyntaxError:
            break
        except TypeError:
            if number != 'quit':
                print "Invalid number"
            break
        for word in t.words(number):
            print word


def stdin_loop(t):
    for number in sys.stdin:
        if not number.strip():
            break
        number = int(number.strip())
        for word in t.words(number):
            print word


def main(data_dir, user_input=None):
    t = T9(data_dir=data_dir)
    # Load data module. Remember to build it.
    t.load()
    if user_input:
        main_user_loop(t)
    else:
        stdin_loop(t)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        usage = "Usage: {0} <data_directory>"
        print usage.format(sys.argv[0])
