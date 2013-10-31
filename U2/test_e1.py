import unittest
from e1 import flatten_collection, flatten_dictionary


class FlattenCollectionTestCase(unittest.TestCase):
    def test_depth_1_list(self):
        self.assertEqual(flatten_collection([1, 2, 3], list), [1, 2, 3])

    def test_depth_1_tuple(self):
        self.assertEqual(flatten_collection([1, 2, 3], tuple), (1, 2, 3))

    def test_depth_2_list(self):
        self.assertEqual(flatten_collection([1, [u'5', u'6', u'7'], 3], list), [1, u'5', u'6', u'7', 3])

    def test_depth_2_tuple(self):
        self.assertEqual(flatten_collection([1, [u'5', u'6', u'7'], 3], tuple), (1, u'5', u'6', u'7', 3))

    def test_depth_3_list(self):
        self.assertEqual(flatten_collection([1, [u'5', (6, 6, 6), u'7'], [3, 3, 3]], list),
                         [1, u'5', 6, 6, 6, u'7', 3, 3, 3])

    def test_depth_3_tuple(self):
        self.assertEqual(flatten_collection([1, [u'5', (6, 6, 6), u'7'], [3, 3, 3]], tuple),
                         (1, u'5', 6, 6, 6, u'7', 3, 3, 3))


class FlattenDictionaryTestCase(unittest.TestCase):
    def test_depth_1(self):
        self.assertEqual(flatten_dictionary({'a': 1, 'b': 2, 'c': 3}), {'a': 1, 'b': 2, 'c': 3})

    def test_depth_2(self):
        self.assertEqual(flatten_dictionary({'a': 1, 'b': {'d': 4, 'e': 5}, 'c': 3}),
                         {'a': 1, 'b_d': 5, 'b_e': 5, 'c': 3})

    def test_depth_3(self):
        self.assertEqual(flatten_dictionary({'a': 1, 'b': {'d': 4, 'e': {'f': 6, 'g': 7}}, 'c': {'h': 8}}),
                         {'a': 1, 'b_d': 5, 'b_e_f': 6, 'b_e_g': 7, 'c_h': 8})

    def test_depth_2_no_crumbs(self):
        self.assertEqual(flatten_dictionary({'a': 1, 'b': {'d': 4, 'e': 5}, 'c': 3}, False),
                         {'a': 1, 'd': 4, 'e': 5, 'c': 3})

    def test_depth_3_no_crumbs(self):
        self.assertEqual(flatten_dictionary({'a': 1, 'b': {'a': 1, 'd': 4, 'e': {'f': 6, 'd': 7}}, 'c': {'h': 8}}, False),
                         {'a': [1, 1], 'd': [4, 7], 'f': 6, 'h': 8})
