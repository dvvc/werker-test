import unittest

import wercktest

class TestWercktest(unittest.TestCase):

    def test_main(self):
        self.assertEqual(wercktest.build_salute('foo'),
                         'Hello foo, this is version 0.0.1')

if __name__ == '__main__':
    unittest.main()
