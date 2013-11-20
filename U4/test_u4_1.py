import unittest
from u4_1 import check_date, find_in_xml


class U4TestCase(unittest.TestCase):

    def parse_xml(self):
        self.assertEqual(list(find_in_xml('''
            <one this="1" is="11" foo="111">
                <two this="2" is="22" bar="222" src="2222">
                    <three this="3" is="33" baz="333" />
                </two>
            </one>
            ''')),
            [('foo', '111'), ('bar','222'), ('baz', '333')]
        )

    def test_date_before(self):
        self.assertFalse(check_date('1981-04-14'))
        self.assertFalse(check_date('1980-04-30'))
        self.assertFalse(check_date('1000-01-01'))

    def test_date_in(self):
        self.assertTrue(check_date('1981-04-15'))
        self.assertTrue(check_date('1982-01-15'))
        self.assertTrue(check_date('1982-01-30'))
        self.assertTrue(check_date('1994-12-31'))
        self.assertTrue(check_date('1995-11-21'))
        self.assertTrue(check_date('1995-11-01'))

    def test_date_after(self):
        self.assertFalse(check_date('1995-11-22'))
        self.assertFalse(check_date('1996-01-01'))
        self.assertFalse(check_date('1999-11-15'))


if __name__ == "__main__":
    unittest.main()