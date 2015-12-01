import unittest

from trinine import t9


class Test9(unittest.TestCase):

    def setUp(self):
        self.t = t9.T9()

    def tearDown(self):
        self.t = None

    def test_load(self):
        self.assertEqual(False, 'data' in dir(self.t))
        self.t.load()
        self.assertEqual(True, 'data' in dir(self.t))

    def test_number_one_map(self):
        self.t.load()
        words = self.t.map_number(1234)
        self.assertEqual([], words)

    def test_number_map(self):
        self.t.load()
        char_list = self.t.map_number(4663)
        self.assertEqual([['g', 'h', 'i'],
                          ['m', 'n', 'o'],
                          ['m', 'n', 'o'],
                          ['d', 'e', 'f']],
                         char_list)

    def test_word_map(self):
        self.t.load()
        word_list = self.t.map_words(4663)
        self.assertEqual([u'gond', u'gone', u'good', u'home',
                          u'hond', u'hone', u'hood', u'hoof',
                          u'imme', u'inne', u'inof'],
                         word_list)

    def test_words(self):
        self.t.load()
        words = self.t.words(4663)
        self.assertEqual([u'home', u'good', u'gone',
                          u'hood', u'hoof', u'homepage',
                          u'homes', u'goods', u'immediately',
                          u'immediate'],
                         words)

    def test_two(self):
        self.t.load()
        words = self.t.words(2)
        self.assertEqual([u'a', u'c', u'b',
                          u'and', u'by', u'be',
                          u'are', u'at', u'as', u'all'],
                         words)

    def test_one(self):
        self.t.load()
        words = self.t.words(1)
        self.assertEqual([], words)
